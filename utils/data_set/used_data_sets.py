from utils.data_set.data_set_details import DataSetDetails


class UsedDataSets:

    def __init__(self):

        self._used_data_sets = []

    def __str__(self):

        rez = '\n&&&& Used data sets &&&&\n'

        for data_set in self._used_data_sets:
            rez += str(data_set)

        rez += '\n&& Is valid : ' + str(self.is_valid()) + ' &&'

        return rez

    #########################################################################
    # Public methods

    def add(self,
            new_data_set: DataSetDetails):
        """
        - Adds a new entry to the list if the new_data_set parameter is an 
        instance of the UsedDataSet class and also valid.

        :param new_data_set: DataSetDetails instance.
        """

        if isinstance(new_data_set, DataSetDetails) and new_data_set.is_valid():
            self._used_data_sets.append(new_data_set)
        else:
            raise ValueError('new_data_set parameter must be an instance of '
                             'the UsedDataSet class and also it must be '
                             'valid.')

    def get_used_data_sets(self):
        """
        :return: DataSetDetails list
        """

        return self._used_data_sets

    def clear(self):
        """
        - Clears the list.
        """

        self._used_data_sets.clear()

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self._used_data_sets:
            return False

        for data_set in self._used_data_sets:
            if not isinstance(data_set, DataSetDetails):
                return False
            elif not data_set.is_valid():
                return False

        return True

    #########################################################################
