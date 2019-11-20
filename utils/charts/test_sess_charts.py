from copy import deepcopy

import constants.test_sess_constants as const
from utils.charts.chart_entries import ChartEntries
from utils.charts.test_sess_chart import TestSessChart


class TestSessCharts:
    def __init__(self):

        self._charts = []

    def __str__(self):

        sep = '\n*********************************************************'

        rez = '\n' + sep
        rez += '\nCharts:' + sep

        for chart in self._charts:
            rez += str(chart)

        rez += '\n** Is valid : ' + str(self.is_valid()) + ' **'
        rez += sep

        return rez

    #########################################################################
    # Auxiliary methods

    def _add(self,
             chart_name: str,
             chart_details: ChartEntries):
        """
        - Adds a new entry to the list if the chart_details parameter is an
        instance of the ChartEntries class and also valid.

        :param chart_details: ChartEntries instance.
        """

        if isinstance(chart_details, ChartEntries) \
                and chart_details.is_valid():
            new_tsc = TestSessChart()

            new_tsc.chart_name = chart_name
            new_tsc.entries = chart_details

            self._charts.append(new_tsc)
        else:
            raise ValueError('new_entry parameter must be an instance of '
                             'the ChartEntries class and also it must be '
                             'valid.')

    #########################################################################
    # Public methods

    def set_precision_chart(
            self,
            chart_details: ChartEntries):
        """
        - Set/update the precision chart.

        :param chart_details: Chart details.
        """

        self._add(const.TER_PRECISION_TEXT,
                  chart_details=chart_details)

    def set_recall_chart(
            self,
            chart_details: ChartEntries):
        """
        - Set/update the recall chart.

        :param chart_details: Chart details.
        """

        self._add(const.TER_RECALL_TEXT,
                  chart_details=chart_details)

    def set_f_measure_chart(
            self,
            chart_details: ChartEntries):
        """
        - Set/update the f-measure chart.

        :param chart_details: Chart details.
        """

        self._add(const.TER_F_MEASURE_TEXT,
                  chart_details=chart_details)

    def get_entries(self):
        """
        :return: Deepcopy of the TestSessChart list.
        """

        return deepcopy(self._charts)

    def get_chart(
            self,

            chart_name: str):
        """
        - If the chart_name parameter is valid returns a deepcopy of the
        requested chart.

        :param chart_name: Chart name.
        """

        if chart_name not in const.TER_METHODS_LIST:
            raise ValueError('Chart name must be string and it must be in '
                             'test_sess_constants.TER_METHODS_LIST.')

        for chart in self._charts:
            if chart.chart_name == chart_name:
                return deepcopy(chart)

    def clear(self):
        """
        - Clears the list.
        """

        self._charts.clear()

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self._charts:
            return False

        for entry in self._charts:
            if not isinstance(entry, TestSessChart):
                return False
            elif not entry.is_valid():
                return False

        return True

    #########################################################################
