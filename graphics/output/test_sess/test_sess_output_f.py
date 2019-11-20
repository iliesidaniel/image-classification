from graphics.output.test_sess.test_sess_overall_results_output_f import TestSessOverallResultsOutputF
from graphics.output.test_sess.test_sess_charts_f import TestSessChartsF

from graphics.output.confusion_matrix_output_f import ConfusionMatrixOutputF

from graphics.widgets.progress_bar_c import ProgressBarC

import constants.output_constants as const
import tkinter as tk


class TestSessOutputF(tk.Frame):
    """
    - Use to display all the elements that will be used to output the results 
    of an automated test session.
    - You have direct access for the components. For details check their 
    documentation/implementation.
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
                          parent)

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        self._f_progress_bar = tk.Frame(
            self,

            padx=const.TESO_SUBFRAME_PADX,
            pady=60,
        )

        self._f_results_output = tk.Frame(
            self,
        )

        self.progress_bar = ProgressBarC(
            parent=self._f_progress_bar,

            width=const.TESO_PB_WIDTH,
            height=const.TESO_PB_HEIGHT,

            text='Preparations - Please wait',
            fill_percent=0,

            fill_color=const.TESO_PB_FILL_COLORS,
            empty_color=const.TESO_PB_EMPTY_COLORS,
            text_color=const.TESO_PB_TEXT_COLORS
        )

        self.overall_results = TestSessOverallResultsOutputF(
            parent=self._f_results_output,
        )

        self.confusion_matrix = ConfusionMatrixOutputF(
            parent=self._f_results_output,
        )

        self.charts = TestSessChartsF(
            parent=self._f_results_output,
        )

    def _place_widgets(self):

        self.progress_bar.pack(side='top',
                               fill='both',
                               expand=True)

        self.overall_results.pack(side='top',
                                  fill='both',
                                  expand=True)

        self.confusion_matrix.pack(side='top',
                                   fill='both',
                                   expand=True)

        self.charts.pack(side='top',
                         fill='both',
                         expand=True)

        self._f_progress_bar.pack(side='top',
                                  fill='both',
                                  expand=True)

        self._f_results_output.pack(side='top',
                                    fill='both',
                                    expand=True)

    #########################################################################
    # Public methods

    def enable(self):
        """ Enables all the widgets."""

        self.confusion_matrix.enable()
        self.overall_results.enable()
        self.charts.enable()

    def disable(self):
        """ Disables all the widgets."""

        self.charts.disable()
        self.overall_results.disable()
        self.confusion_matrix.disable()

    #########################################################################
