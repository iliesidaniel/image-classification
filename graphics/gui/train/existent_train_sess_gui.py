from graphics.output.train_sess.train_sess_details_output_f import TrainSessDetailsOutputF
from graphics.output.train_sess.train_sess_output_f import TrainSessOutputF

from file_experts.data_set.data_set_validator import DataSetValidator

from graphics.widgets.scrollable_canvas_c import ScrollableCanvasC
from graphics.widgets.validated_browse_f import ValidatedBrowseF
from graphics.widgets.session_buttons_f import SessionButtonsF
from graphics.widgets.combobox_input_f import ComboboxInputF
from graphics.widgets.browse_f import BrowseF

from utils.call_method_in_new_thread import CallMethodInNewThread

from controllers.data_set_controller import DataSetController
from controllers.session_controller import SessionController

from session.train_session import TrainSession

from tkinter import messagebox


import constants.gui_constants as const

import tkinter as tk


class ExistentTrainSessGUI(tk.Frame):

    def __init__(self,

                 parent,

                 enable_train_sess_buttons,
                 disable_train_sess_buttons):

        tk.Frame.__init__(self,
                          parent,
                          bg='light green')

        self._enable_train_sess_buttons = enable_train_sess_buttons
        self._disable_train_sess_buttons = disable_train_sess_buttons

        self._number_of_epochs_selected = False
        self._valid_data_set_selected = False
        self._train_session_selected = False
        self._test_data_set_path = ''
        self._first_start = True

        self._train_session = None

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

        self._data_set_browse = ValidatedBrowseF(
            self._sc_scrollable.f_main_frame,

            no_selection_message=const.ETS_DSB_NO_SELECTION,
            user_instruction=const.ETS_DSB_USER_INSTRUCTION,
            invalid_message=const.ETS_DSB_INVALID_MESSAGE,

            browse_window_title=const.ETS_DSB_WINDOW_TITLE,
            initial_directory=const.ETS_DSB_INITIAL_DIRECTORY,
            supported_files=const.ETS_DSB_SUPPORTED_FILES,

            validation_method=self._validate_data_set_selection,

            browse_button_eh=self._data_set_selected_eh,

            directory=False,
            disabled=True
        )

        self._number_of_epochs_input = ComboboxInputF(
            self._sc_scrollable.f_main_frame,

            user_instruction=const.ETS_EPOCHS_NBR_TEXT,
            user_options=const.ETS_EPOCHS_NBR_OPTIONS,

            selection_eh=self._number_of_epochs_selected_eh,

            disabled=True
        )

        self._train_sess_details_output = TrainSessDetailsOutputF(
            parent=self._sc_scrollable.f_main_frame,

            disabled=True
        )

        self._train_sess_browse = BrowseF(
            self._sc_scrollable.f_main_frame,

            no_selection_message=const.ETS_TSB_NO_SELECTION,
            user_instruction=const.ETS_TSB_USER_INSTRUCTION,
            browse_window_title=const.ETS_TSB_WINDOW_TITLE,
            initial_path=const.ETS_TSB_INITIAL_DIRECTORY,
            supported_files=const.ETS_TSB_SUPPORTED_FILES,

            browse_button_eh=self._train_session_selected_eh,

            directory=False,
            disabled=False
        )

        self._session_buttons = SessionButtonsF(
            parent=self._sc_scrollable.f_main_frame,

            start_eh=self._start_btn_eh,
            pause_eh=self._pause_btn_eh,
            stop_eh=self._stop_btn_eh,
            cancel_eh=self._cancel_btn_eh,

            disabled=True
        )

        self._train_sess_browse.config(
            pady=const.ETS_FRAME_PADY * 4,
        )

        self._session_buttons.config(
            pady=const.ETS_FRAME_PADY * 4,
        )

        # TODO

        """
        self._number_of_epochs_input.config(
            pady=30,
        )

        self._data_set_browse.config(
            pady=30,
        )
        """

    def _place_widgets(self):

        self._train_sess_browse.pack(side='top',
                                     fill='both',
                                     expand=True)

        self._train_sess_details_output.pack(side='top',
                                             fill='both',
                                             expand=True)

        # TODO

        """
        self._data_set_browse.pack(side='top',
                                   fill='both',
                                   expand=True)

        self._number_of_epochs_input.pack(side='top',
                                          fill='both',
                                          expand=True)
        """

        self._session_buttons.pack(side='top',
                                   fill='both',
                                   expand=True)

    #########################################################################
    # Event handling

    # ~~~~~~~~~~~~~~~~~~~~~Train session browse~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _train_session_selected_eh(
            self,

            selected_path):

        self._train_session_selected = True

        print('_train_session_selected_eh' + str(selected_path))

        # self._check_form_validity()   TODO

        self._alpha_version_check_form_validity()

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

        print('_data_set_selected_eh' + str(selected_path))

        # self._check_form_validity()   TODO

        self._alpha_version_check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Number of epochs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _number_of_epochs_selected_eh(
            self,

            number_of_epochs):

        self._number_of_epochs_selected = True

        print('_number_of_epochs_selected_eh' + str(number_of_epochs))

        # self._check_form_validity()   TODO

        self._alpha_version_check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Session buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _start_btn_eh(self):

        if self._first_start:
            self._first_start = False

            self._train_sess_details_output.destroy()
            # self._number_of_epochs_input.destroy()    TODO
            self._train_sess_browse.destroy()
            self._session_buttons.destroy()
            # self._data_set_browse.destroy()   TODO

            self._create_and_place_output_frame_and_canvas()

            self._session_buttons = SessionButtonsF(
                parent=self._sc_scrollable.f_main_frame,

                start_eh=self._start_btn_eh,
                pause_eh=self._pause_btn_eh,
                stop_eh=self._stop_btn_eh,
                cancel_eh=self._cancel_btn_eh,

                disabled=True
            )

            self._session_buttons.task_started()

            self._train_session_output = TrainSessOutputF(
                parent=self._sc_scrollable.f_main_frame,
            )

            self._session_buttons.pack(side='top',
                                       fill='both',
                                       expand=True)

            self._train_session_output.pack(side='top',
                                            fill='both',
                                            expand=True)

            self._train_session = TrainSession(
                add_message_method=self._train_session_output.new_message,
                training_finished=self.training_ended,
                data_set_details=self._data_set_details,
                session_details=self._session_details
            )

            CallMethodInNewThread.call_method(
                function_to_call=self._train_session.start_training
            )
        else:
            if self._train_session is not None:
                self._train_session.start_training()

        self._disable_train_sess_buttons()

    def _pause_btn_eh(self):

        if self._train_session is not None:
            self._train_session.pause_training()

    def _stop_btn_eh(self):

        if self._train_session is not None:
            self._train_session.stop_training()

    def _cancel_btn_eh(self):

        if self._train_session is not None:
            self._train_session.cancel_training()

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

    def _alpha_version_check_form_validity(self):

        if self._train_session_selected:
            self._train_sess_details_output.enable()
            self._session_buttons.enable()
        else:
            self._session_buttons.disable()
            self._train_sess_details_output.disable()

    def _check_form_validity(self):

        if self._train_session_selected:
            self._train_sess_details_output.enable()
            self._data_set_browse.enable()

            if self._valid_data_set_selected:
                self._number_of_epochs_input.enable()

                if self._number_of_epochs_selected:
                    self._session_buttons.enable()
                else:
                    self._session_buttons.disable()
            else:
                self._number_of_epochs_input.disable()
        else:
            self._train_sess_details_output.disable()
            self._number_of_epochs_input.disable()
            self._data_set_browse.disable()
            self._session_buttons.disable()

    #########################################################################
    # Public methods

    def training_ended(self):

        messagebox.showinfo(
            title='Training completed',
            message='Training completed.'
        )

        self._enable_train_sess_buttons()

    #########################################################################
