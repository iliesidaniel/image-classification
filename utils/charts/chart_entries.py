from utils.charts.chart_entry import ChartEntry


class ChartEntries:

    def __init__(self):

        self._entries = []

    def __str__(self):

        sep = '\n#########################################################'

        rez = '\n' + sep
        rez += '\nChart entries:' + sep

        for entry in self._entries:
            rez += str(entry)

        rez += '\n## Is valid : ' + str(self.is_valid()) + ' ##'
        rez += sep

        return rez

    #########################################################################
    # Public methods

    def add(self,
            new_entry: ChartEntry):
        """
        - Adds a new entry to the list if the new_data_set parameter is an 
        instance of the UsedDataSet class and also valid.

        :param new_entry: ChartEntry instance.
        """

        if isinstance(new_entry, ChartEntry) and new_entry.is_valid():
            self._entries.append(new_entry)
        else:
            raise ValueError('new_entry parameter must be an instance of '
                             'the ChartEntry class and also it must be '
                             'valid.')

    def get_entries(self):
        """
        :return: ChartEntry list
        """

        return self._entries

    def clear(self):
        """
        - Clears the list.
        """

        self._entries.clear()

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self._entries:
            return False

        for entry in self._entries:
            if not isinstance(entry, ChartEntry):
                return False
            elif not entry.is_valid():
                return False

        return True

    #########################################################################


