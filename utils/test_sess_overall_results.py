

class TestSessOverallResults:

    def __init__(self):

        self._recall = -1.
        self._precision = -1.
        self._f_measure = -1.

    def __str__(self):

        rez = '\nRecall    :    ' + str(self.recall)
        rez += '\nPrecision :    ' + str(self.precision)
        rez += '\nF-measure :    ' + str(self.f_measure)

        rez += '\n\nThe overall result values are valid :  ' \
               + str(self.is_valid())

        return rez

    ##########################################################################
    # precision

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(
            self,
            value: float):
        if not isinstance(value, float) or value < .0 or value > 100.0:
            raise ValueError('Precision must be float and >= 0, <= 100.')

        self._precision = value

    ##########################################################################
    # recall

    @property
    def recall(self):
        return self._recall

    @recall.setter
    def recall(
            self,
            value: float):
        if not isinstance(value, float) or value < .0 or value > 100.0:
            raise ValueError('Recall must be float and >= 0, <= 100.')

        self._recall = value

    ##########################################################################
    # f_measure

    @property
    def f_measure(self):
        return self._f_measure

    @f_measure.setter
    def f_measure(
            self,
            value: float):
        if not isinstance(value, float) or value < .0 or value > 100.0:
            raise ValueError('F_measure must be float and >= 0, <= 100.')

        self._f_measure = value

    ##########################################################################
    # Public methods

    def is_valid(self):
        """
        :return: - True if valid.
                 - False otherwise.
        """

        if not isinstance(self.recall, float) \
                or not isinstance(self.f_measure, float) \
                or not isinstance(self.precision, float):
            return False

        if self.recall < .0 or self.recall > 100.0 \
                or self.f_measure < .0 or self.f_measure > 100.0 \
                or self.precision < .0 or self.precision > 100.0:
            return False

        return True

    ##########################################################################
