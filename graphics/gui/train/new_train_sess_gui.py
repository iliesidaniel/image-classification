from graphics.output.train_sess.train_sess_output_f import TrainSessOutputF
from graphics.input.train_sess_details_input_f import TrainSessDetailsInputF
from graphics.input.data_augmentation_input_f import DataAugmentationInputF
from graphics.input.file_save_details_input_f import FileSaveDetailsInputF
from graphics.widgets.scrollable_canvas_c import ScrollableCanvasC
from graphics.widgets.session_buttons_f import SessionButtonsF

from utils.call_method_in_new_thread import CallMethodInNewThread

from controllers.session_controller import SessionController

from session.train_session import TrainSession

from tkinter import messagebox


import constants.gui_constants as gui_const
import tkinter as tk


class NewTrainSessGUI(tk.Frame):

    def __init__(self,

                 parent,

                 enable_train_sess_buttons,
                 disable_train_sess_buttons):

        tk.Frame.__init__(self,
                          parent)

        self._enable_train_sess_buttons = enable_train_sess_buttons
        self._disable_train_sess_buttons = disable_train_sess_buttons

        self._valid_train_session_details_input = False
        self._valid_train_sess_save_details = False

        self._first_start = True

        self._train_session = None

        self._create_widgets()
        self._place_widgets()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):
        self._sc_scrollable = ScrollableCanvasC(
            parent=self,
        )

        self._train_sess_save_details = FileSaveDetailsInputF(
            parent=self._sc_scrollable.f_main_frame,

            file_extension=gui_const.NTSG_EXTENSION,

            valid_input_eh=self._valid_save_details_eh,
            invalid_input_eh=self._invalid_save_details_eh,

            disabled=False
        )

        self._train_session_details_input = TrainSessDetailsInputF(
            parent=self._sc_scrollable.f_main_frame,

            valid_input_eh=self._valid_session_details_eh,
            invalid_input_eh=self._invalid_session_details_eh,

            disabled=True
        )

        self._data_augmentation = DataAugmentationInputF(
            parent=self._sc_scrollable.f_main_frame,

            selection_eh=self._data_augmentation_selection_eh,

            disabled=True
        )

        self._session_buttons = SessionButtonsF(
            parent=self._sc_scrollable.f_main_frame,

            start_eh=self._start_btn_eh,
            pause_eh=self._pause_btn_eh,
            stop_eh=self._stop_btn_eh,
            cancel_eh=self._cancel_btn_eh,

            disabled=True
        )

        self._train_session_output = TrainSessOutputF(
            parent=self._sc_scrollable.f_main_frame,
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

        pass

    # ~~~~~~~~~~~~~~~~~~~~~Save details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _valid_save_details_eh(
            self,

            _):

        self._valid_train_sess_save_details = True

        self._check_form_validity()

    def _invalid_save_details_eh(self):

        self._valid_train_sess_save_details = False

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Session details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _valid_session_details_eh(self):

        self._valid_train_session_details_input = True

        self._check_form_validity()

    def _invalid_session_details_eh(self):

        self._valid_train_session_details_input = False

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Session buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _start_btn_eh(self):

        if self._first_start:
            self._first_start = False

            session_details = self._train_session_details_input.get_input()
            session_file_details = self._train_sess_save_details.get_new_file_details()

            session_details.data_augmentation = self._data_augmentation.get_input()

            self._session_details, data_set_details = SessionController.process_and_save_the_input_for_a_new_session(
                session_file_details=session_file_details,
                session_details=session_details
            )

            self._train_session_details_input.destroy()
            self._train_sess_save_details.destroy()
            self._data_augmentation.destroy()

            self._train_session_output.pack(side='top',
                                            fill='both',
                                            expand=True)

            self._train_session = TrainSession(
                add_message_method=self._train_session_output.new_message,
                training_finished=self.training_ended,
                data_set_details=data_set_details,
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

    def _check_form_validity(self):

        if self._valid_train_sess_save_details:
            self._train_session_details_input.enable()
            self._data_augmentation.enable()

            if self._valid_train_session_details_input:
                self._session_buttons.enable()
                self._data_augmentation.enable()
            else:
                self._session_buttons.disable()
                self._data_augmentation.disable()
        else:
            self._train_session_details_input.disable()
            self._data_augmentation.disable()
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
