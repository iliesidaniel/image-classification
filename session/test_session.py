from controllers.data_set_controller import DataSetController
from controllers.session_controller import SessionController

from utils.train.session_details import SessionDetails


import constants.cnn_constants as cnn_const
import neural_networks.cnn as cnn

import tensorflow as tf
import threading
import math


class TestSession(threading.Thread):

    def __init__(self,

                 session_details: SessionDetails,
                 test_data_set_path: str,
                 automated_test_session,
                 testing_finished):

        super(TestSession, self).__init__()

        self._test_data_set_path = test_data_set_path
        self._testing_finished = testing_finished
        self._session_details = session_details
        self._GUI = automated_test_session

        self._confusion_matrix = [
            [
                0
                for _ in range(self._session_details.number_of_classes)
            ]
            for _ in range(self._session_details.number_of_classes)
        ]

        self._cnn = cnn.CNN(
            session_details=session_details
        )

        self.stop_testing = False

    #########################################################################
    # Auxiliary methods

    def _test(self):

        with tf.Graph().as_default() as graph:

            self._test_data_set_details = DataSetController.read_main_data_set_file(
                file_path=self._test_data_set_path
            )

            labels, images = SessionController.get_examples_for_test_session(
                test_data_set_details=self._test_data_set_details,
                session_details=self._session_details
            )

            logits = self._cnn.create_cnn_model(images)

            top_k_op = tf.nn.top_k(logits,  1)

            summary_op = tf.summary.merge_all()

            summary_writer = tf.summary.FileWriter(
                logdir=self._session_details.checkpoints_directory,
                graph=graph
            )

            variable_averages = tf.train.ExponentialMovingAverage(
                cnn_const.CNN_MOVING_AVERAGE_DECAY

            )
            variables_to_restore = variable_averages.variables_to_restore()

            saver = tf.train.Saver(variables_to_restore)

            writer = tf.summary.FileWriter(
                logdir=self._session_details.checkpoints_directory
            )

            with tf.Session() as sess:
                checkpoint = tf.train.get_checkpoint_state(
                    checkpoint_dir=self._session_details.checkpoints_directory
                )

                if checkpoint and checkpoint.model_checkpoint_path:
                    saver.restore(sess, checkpoint.model_checkpoint_path)
                    global_step = checkpoint.model_checkpoint_path.split('/')[-1].split('-')[-1]
                else:
                    print('No checkpoint file found')
                    return

                coord = tf.train.Coordinator()
                threads = []
                try:
                    for qr in tf.get_collection(tf.GraphKeys.QUEUE_RUNNERS):
                        threads.extend(
                            qr.create_threads(
                                sess,
                                coord=coord,
                                daemon=True,
                                start=True
                            )
                        )

                    num_iter = int(
                        math.ceil(
                            self._test_data_set_details.number_of_examples
                            / self._session_details.examples_per_batch
                        )
                    )

                    left_to_check = \
                        self._test_data_set_details.number_of_examples

                    step = 0

                    while step < num_iter and not coord.should_stop():

                        predictions, label, img = sess.run(
                            [
                                top_k_op,
                                labels,
                                images
                            ]
                        )

                        for index in range(len(label)):

                            b = predictions.indices[index][0]
                            a = label[index]

                            self._confusion_matrix[a][b] \
                                = self._confusion_matrix[a][b] \
                                + 1

                            left_to_check -= 1

                            if left_to_check == 0:
                                break

                        step += 1
                        percent = int(step / num_iter * 100)

                        self._GUI.update_test_progress(
                            progress=percent
                        )

                    if not self.stop_testing:
                        summary = tf.Summary()
                        summary.ParseFromString(sess.run(summary_op))
                        summary_writer.add_summary(summary, global_step)

                except Exception as e:
                    coord.request_stop(e)

                    writer.close()

                coord.request_stop()
                coord.join(threads, stop_grace_period_secs=10)

            writer.close()

    #########################################################################
    # Public methods

    def run(self):

        self._test()

        self._GUI.confusion_matrix_update_method(
            confusion_matrix=self._confusion_matrix
        )

        self._testing_finished()

    def start_test(self):

        self.start()

    #########################################################################
