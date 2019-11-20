from graphics.gui.test.existent_k_fold_cv_sess_gui import ExistentKFoldCVSessGUI
from graphics.gui.test.new_k_fold_cv_sess_gui import NewKFoldCVSessGUI

from graphics.widgets.kfoldcvsessbuttonsf import KFoldCVSessButtonsF

import tkinter as tk


class KFoldCVSessGUI(tk.Frame):

    def __init__(self,

                 parent,

                 enable_test_sess_buttons,
                 disable_test_sess_buttons):
        """
        :param parent: Parent.
        :param enable_test_sess_buttons: Method that enables the buttons in
                                         the parent elements.
        :param disable_test_sess_buttons: Method that disable the buttons in
                                          the parent elements.
        """

        tk.Frame.__init__(self,
                          parent)

        self._disable_test_sess_buttons = disable_test_sess_buttons
        self._enable_test_sess_buttons = enable_test_sess_buttons

        self._existent_session_gui = None
        self._new_session_gui = None

        self._create()
        self._place()

    #########################################################################
    # Creation and placement

    def _create(self):

        self._kfcv_session_switch = KFoldCVSessButtonsF(
            self,

            new_sess_eh=self._new_sess_eh,
            existent_sess_eh=self._existent_sess_eh
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

        self._kfcv_session_switch.pack(side='top',
                                       fill='x')

        self._f_output.pack(side='top',
                            fill='both',
                            expand=True)
        self._f_temporary_output.pack(side='top',
                                      fill='both',
                                      expand=True)

    def _delete_and_recreate_the_temporary_frame(self):
        """ Deletes and creates again _f_temporary_user_interaction."""

        if self._new_session_gui is not None:
            self._new_session_gui.destroy()
            del self._new_session_gui

            self._new_session_gui = None

        if self._existent_session_gui is not None:
            self._existent_session_gui.destroy()
            del self._existent_session_gui

            self._existent_session_gui = None

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

    def _new_sess_eh(self):
        """ Displays NewTrainSessGUI """

        self._delete_and_recreate_the_temporary_frame()

        self._new_session_gui = NewKFoldCVSessGUI(
            self._f_temporary_output,

            enable_k_fold_cv_sess_buttons=self.enable,
            disable_k_fold_cv_sess_buttons=self.disable
        )

        self._new_session_gui.pack(side='top',
                                   fill='both',
                                   expand=True)

    def _existent_sess_eh(self):
        """ Displays ExistentTrainSessGUI """

        self._delete_and_recreate_the_temporary_frame()

        self._existent_session_gui = ExistentKFoldCVSessGUI(
            self._f_temporary_output,

            enable_k_fold_cv_sess_buttons=self.enable,
            disable_k_fold_cv_sess_buttons=self.disable
        )

        self._existent_session_gui.pack(side='top',
                                        fill='both',
                                        expand=True)

    #########################################################################
    # Public methods

    def enable(self):
        """ Enables all the widgets."""

        self._enable_test_sess_buttons()
        self._kfcv_session_switch.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._disable_test_sess_buttons()
        self._kfcv_session_switch.disable()

    #########################################################################
