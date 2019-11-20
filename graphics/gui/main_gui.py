from graphics.gui.data_set.create_data_set_gui import CreateDataSetGUI
from graphics.widgets.main_gui_buttons_f import MainGuiButtonsF
from graphics.gui.train.train_sess_gui import TrainSessGUI
from graphics.gui.test.test_sess_gui import TestSessGUI

from controllers.data_set_controller import DataSetController


import constants.main_window_constants as const
import tkinter as tk


class MainGUI(tk.Frame):
    """ Main GUI"""

    def __init__(self,
                 parent,
                 exit_method):
        """ Calls self.pack(), to create and draw the inner widgets call
        run() method.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.MW_WINDOW_PADX,
                          pady=const.MW_WINDOW_PADY,
                          relief='ridge',
                          bd=8)

        self._create_gui = None
        self._train_gui = None
        self._test_gui = None
        self._interact_gui = None

        self._exit_method = exit_method

        self.pack(fill='both', expand=1)

    #########################################################################
    # Widget creation and placement

    def run(self):
        """ Creates and places all the required elements."""

        self._create_frames()
        self._place_frames()

    def _create_frames(self):
        """ Creates the frames."""

        self._f_buttons = MainGuiButtonsF(
            parent=self,

            info_eh=self.info_eh,
            create_data_set_eh=self._create_data_set_gui,
            train_eh=self._add_train_gui,
            test_eh=self._add_test_gui,
            help_eh=self.help_eh,
            exit_eh=self._exit_command,
        )

        self._f_user_interaction = tk.Frame(
            self,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY)

        self._f_temporary_container = tk.Frame(
            self._f_user_interaction,
            padx=0,
            pady=0)

    def _place_frames(self):
        """ Places the widgets."""

        self._f_buttons.pack(side='top', fill='x')
        self._f_user_interaction.pack(side='bottom', fill='both', expand=1)
        self._f_temporary_container.pack(side='top', fill='both', expand=1)

    def _delete_and_recreate_the_temporary_frame(self):
        """ Deletes and creates again _f_temporary_user_interaction."""

        self._f_temporary_container.pack_forget()
        del self._f_temporary_container

        self._f_temporary_container = tk.Frame(
            self._f_user_interaction,
            relief='sunken',
            bd=4,
            padx=0,
            pady=0)

    #########################################################################
    # Event handlers

    def info_eh(self):
        """ Adds TrainGUI"""
        main_file_path = '/home/senna/temp2537490563548906807645/first_data_set.txt'

        data_set_details = DataSetController.read_main_data_set_file(
            file_path=main_file_path
        )

        DataSetController.read_data_set_files_without_image_resize(
            data_set_details=data_set_details,
            desired_image_size=24
        )

        print('############################################################')
        print('############################################################')
        print(str(data_set_details))
        print('**==**==**==**==**==**==**==****==**==**==**==**==**==**==**')
        print('**==**==**==**==**==**==**==****==**==**==**==**==**==**==**')
        print('############################################################')
        print('############################################################')

    def help_eh(self):

        # TODO

        pass

    #########################################################################
    # Launchers for create data set, training, testing and interact GUIs.

    def _create_data_set_gui(self):
        """ Adds CreateDataSetGUI"""

        self._train_gui = None
        self._test_gui = None
        self._interact_gui = None

        self._delete_and_recreate_the_temporary_frame()

        self._create_gui = CreateDataSetGUI(
            self._f_temporary_container,

            enable_main_window_buttons=self._f_buttons.enable,
            disable_main_window_buttons=self._f_buttons.disable
        )

        self._create_gui.pack(
            side='top', fill='both', expand=1)
        self._f_temporary_container.pack(
            side='top', fill='both', expand=1)

    def _add_train_gui(self):
        """ Adds TrainGUI"""

        self._create_gui = None
        self._test_gui = None
        self._interact_gui = None

        self._delete_and_recreate_the_temporary_frame()

        self._train_gui = TrainSessGUI(
            parent=self._f_temporary_container,

            enable_main_window_buttons=self._f_buttons.enable,
            disable_main_window_buttons=self._f_buttons.disable
        )

        self._train_gui.pack(side='top', fill='both', expand=1)
        self._f_temporary_container.pack(side='top', fill='both', expand=1)

    def _add_test_gui(self):
        """ Adds TestGUI"""

        self._create_gui = None
        self._train_gui = None
        self._interact_gui = None

        self._delete_and_recreate_the_temporary_frame()

        self._test_gui = TestSessGUI(
            parent=self._f_temporary_container,

            enable_main_window_buttons=self._f_buttons.enable,
            disable_main_window_buttons=self._f_buttons.disable
        )

        self._test_gui.pack(
            side='top', fill='both', expand=1)
        self._f_temporary_container.pack(
            side='top', fill='both', expand=1)

    def _exit_command(self):
        self.on_closing()
        self._exit_method()

    #########################################################################
    # Public methods

    def on_closing(self):
        """ Call this method on parent closing."""

        if self._create_gui is not None:
            pass
            # self._create_gui.on_closing()

        if self._train_gui is not None:
            pass
            # self._train_gui.on_closing()

        if self._test_gui is not None:
            pass
            # self._test_gui.on_closing()

        if self._interact_gui is not None:
            pass
            # self._interact_gui.on_closing()

    #########################################################################
