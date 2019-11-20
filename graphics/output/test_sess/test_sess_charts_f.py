import tkinter as tk

import constants.output_constants as const
from graphics.charts.column_chart import ColumnChart
from graphics.widgets.combobox_input_f import ComboboxInputF
from utils.charts.test_sess_charts import TestSessCharts


class TestSessChartsF(tk.Frame):
    """
    - Use to display charts with the results of the test session.
    """

    def __init__(self,

                 parent,

                 disabled=False):
        """
        :param parent: Parent.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          relief=const.TESC_FRAME_RELIEF,
                          padx=const.TESC_FRAME_PADX,
                          pady=const.TESC_FRAME_PADY,
                          bd=const.TESC_FRAME_BD)

        self._test_sess_charts = TestSessCharts()

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        self._lbl_title = tk.Label(
            self,

            font=const.TESC_TITLE_FONT,
            text=const.TESC_TITLE_TEXT,

            padx=const.TESC_TITLE_PADX,
            pady=const.TESC_TITLE_PADY,
        )

        self._f_output = tk.Frame(
            self,

            relief=const.TESC_SUBFRAME_RELIEF,
            padx=const.TESC_SUBFRAME_PADX,
            pady=const.TESC_SUBFRAME_PADY,
            bd=const.TESC_SUBFRAME_BD,
        )

        self._f_chart = tk.Frame(
            self._f_output,
        )

        self._ci_chart_to_display = ComboboxInputF(
            parent=self._f_output,

            user_instruction=const.TESC_CHARTS_TEXT,
            user_options=const.TESC_CHARTS_OPTIONS,

            selection_eh=self._chart_selected_eh,
        )

        self._column_chart = ColumnChart(
            parent=self._f_chart
        )

    def _place_widgets(self):

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._ci_chart_to_display.pack(side='top',
                                       fill='both',
                                       expand=True)

        self._column_chart.pack(side='top')

        self._f_chart.place(in_=self._column_chart,
                            anchor="c",
                            relx=.5,
                            rely=.5)

        self._f_chart.pack(side='top',
                           fill='both',
                           expand=True)

        self._f_output.pack(side='top',
                            fill='both',
                            expand=True)

    #########################################################################
    # Event handling

    def _chart_selected_eh(
            self,

            selected_text: str):
        """
        - Called when the user selects a chart name.
        
        :param selected_text: selected text. 
        """

        chart = self._test_sess_charts.get_chart(selected_text)

        if chart is not None:
            self._column_chart.update_values(chart_entries=chart)

    #########################################################################
    # Public methods

    def update_chart_values(
            self,

            test_sess_charts: TestSessCharts):
        """
        - Updates the charts details.
        
        :param test_sess_charts: Details about the charts, it must be a 
                                 valid instance of TestSessCharts or it will
                                 raise ValueError.
        """

        if isinstance(test_sess_charts, TestSessCharts) \
                and test_sess_charts.is_valid():
            self._test_sess_charts = test_sess_charts
        else:
            raise ValueError('test_sess_charts is not a valid instance of '
                             'TestSessCharts')

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_title.config(state='normal')
        self._ci_chart_to_display.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._ci_chart_to_display.disable()
        self._lbl_title.config(state='disabled')

    #########################################################################
