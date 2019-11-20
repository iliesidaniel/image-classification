from graphics.input.train_sess_details_input_f import TrainSessDetailsInputF
from graphics.input.data_augmentation_input_f import DataAugmentationInputF
from graphics.input.file_save_details_input_f import FileSaveDetailsInputF

from graphics.output.train_sess.train_sess_output_f import TrainSessOutputF
from graphics.output.test_sess.test_sess_output_f import TestSessOutputF

from graphics.widgets.scrollable_canvas_c import ScrollableCanvasC
from graphics.widgets.session_buttons_f import SessionButtonsF
from graphics.widgets.combobox_input_f import ComboboxInputF

from utils.train.train_sess_message import TrainSessMessage


import constants.gui_constants as const
import tkinter as tk


class NewKFoldCVSessGUI(tk.Frame):

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
                          parent)

        self._disable_k_fold_cv_sess_buttons = disable_k_fold_cv_sess_buttons
        self._enable_k_fold_cv_sess_buttons = enable_k_fold_cv_sess_buttons

        self._valid_train_session_details_input = False
        self._valid_train_sess_save_details = False

        self._sc_scrollable = None
        self._f_output = None

        self._display_options = []

        self._first_start = True

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

        self._data_augmentation = DataAugmentationInputF(
            parent=self._sc_scrollable.f_main_frame,

            selection_eh=self._data_augmentation_selection_eh,

            disabled=True
        )

        self._train_session_details_input = TrainSessDetailsInputF(
            parent=self._sc_scrollable.f_main_frame,

            valid_input_eh=self._valid_session_details_eh,
            invalid_input_eh=self._invalid_session_details_eh,

            k_fold_cv_session=True,
            disabled=True
        )

        self._train_sess_save_details = FileSaveDetailsInputF(
            parent=self._sc_scrollable.f_main_frame,

            file_extension=const.NTSG_EXTENSION,

            valid_input_eh=self._valid_save_details_eh,
            invalid_input_eh=self._invalid_save_details_eh,

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

    def _place_widgets(self):

        self._sc_scrollable.pack(side='top',
                                 fill='both',
                                 expand=True)

        self._train_sess_save_details.pack(side='top',
                                           fill='both',
                                           expand=True)

        self._train_session_details_input.pack(side='top',
                                               fill='both',
                                               expand=True)

        self._data_augmentation.pack(side='top',
                                     fill='both',
                                     expand=True)

        self._session_buttons.pack(side='top',
                                   fill='both',
                                   expand=True)

    #########################################################################
    # Event handling

    # ~~~~~~~~~~~~~~~~~~~~~Data augmentation~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _data_augmentation_selection_eh(self):

        # TODO

        pass

    # ~~~~~~~~~~~~~~~~~~~~~Data augmentation~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _fold_number_selected_eh(
            self,

            selected_value):

        # TODO

        if selected_value != 'Overall':
            self._train_session_output.pack_forget()
            self._test_sess_output.pack_forget()

            self._train_session_output.pack(side='top',
                                            fill='both',
                                            expand=True)
            self._test_sess_output.pack(side='top',
                                        fill='both',
                                        expand=True)
        else:
            self._train_session_output.pack_forget()

        print('_fold_number_selected_eh    ' + selected_value)

    # ~~~~~~~~~~~~~~~~~~~~~Save details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _valid_save_details_eh(
            self,

            save_details):

        self._valid_train_sess_save_details = True

        print('_valid_save_details_eh    ' + str(save_details))

        self._check_form_validity()

    def _invalid_save_details_eh(self):

        self._valid_train_sess_save_details = False

        print('_invalid_save_details_eh')

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Session details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _valid_session_details_eh(self):

        session_details = self._train_session_details_input.get_input()
        self._valid_train_session_details_input = True
        self._display_options = ["Overall"]

        for i in range(int(session_details.number_of_folds)):
            self._display_options.append(str(i + 1))

        print('_valid_session_details_eh')

        self._check_form_validity()

    def _invalid_session_details_eh(self):

        self._valid_train_session_details_input = False

        print('_invalid_session_details_eh')

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Session buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _start_btn_eh(self):

        if self._first_start:
            self._first_start = False

            self._train_session_details_input.destroy()
            self._train_sess_save_details.destroy()
            self._data_augmentation.destroy()

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

        print(str(self._train_session_details_input.get_input()))
        print(str(self._train_sess_save_details.get_new_file_details()))
        print(str(self._data_augmentation.get_input()))

    def _stop_btn_eh(self):

        # TODO

        pass

    def _cancel_btn_eh(self):

        # TODO

        pass

    #########################################################################
    # Auxiliary methods

    def _check_form_validity(self):

        if self._valid_train_sess_save_details:
            self._train_session_details_input.enable()
            self._data_augmentation.enable()

            if self._valid_train_session_details_input:
                self._session_buttons.enable()
            else:
                self._session_buttons.disable()
                self._data_augmentation.disable()
        else:
            self._train_session_details_input.disable()
            self._data_augmentation.disable()
            self._session_buttons.disable()

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
