from graphics.widgets.single_line_output_f import SingleLineOutputF
from utils.test_sess_overall_results import TestSessOverallResults

import constants.output_constants as const
import tkinter as tk


class TestSessOverallResultsOutputF(tk.Frame):
    """
    - Use to display overall results for a test session.
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
                          relief=const.TSOR_FRAME_RELIEF,
                          padx=const.TSOR_FRAME_PADX,
                          pady=const.TSOR_FRAME_PADY,
                          bd=const.TSOR_FRAME_BD)

        self._slo_identifiers_classes = []

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        self._lbl_title = tk.Label(
            self,

            font=const.TSOR_TITLE_FONT,
            text=const.TSOR_TITLE_TEXT,

            padx=const.TSOR_TITLE_PADX,
            pady=const.TSOR_TITLE_PADY,
        )

        self._f_results = tk.Frame(
            self,

            relief=const.TSOR_SUBFRAME_RELIEF,
            padx=const.TSOR_SUBFRAME_PADX,
            pady=const.TSOR_SUBFRAME_PADY,
            bd=const.TSOR_SUBFRAME_BD
        )

        self._slo_subtitle = SingleLineOutputF(
            parent=self,

            description_width=28,

            font=const.TSOR_SUBTITLE_FONT,
            description=const.TSOR_SUBTITLE_EVAL_METHOD_TEXT,
            output_text=const.TSOR_SUBTITLE_RESULT_TEXT
        )

        self._slo_precision = SingleLineOutputF(
            parent=self._f_results,

            description_width=26,

            font=const.TSOR_FONT,
            description=const.TSOR_PRECISION_TEXT,
            output_text=const.TSOR_PRECISION_INITIAL_TEXT
        )

        self._slo_recall = SingleLineOutputF(
            parent=self._f_results,

            description_width=26,

            font=const.TSOR_FONT,
            description=const.TSOR_RECALL_TEXT,
            output_text=const.TSOR_RECALL_INITIAL_TEXT
        )

        self._slo_f_measure = SingleLineOutputF(
            parent=self._f_results,

            description_width=26,

            font=const.TSOR_FONT,
            description=const.TSOR_F_MEASURE_TEXT,
            output_text=const.TSOR_F_MEASURE_INITIAL_TEXT
        )

    def _place_widgets(self):

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._slo_subtitle.pack(side='top',
                                fill='both',
                                expand=True)

        self._slo_precision.pack(side='top',
                                 fill='both',
                                 expand=True)
        self._slo_recall.pack(side='top',
                              fill='both',
                              expand=True)
        self._slo_f_measure.pack(side='top',
                                 fill='both',
                                 expand=True)

        self._f_results.pack(side='top',
                             fill='both',
                             expand=True)

    #########################################################################
    # Public methods

    def update_results(
            self,

            overall_results: TestSessOverallResults):
        """
        - Updates the results.
        
        :param overall_results: Overall test session results. 
        """

        if overall_results.is_valid():
            self._slo_precision.update_output(
                output_text='%.2f' % overall_results.precision)

            self._slo_recall.update_output(
                output_text='%.2f' % overall_results.recall)

            self._slo_f_measure.update_output(
                output_text='%.2f' % overall_results.f_measure)
        else:
            raise ValueError('Overall results are not valid:\n\n'
                             + str(overall_results))

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_title.config(state='normal')
        self._slo_precision.enable()
        self._slo_f_measure.enable()
        self._slo_subtitle.enable()
        self._slo_recall.enable()

        for item in self._slo_identifiers_classes:
            item.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._slo_recall.disable()
        self._slo_subtitle.disable()
        self._slo_f_measure.disable()
        self._slo_precision.disable()
        self._lbl_title.config(state='disabled')

    #########################################################################
