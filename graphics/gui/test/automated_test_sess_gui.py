import tkinter as tk

import constants.gui_constants as const
from controllers.data_set_controller import DataSetController
from controllers.session_controller import SessionController
from file_experts.data_set.data_set_validator import DataSetValidator
from graphics.output.test_sess.test_sess_output_f import TestSessOutputF
from graphics.output.train_sess.train_sess_details_output_f import TrainSessDetailsOutputF
from graphics.widgets.browse_f import BrowseF
from graphics.widgets.scrollable_canvas_c import ScrollableCanvasC
from graphics.widgets.validated_browse_f import ValidatedBrowseF
from session.test_session import TestSession
from utils.charts.chart_entries import ChartEntries
from utils.charts.chart_entry import ChartEntry
from utils.charts.test_sess_charts import TestSessCharts
from utils.test_sess_overall_results import TestSessOverallResults


class AutomatedTestSessGUI(tk.Frame):

    def __init__(self,

                 parent,

                 enable_test_sess_buttons,
                 disable_test_sess_buttons):
        """
        :param parent: 
        :param enable_test_sess_buttons: 
        :param disable_test_sess_buttons: 
        """

        tk.Frame.__init__(self,
                          parent)

        self._disable_test_sess_buttons = disable_test_sess_buttons
        self._enable_test_sess_buttons = enable_test_sess_buttons

        self._valid_data_set_selected = False
        self._train_session_selected = False

        self._test_data_set_path = ''
        self._session_details = None

        self._sc_scrollable = None
        self._f_output = None

        self._create_widgets()
        self._place_widgets()

    #########################################################################
    # Widget creation and placement

    def _create_and_place_output_frame_and_canvas(self):

        if self._sc_scrollable:
            self._sc_scrollable.destroy()
            del self._sc_scrollable

        if self._f_output:
            self._f_output.destroy()
            del self._f_output

        self._f_output = tk.Frame(
            self,
        )

        self._sc_scrollable = ScrollableCanvasC(
            parent=self._f_output,
        )

        self._sc_scrollable.pack(side='top',
                                 fill='both',
                                 expand=True)

        self._f_output.pack(side='top',
                            fill='both',
                            expand=True)

    def _create_widgets(self):

        self._create_and_place_output_frame_and_canvas()

        self._f_start_btn = tk.Frame(
            self._sc_scrollable.f_main_frame,

            padx=const.ATS_SUBFRAME_PADX,
            pady=const.ATS_SUBFRAME_PADY,
        )

        self._train_sess_browse = BrowseF(
            self._sc_scrollable.f_main_frame,

            no_selection_message=const.ATS_TSB_NO_SELECTION,
            user_instruction=const.ATS_TSB_USER_INSTRUCTION,

            browse_window_title=const.ATS_TSB_WINDOW_TITLE,
            supported_files=const.ATS_TSB_SUPPORTED_FILES,
            initial_path=const.ATS_TSB_INITIAL_DIRECTORY,

            browse_button_eh=self._train_session_selected_eh,

            directory=False,
            disabled=False
        )

        self._data_set_browse = ValidatedBrowseF(
            self._sc_scrollable.f_main_frame,

            no_selection_message=const.ATS_DSB_NO_SELECTION,
            user_instruction=const.ATS_DSB_USER_INSTRUCTION,
            invalid_message=const.ATS_DSB_INVALID_MESSAGE,

            browse_window_title=const.ATS_DSB_WINDOW_TITLE,
            initial_directory=const.ATS_DSB_INITIAL_DIRECTORY,
            supported_files=const.ATS_DSB_SUPPORTED_FILES,

            validation_method=self._validate_data_set_selection,

            browse_button_eh=self._data_set_selected_eh,

            directory=False,
            disabled=True
        )

        self._train_sess_details_output = TrainSessDetailsOutputF(
            parent=self._sc_scrollable.f_main_frame,

            disabled=True
        )

        self._start_button = tk.Button(
            self._f_start_btn,

            command=self._start_btn_eh,
            text=const.ATS_BTN_TEXT,
            font=const.ATS_FONT,

            padx=const.ATS_START_BTN_PADX,
            pady=const.ATS_START_BTN_PADY,
            bd=const.ATS_START_BTN_BD,

            state='disabled'
        )

        self._data_set_browse.config(
            pady=const.ETS_FRAME_PADY * 2,
        )

        self._train_sess_browse.config(
            pady=const.ETS_FRAME_PADY * 4,
        )

    def _place_widgets(self):

        self._train_sess_browse.pack(side='top',
                                     fill='both',
                                     expand=True)

        self._train_sess_details_output.pack(side='top',
                                             fill='both',
                                             expand=True)

        self._data_set_browse.pack(side='top',
                                   fill='both',
                                   expand=True)

        self._f_start_btn.pack(side='top',
                               fill='both',
                               expand=True)

        self._start_button.pack(side='top')

    #########################################################################
    # Event handling

    # ~~~~~~~~~~~~~~~~~~~~~Train session browse~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _train_session_selected_eh(
            self,

            selected_path):

        self._train_session_selected = True

        self._check_form_validity()

        self._session_details = SessionController.read_main_session_file(
            session_file_path=selected_path
        )

        self._data_set_details = DataSetController.read_main_data_set_file(
            file_path=self._session_details.main_data_set_file
        )

        self._train_sess_details_output.update_session_details(
            data_set_details=self._data_set_details,
            session_details=self._session_details
        )

    # ~~~~~~~~~~~~~~~~~~~~~Data set browse~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _data_set_selected_eh(
            self,

            selected_path):

        self._valid_data_set_selected = True

        self._session_details.current_data_set_path = selected_path

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Session buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _start_btn_eh(self):

        self._create_and_place_output_frame_and_canvas()

        self._test_sess_output = TestSessOutputF(
            parent=self._sc_scrollable.f_main_frame
        )

        self._test_sess_output.confusion_matrix.set_classes(
            data_set_classes=self._data_set_details.classes.get_data_set_classes()
        )

        self._test_sess_output.pack(side='top',
                                    fill='both',
                                    expand=True)

        self._disable_test_sess_buttons()

        self._train_sess_details_output.destroy()
        self._train_sess_browse.destroy()
        self._data_set_browse.destroy()
        self._start_button.destroy()
        self._f_start_btn.destroy()

        self._test_session = TestSession(
            test_data_set_path=self._test_data_set_path,
            session_details=self._session_details,
            testing_finished=self.session_ended,
            automated_test_session=self
        )

        self._test_session.start_test()

    #########################################################################
    # Auxiliary methods

    def _validate_data_set_selection(
            self,

            selected_path):

        self._test_data_set_path = selected_path

        data_set_details = DataSetController.read_main_data_set_file(
            file_path=selected_path
        )

        return DataSetValidator.data_set_and_session_are_compatible(
            session_details=self._session_details,
            data_set_details=data_set_details
        )

    def _check_form_validity(self):

        if self._train_session_selected:
            self._train_sess_details_output.enable()
            self._data_set_browse.enable()

            if self._valid_data_set_selected:
                self._start_button.config(state='norma')
            else:
                self._start_button.config(state='disabled')
        else:
            self._start_button.config(state='disabled')
            self._train_sess_details_output.disable()
            self._data_set_browse.disable()

    def _update_progress(
            self,

            progress_text: str,
            progress_value: int):
        """
        - Updates the progress bar.
        """

        if not isinstance(progress_value, int) \
                or progress_value < 0:
            raise ValueError('Value provided '
                             + str(progress_value)
                             + '. It must be an integer >=0 and <=100.')

        if progress_value > 100:
            progress_value = 100

        self._test_sess_output.progress_bar.update_progress(
            percent=progress_value,
            text=progress_text
        )

    def _process_test_results(self, confusion_matrix):

        self._test_sess_output.confusion_matrix.set_confusion_matrix(confusion_matrix)

        classes = self._data_set_details.classes.get_data_set_classes()

        overall_results = TestSessOverallResults()
        test_charts = TestSessCharts()

        ces_precision = ChartEntries()
        ces_f_measure = ChartEntries()
        ces_recall = ChartEntries()

        avg_precision = 0.
        avg_f_measure = 0.
        avg_recall = 0.

        f_measure = []
        precision = []
        recall = []

        line = []
        col = []

        for i in range(len(confusion_matrix)):
            line.append(0)
            col.append(0)

            for j in range(len(confusion_matrix)):
                line[i] = line[i] + confusion_matrix[i][j]

                col[i] = col[i] + confusion_matrix[j][i]

        for i in range(len(confusion_matrix)):
            recall.append(confusion_matrix[i][i] / col[i] * 100)
            avg_recall += recall[i]

            precision.append(confusion_matrix[i][i] / line[i] * 100)
            avg_precision += precision[i]

            if precision[i]+recall[i] != 0:
                tmp_recall = 2 \
                             * (
                                 (precision[i] * recall[i])
                                 / (precision[i] + recall[i])
                             )
            else:
                tmp_recall = 0

            f_measure.append(tmp_recall)
            avg_f_measure += f_measure[i]

        avg_precision = float(avg_precision / len(confusion_matrix))
        avg_f_measure = float(avg_f_measure / len(confusion_matrix))
        avg_recall = float(avg_recall / len(confusion_matrix))

        overall_results.recall = avg_recall
        overall_results.f_measure = avg_f_measure
        overall_results.precision = avg_precision

        self._test_sess_output.overall_results.update_results(
            overall_results=overall_results
        )

        for i in range(len(confusion_matrix)):
            # Recall
            tmp_recall = ChartEntry()

            tmp_recall.identifier = classes[i].class_name
            tmp_recall.x = 0
            tmp_recall.y = recall[i]
            tmp_recall.confidence_interval_95 = 0.

            ces_recall.add(new_entry=tmp_recall)

            # Precision
            tmp_precision = ChartEntry()

            tmp_precision.identifier = classes[i].class_name
            tmp_precision.x = 0
            tmp_precision.y = precision[i]
            tmp_precision.confidence_interval_95 = 0.

            ces_precision.add(new_entry=tmp_precision)

            # F measure
            tmp_f_measure = ChartEntry()

            tmp_f_measure.identifier = classes[i].class_name
            tmp_f_measure.x = 0
            tmp_f_measure.y = f_measure[i]
            tmp_f_measure.confidence_interval_95 = 0.

            ces_f_measure.add(new_entry=tmp_f_measure)

        test_charts.set_precision_chart(ces_precision)
        test_charts.set_recall_chart(ces_recall)
        test_charts.set_f_measure_chart(ces_f_measure)

        self._test_sess_output.charts.update_chart_values(test_charts)

    #########################################################################
    # Public methods

    def confusion_matrix_update_method(
            self,
            confusion_matrix):

        self._process_test_results(confusion_matrix)

    def session_ended(self):

        self._enable_test_sess_buttons()

        print('Session ended.')

    def update_test_progress(
            self,

            progress: int):
        """
        - Updates the progress bar with the current download percentage.
        """

        if progress != 100:
            text = 'Testing  -  ' \
                   + str(progress) \
                   + '% completed'
        else:
            text = 'Test session completed! You can check the results.'

        self._update_progress(
            progress_value=progress,
            progress_text=text
        )

    #########################################################################
