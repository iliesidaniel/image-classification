from file_experts.data_set.image_reader import ImageReader
from utils.train.session_details import SessionDetails
from datetime import datetime


import constants.cnn_constants as cnn_const
import neural_networks.cnn as cnn
import tensorflow as tf


class InteractSession:

    def __init__(self,

                 session_details: SessionDetails,
                 update_guesses_and_time):

        self._session_details = session_details

        self._cnn = cnn.CNN(
            session_details=session_details,
            interact=True
        )

        self._update_guesses_and_time = update_guesses_and_time

    #########################################################################
    # Auxiliary methods

    def _evaluate_image(
            self,

            image_path: str):

        tf.reset_default_graph()

        image = ImageReader.decode_image_for_nn(
            path=image_path,

            height=self._session_details.image_size,
            width=self._session_details.image_size
        )

        tf.summary.image("image", [image])

        logits = self._cnn.create_cnn_model([image])

        softmax = tf.nn.softmax(
            logits,
            dim=-1,
            name=None
        )

        top_k_op = tf.nn.top_k(softmax, k=5)

        variable_averages = tf.train.ExponentialMovingAverage(
            cnn_const.CNN_MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

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

            summary_writer = tf.summary.FileWriter('/tmp/manualTest')

            # Start the queue runners.
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

                predictions, softmax_, logits_ = sess.run([top_k_op, softmax, logits])

                summary_op = tf.summary.merge_all()
                summary = tf.Summary()
                summary.ParseFromString(sess.run(summary_op))
                summary_writer.add_summary(summary, global_step)

                coord.request_stop()
                coord.join(threads, stop_grace_period_secs=10)

                return predictions
            except Exception as e:
                coord.request_stop(e)

            coord.request_stop()
            coord.join(threads, stop_grace_period_secs=10)

    #########################################################################
    # Public methods

    def evaluate_image(
            self,

            image_path: str):

        start_time = datetime.now()

        predictions = self._evaluate_image(
            image_path=image_path
        )

        end_time = datetime.now()

        execution_time = end_time - start_time

        labels = predictions[1][0]
        guesses = predictions[0][0]

        for index in range(len(guesses)):
            guesses[index] = int(guesses[index] * 100)

        self._update_guesses_and_time(
            labels,
            guesses,
            execution_time
        )

    #########################################################################
