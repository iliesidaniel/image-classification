from datetime import datetime


class TrainSessMessage:

    def __init__(self):

        self._time = ''

        self._step = -1
        self._loss = -1.0
        self._examples_per_sec = -1.0
        self._seconds_per_batch = -1.0

    def __str__(self):

        rez = '\n\n---- Train session message ----n'
        rez += '\n\tTime              :    ' + str(self.time)
        rez += '\n\tSteps             :    ' + str(self.step)
        rez += '\n\tLoss              :    ' + str(self.loss)
        rez += '\n\tExamples per sec  :    ' + str(self.examples_per_sec)
        rez += '\n\tSeconds per batch :    ' + str(self.seconds_per_batch)
        rez += '\n---- Is valid : ' + str(self.is_valid()) + ' ----'

        return rez

    #########################################################################
    # time

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self,
             value: datetime):
        if not isinstance(value, datetime):
            raise ValueError('Description must be datetime.')

        self._time = "{:%d / %b / %Y   %H : %M : %S : %f}".format(
            value
            )

    #########################################################################
    # step

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self,
             value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError(
                'The number of steps per set must be integer and above 0, '
                'but got "'
                + str(value)
                + '".'
            )

        self._step = value

    #########################################################################
    # loss

    @property
    def loss(self):
        return self._loss

    @loss.setter
    def loss(self,
             value: float):
        if not isinstance(value, float) or value < 0.0:
            raise ValueError(
                'Loss must be float and above 0, but got "'
                + str(value)
                + '".'
            )

        self._loss = round(value, 3)

    #########################################################################
    # examples_per_set

    @property
    def examples_per_sec(self):
        return self._examples_per_sec

    @examples_per_sec.setter
    def examples_per_sec(self,
                         value: float):
        if not isinstance(value, float) or value < 0.0:
            raise ValueError(
                'The number of examples per second must be float and above'
                ' 0, but got "'
                + str(value)
                + '".'
            )

        self._examples_per_sec = round(value, 3)

    #########################################################################
    # seconds_per_batch

    @property
    def seconds_per_batch(self):
        return self._seconds_per_batch

    @seconds_per_batch.setter
    def seconds_per_batch(self,
                          value: float):
        if not isinstance(value, float) or value < 0.0:
            raise ValueError(
                'The number of seconds per batch must be float and above 0, '
                'but got "'
                + str(value)
                + '".'
            )

        self._seconds_per_batch = round(value, 3)

    #########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not isinstance(self.step, int) \
                or not isinstance(self.seconds_per_batch, float) \
                or not isinstance(self.examples_per_sec, float) \
                or not isinstance(self.loss, float) \
                or not isinstance(self.time, str):
            return False

        if self.seconds_per_batch < 0.0 \
                or self.examples_per_sec < 0.0 \
                or self.time != '' \
                or self.loss < 0.0 \
                or self.step < 0:
            return False

        return True

    #########################################################################
