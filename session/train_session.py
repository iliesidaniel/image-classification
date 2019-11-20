from utils.call_method_in_new_thread import CallMethodInNewThread
from utils.data_set.data_set_details import DataSetDetails
from utils.train.session_details import SessionDetails

from controllers.session_controller import SessionController

from session.logger_hook import LoggerHook


import constants.cnn_constants as cnn_const
import neural_networks.cnn as cnn

import tensorflow as tf
import threading
import time


class TrainSession(threading.Thread):

    def __init__(self,

                 add_message_method,
                 training_finished,
                 session_details: SessionDetails,
                 data_set_details: DataSetDetails):
        super(TrainSession, self).__init__()

        self._add_message_method = add_message_method
        self._training_finished = training_finished
        self._data_set_details = data_set_details
        self._session_details = session_details

        self._cnn = cnn.CNN(
            session_details=session_details
        )

        self._num_batches_per_epoch = \
            self._data_set_details.number_of_examples \
            / self._session_details.examples_per_batch

        self._number_of_steps = int(
            self._session_details.number_of_epochs
            * self._num_batches_per_epoch
        )

        self._stop_training = False
        self._pause_training = False
        self._cancel_training = False

    #########################################################################
    # Auxiliary methods

    def _train_helper(self, total_loss, global_step):

        decay_steps = int(
            self._num_batches_per_epoch
            * cnn_const.CNN_NUM_EPOCHS_PER_DECAY
        )

        lr = tf.train.exponential_decay(
            cnn_const.CNN_INITIAL_LEARNING_RATE,
            global_step,
            decay_steps,
            cnn_const.CNN_LEARNING_RATE_DECAY_FACTOR,
            staircase=True)

        tf.summary.scalar('learning_rate', lr)

        loss_averages_op = self._loss_summary(total_loss)

        with tf.control_dependencies([loss_averages_op]):
            opt = tf.train.GradientDescentOptimizer(lr)
            grads = opt.compute_gradients(total_loss)

        apply_gradient_op = opt.apply_gradients(
            grads_and_vars=grads,
            global_step=global_step
        )

        for var in tf.trainable_variables():
            tf.summary.histogram(var.op.name, var)

        for grad, var in grads:
            if grad is not None:
                tf.summary.histogram(
                    name=var.op.name + '/gradients',
                    values=grad
                )

        variable_averages = tf.train.ExponentialMovingAverage(
            cnn_const.CNN_MOVING_AVERAGE_DECAY, global_step)
        variables_averages_op = variable_averages.apply(
            var_list=tf.trainable_variables()
        )

        with tf.control_dependencies([apply_gradient_op, variables_averages_op]):
            train_op = tf.no_op(name='train')

        return train_op

    def _train(self):

        with tf.Graph().as_default():
            global_step = tf.contrib.framework.get_or_create_global_step()

            labels, images = SessionController.get_examples_for_train_session(
                session_details=self._session_details
            )

            tf.summary.image(
                tensor=images,
                name='image',
                max_outputs=100
            )

            logits = self._cnn.create_cnn_model(images)

            loss = self._calculate_loss(
                logits=logits,
                labels=labels
            )

            train_op = self._train_helper(loss, global_step)

            with tf.train.MonitoredTrainingSession(
                    checkpoint_dir=self._session_details.checkpoints_directory,
                    save_checkpoint_secs=cnn_const.CNN_CHECKPOINT_SAVE_INTERVAL,
                    hooks=[
                        tf.train.StopAtStepHook(
                            last_step=self._number_of_steps
                        ),
                        tf.train.NanTensorHook(loss),
                        LoggerHook(
                            add_message=self._update_session_status,
                            batch_size=self._session_details.examples_per_batch,
                            loss=loss
                        )
                    ],
                    config=tf.ConfigProto(
                        log_device_placement=False
                    )
            ) as mon_sess:
                while not mon_sess.should_stop():
                    while self._pause_training:
                        time.sleep(1)

                    if self._stop_training or self._cancel_training:
                        break

                    mon_sess.run(train_op)

        self._training_finished()

    @staticmethod
    def _calculate_loss(logits, labels):

        labels = tf.cast(labels, tf.int64)

        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
            name='cross_entropy_per_example',
            labels=labels,
            logits=logits
        )
        cross_entropy_mean = tf.reduce_mean(
            input_tensor=cross_entropy,
            name='cross_entropy'
        )
        tf.add_to_collection(
            name='losses',
            value=cross_entropy_mean
        )

        return tf.add_n(
            inputs=tf.get_collection(
                key='losses'
            ),
            name='total_loss'
        )

    @staticmethod
    def _loss_summary(total_loss):

        loss_averages = tf.train.ExponentialMovingAverage(0.9, name='avg')
        losses = tf.get_collection('losses')
        loss_averages_op = loss_averages.apply(losses + [total_loss])

        for l in losses + [total_loss]:
            tf.summary.scalar(l.op.name + ' (raw)', l)
            tf.summary.scalar(l.op.name, loss_averages.average(l))

        return loss_averages_op

    def _update_session_status(
            self,
            output):

        if not self._stop_training and not self._cancel_training:
            CallMethodInNewThread.call_method(
                function_to_call=self._add_message_method,
                message=output
            )

    #########################################################################
    # Public methods

    def run(self):

        self._train()

    def start_training(self):

        if self._pause_training:
            self._pause_training = False
        else:
            self.start()

    def pause_training(self):

        self._pause_training = True

    def stop_training(self):

        self._stop_training = True
        self._pause_training = False

    def cancel_training(self):

        self._cancel_training = True
        self._pause_training = False

    #########################################################################
