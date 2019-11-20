

class ChartEntry:

    def __init__(self):

        self._identifier = ''
        self._x = -1
        self._y = -1
        self._confidence_interval_95 = -1

    def __str__(self):

        rez = '\n## Is valid : ' + str(self.is_valid()) + ' ##'
        rez += '\nIdentifier  :    ' + self.identifier
        rez += '\nX           :    ' + str(self.x)
        rez += '\nY           :    ' + str(self.y)
        rez += '\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

        return rez

    ##########################################################################
    # identifier

    @property
    def identifier(self):
        return self._identifier

    @identifier .setter
    def identifier(self,
                   value: str):
        if not isinstance(value, str) \
                or value == '':
            raise ValueError('Identifier must be string and not empty.')

        self._identifier = value

    ##########################################################################
    # x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,
          value):
        if isinstance(value, float):
            value = int(round(value))

        if not isinstance(value, int) or value < 0:
            raise ValueError('X must be integer and >= 0.')

        self._x = value

    ##########################################################################
    # y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,
          value):
        if isinstance(value, float):
            value = int(round(value))

        if not isinstance(value, int) or value < 0:
            raise ValueError('Y must be integer and >= 0.')

        self._y = value

    ##########################################################################
    # confidence_interval_95

    @property
    def confidence_interval_95(self):
        return self._confidence_interval_95

    @confidence_interval_95.setter
    def confidence_interval_95(
            self,

            value):
        if not isinstance(value, float) or value < 0:
            raise ValueError('CI must be float and >= 0.')

        self._confidence_interval_95 = value

    ##########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not isinstance(self.identifier, str) or self.identifier == '' \
                or not isinstance(self.confidence_interval_95, float) \
                or self.confidence_interval_95 < 0 \
                or not isinstance(self.x, int) or self.x < 0 \
                or not isinstance(self.y, int) or self.y < 0:
            return False

        return True

    ##########################################################################
