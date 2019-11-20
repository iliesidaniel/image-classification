from graphics.output.train_sess.train_sess_details_output_f import TrainSessDetailsOutputF
from graphics.output.train_sess.train_sess_output_f import TrainSessOutputF
from graphics.output.test_sess.test_sess_output_f import TestSessOutputF

from graphics.widgets.scrollable_canvas_c import ScrollableCanvasC
from graphics.widgets.session_buttons_f import SessionButtonsF
from graphics.widgets.combobox_input_f import ComboboxInputF
from graphics.widgets.browse_f import BrowseF

from utils.train.train_sess_message import TrainSessMessage


import constants.gui_constants as const
import tkinter as tk


class ExistentKFoldCVSessGUI(tk.Frame):

    def __init__(self,

                 parent,

                 enable_k_fold_cv_sess_buttons,
                 disable_k_fold_cv_sess_buttons):
        """
        :param parent: 
        :param enable_k_fold_cv_sess_buttons: 
        :param disable_k_fold_cv_sess_buttons: 
        """

        tk.Frame.__init__(self,
                          parent,
                          bg='light green')

        self._disable_k_fold_cv_sess_buttons = disable_k_fold_cv_sess_buttons
        self._enable_k_fold_cv_sess_buttons = enable_k_fold_cv_sess_buttons

        self._number_of_epochs_selected = False
        self._valid_data_set_selected = False
        self._train_session_selected = False
        self._first_start = True

        self._sc_scrollable = None
        self._f_output = None

        self._display_options = []

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

            disabled=False
        )

        self._train_session_output = TrainSessOutputF(
            parent=self._sc_scrollable.f_main_frame,
        )

    def _place_widgets(self):

        self._train_sess_browse.pack(side='top',
                                     fill='both',
                                     expand=True)

        self._train_sess_details_output.pack(side='top',
                                             fill='both',
                                             expand=True)

        self._session_buttons.pack(side='top',
                                   fill='x')

    #########################################################################
    # Event handling

    # ~~~~~~~~~~~~~~~~~~~~~Train session browse~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _train_session_selected_eh(
            self,

            selected_path):

        self._train_session_selected = True

        print('_train_session_selected_eh' + str(selected_path))

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Data augmentation~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _fold_number_selected_eh(
            self,

            selected_value):

        # TODO

        self._first_start = self._first_start  # To mute PyCharm warning :) *2

        print('_fold_number_selected_eh    ' + selected_value)

    # ~~~~~~~~~~~~~~~~~~~~~Data set browse~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _data_set_selected_eh(
            self,

            selected_path):

        self._valid_data_set_selected = True

        print('_data_set_selected_eh' + str(selected_path))

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Number of epochs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _number_of_epochs_selected_eh(
            self,

            number_of_epochs):

        self._number_of_epochs_selected = True

        print('_number_of_epochs_selected_eh' + str(number_of_epochs))

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Session buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _start_btn_eh(self):

        if self._first_start:
            self._first_start = False

            self._train_sess_details_output.destroy()
            self._train_sess_browse.destroy()

            self._create_and_place_output_frame_and_canvas()

            self._fold_number_input = ComboboxInputF(
                parent=self._sc_scrollable.f_main_frame,

                user_instruction=const.KFCVESG_K_TEXT,
                user_options=self._display_options,

                selection_eh=self._fold_number_selected_eh,
            )

            self._fold_number_input.config(
                pady=30
            )

            self._train_session_output = TrainSessOutputF(
                parent=self._sc_scrollable.f_main_frame,
            )

            self._test_sess_output = TestSessOutputF(
                parent=self._sc_scrollable.f_main_frame
            )

            self._test_sess_output.progress_bar.pack_forget()

            self._fold_number_input.pack(side='top',
                                         fill='both',
                                         expand=True)

            self._train_session_output.pack(side='top',
                                            fill='both',
                                            expand=True)

            self._test_sess_output.pack(side='top',
                                        fill='both',
                                        expand=True)

            # TODO -> Call the controller to start the training session.

            from utils.call_method_in_new_thread import CallMethodInNewThread

            CallMethodInNewThread.call_method(
                function_to_call=self.mock_data_set_creation,
            )

    def _pause_btn_eh(self):

        # TODO

        pass

    def _stop_btn_eh(self):

        # TODO

        pass

    def _cancel_btn_eh(self):

        # TODO

        pass

    #########################################################################
    # Auxiliary methods

    def _validate_data_set_selection(
            self,

            selected_path):

        self._first_start = self._first_start  # To mute PyCharm warning :) *3

        print(str(selected_path))

        return True

    def _check_form_validity(self):

        # TODO

        pass

    #########################################################################
    #

    #########################################################################
    # Public methods

    #########################################################################
    # Temporary methods

    def mock_data_set_creation(self):

        from random import random
        from time import sleep

        for i in range(25):

            message = TrainSessMessage()

            message.step = i
            message.loss = random() * 100
            message.seconds_per_batch = random() * 100
            message.examples_per_sec = random() * 100

            self._train_session_output.new_message(
                message=message
            )

            sleep(0.2)

    #########################################################################
