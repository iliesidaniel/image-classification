from utils.train.train_sess_message import TrainSessMessage

from datetime import datetime


import constants.cnn_constants as cnn_const

import tensorflow as tf
import time


class LoggerHook(tf.train.SessionRunHook):

    def __init__(self,

                 add_message,
                 batch_size,
                 loss):
        super().__init__()

        self._add_message = add_message
        self._batch_size = batch_size
        self._start_time = None
        self._loss = loss
        self._step = -1

    def before_run(self, run_context):

        self._step += 1
        self._start_time = time.time()

        return tf.train.SessionRunArgs(self._loss)

    def after_run(self, run_context, run_values):

        duration = time.time() - self._start_time
        loss_value = run_values.results

        if self._step % cnn_const.CNN_STATUS_UPDATE_INTERVAL == 0:
            output = self.create_output(
                duration=duration,
                loss_value=loss_value
            )

            self._add_message(output)

    def create_output(self, duration, loss_value):

        num_examples_per_step = self._batch_size
        examples_per_sec = num_examples_per_step / duration
        sec_per_batch = float(duration)

        message = TrainSessMessage()

        message.time = datetime.now()
        message.step = self._step
        message.loss = float(loss_value)
        message.examples_per_sec = float(examples_per_sec)
        message.seconds_per_batch = float(sec_per_batch)

        return message

#############################################################################
