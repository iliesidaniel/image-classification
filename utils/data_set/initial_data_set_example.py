

class InitialDataSetExample:

    def __init__(self):

        self._identifier = -1
        self._path = ''

    def __str__(self):

        rez = '\n---- Initial data set example ----'
        rez += '\nIdentifier :    ' + str(self.identifier)
        rez += '\nPath       :    ' + str(self.path)
        rez += '\n-- Is valid : ' + str(self.is_valid()) + ' --'

        rez = str(self.identifier) + '  ' + str(self.path)

        return rez

    ##########################################################################
    # identifier

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(
            self,
            value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Identifier must be integer and >= 0.')

        self._identifier = value

    ##########################################################################
    # path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(
            self,
            value: str):
        if not isinstance(value, str):
            raise ValueError('Path must be string and not empty.')

        self._path = value

    ##########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not isinstance(self.identifier, int) \
                or not isinstance(self.path, str) \
                or self.identifier < 0:
            return False

        return True

    ##########################################################################
