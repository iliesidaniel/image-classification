from graphics.gui.test.automated_test_sess_gui import AutomatedTestSessGUI
from graphics.gui.test.manual_test_sess_gui import ManualTestSessGUI
from graphics.gui.test.k_fold_cv_sess_gui import KFoldCVSessGUI

from graphics.widgets.test_gui_buttons_f import TestGuiButtonsF

import tkinter as tk


class TestSessGUI(tk.Frame):

    def __init__(self,

                 parent,

                 enable_main_window_buttons,
                 disable_main_window_buttons):

        tk.Frame.__init__(self,
                          parent)

        self._enable_main_window_buttons = enable_main_window_buttons
        self._disable_main_window_buttons = disable_main_window_buttons

        self._automated_test_sess_gui = None
        self._manual_test_sess_gui = None
        self._k_fold_cv_sess_gui = None

        self._create()
        self._place()

    #########################################################################
    # Creation and placement
    def _create(self):

        self._tgb_session_switch = TestGuiButtonsF(
            self,

            manual_sess_eh=self._manual_test_sess_eh,
            automated_sess_eh=self._automated_test_sess_eh,
            k_fold_cv_sess_eh=self._k_fold_cv_sess_eh
        )

        self._f_output = tk.Frame(
            self,
        )

        self._f_temporary_output = tk.Frame(
            self._f_output,

            relief='sunken',

            padx=0,
            pady=0,
            bd=4
        )

    def _place(self):

        self._tgb_session_switch.pack(side='top',
                                      fill='x')

        self._f_output.pack(side='top',
                            fill='both',
                            expand=True)

        self._f_temporary_output.pack(side='top',
                                      fill='both',
                                      expand=True)

    def _delete_and_recreate_the_temporary_frame(self):
        """ Deletes and creates again _f_temporary_output."""

        if self._k_fold_cv_sess_gui is not None:
            self._k_fold_cv_sess_gui.destroy()
            del self._k_fold_cv_sess_gui

            self._k_fold_cv_sess_gui = None

        if self._automated_test_sess_gui is not None:
            self._automated_test_sess_gui.destroy()
            del self._automated_test_sess_gui

            self._automated_test_sess_gui = None

        if self._manual_test_sess_gui is not None:
            self._manual_test_sess_gui.destroy()
            del self._manual_test_sess_gui

            self._manual_test_sess_gui = None

        self._f_temporary_output.destroy()
        del self._f_temporary_output

        self._f_temporary_output = tk.Frame(
            self._f_output,

            relief='sunken',

            padx=0,
            pady=0,
            bd=4
        )

        self._f_temporary_output.pack(side='top',
                                      fill='both',
                                      expand=True)

    #########################################################################
    # Event handling

    def _manual_test_sess_eh(self):
        """ Displays ManualTestSessGUI """

        self._delete_and_recreate_the_temporary_frame()

        self._manual_test_sess_gui = ManualTestSessGUI(
            self._f_temporary_output,

            enable_test_sess_buttons=self.enable,
            disable_test_sess_buttons=self.disable
        )

        self._manual_test_sess_gui.pack(side='top',
                                        fill='both',
                                        expand=True)

    def _automated_test_sess_eh(self):
        """ Displays AutomatedTestSessGUI """

        self._delete_and_recreate_the_temporary_frame()

        self._automated_test_sess_gui = AutomatedTestSessGUI(
            self._f_temporary_output,

            enable_test_sess_buttons=self.enable,
            disable_test_sess_buttons=self.disable
        )

        self._automated_test_sess_gui.pack(side='top',
                                           fill='both',
                                           expand=True)

    def _k_fold_cv_sess_eh(self):
        """ Displays KFoldCVSessGUI """

        self._delete_and_recreate_the_temporary_frame()

        self._k_fold_cv_sess_gui = KFoldCVSessGUI(
            self._f_temporary_output,

            enable_test_sess_buttons=self.enable,
            disable_test_sess_buttons=self.disable
        )

        self._k_fold_cv_sess_gui.pack(side='top',
                                      fill='both',
                                      expand=True)

    #########################################################################
    # Public methods

    def enable(self):
        """ Enables all the widgets."""

        self._enable_main_window_buttons()
        self._tgb_session_switch.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._disable_main_window_buttons()
        self._tgb_session_switch.disable()

    #########################################################################
