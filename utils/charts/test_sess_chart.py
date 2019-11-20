from copy import deepcopy

import constants.test_sess_constants as const
from utils.charts.chart_entries import ChartEntries


class TestSessChart:

    def __init__(self):

        self.entries = ChartEntries()
        self._chart_name = ''

    def __str__(self):

        sep = '\n========================================================='

        rez = '\n' + sep
        rez += '\nChart details:' + sep

        for entry in self.entries.get_entries():
            rez += str(entry)

        rez += '\n== Is valid : ' + str(self.is_valid()) + ' =='
        rez += sep

        return rez

    ##########################################################################
    # chart_name

    @property
    def chart_name(self):
        return self._chart_name

    @chart_name.setter
    def chart_name(self,
                   value: str):
        if value not in const.TER_METHODS_LIST \
                or not isinstance(value, str):
            raise ValueError('Chart name must be string and it must be in '
                             'test_sess_constants.TER_METHODS_LIST.')

        self._chart_name = value

    #########################################################################

    def get_entries(self):
        """
        :return: Deepcopy of entries.get_entries() 
        """

        return deepcopy(self.entries.get_entries())

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self.entries.is_valid():
            return False

        if not isinstance(self.chart_name, str) \
                or self.chart_name == '':
            return False

        return True

    #########################################################################
