

class ClassCorrelationBetweenDataSets:

    def __init__(self):

        self._identifier_in_new_data_set = -1
        self._identifier_in_old_data_set = ''

    def __str__(self):

        rez = '\n---- Class correlation between data sets ----\n'

        rez += '\nIdentifier in new data set :    ' \
               + str(self.identifier_in_new_data_set)
        rez += '\nIdentifier in old data set :    ' \
               + str(self.identifier_in_old_data_set)

        rez += '\n\n-- Is valid : ' + str(self.is_valid()) + ' --'

        return rez

    ##########################################################################
    # identifier_in_new_data_set

    @property
    def identifier_in_new_data_set(self):
        return self._identifier_in_new_data_set

    @identifier_in_new_data_set.setter
    def identifier_in_new_data_set(
            self,
            value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Identifier in new data set must be integer and'
                             ' not < 0.')

        self._identifier_in_new_data_set = value

    ##########################################################################
    # identifier_in_old_data_set

    @property
    def identifier_in_old_data_set(self):
        return self._identifier_in_old_data_set

    @identifier_in_old_data_set.setter
    def identifier_in_old_data_set(
            self,
            value: str):
        if not isinstance(value, str) or value == '':
            raise ValueError('Identifier in old data set must be string and '
                             'not empty.')

        self._identifier_in_old_data_set = value

    ##########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not isinstance(self.identifier_in_new_data_set, int) \
                or self.identifier_in_new_data_set < 0:
            return False

        if not isinstance(self.identifier_in_old_data_set, str) \
                or self.identifier_in_old_data_set == '':
            return False

        return True

    ##########################################################################
