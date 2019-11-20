import constants.global_constants as g_const
import constants.widget_constants as const
import tkinter as tk

from tkinter import ttk


class ComboboxInputF(tk.Frame):
    """ Use to let the user choose from a list of options."""

    def __init__(self,

                 parent,

                 user_instruction: str,
                 user_options: [],

                 selection_eh,

                 disabled=False):
        """
        :param parent: Parent.
        
        :param user_instruction: A short message to let the user know what
                                 he has to do.
        :param user_options: A list with the options to display.
        
        :param selection_eh: A method that will be called when the user 
                             selects an entry.
        
        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.CI_FRAME_PADX,
                          pady=const.CI_FRAME_PADY)

        self._selection_eh = selection_eh

        self._lbl_instruction = tk.Label(
            self,

            text=user_instruction,
            font=const.CI_FONT,

            width=g_const.INPUT_WIDGET_LABEL_WIDTH
        )
        self._cb_user_input = tk.ttk.Combobox(
            self,

            values=user_options,
            font=const.CI_FONT,
            state='readonly'
        )

        self._lbl_instruction.pack(side='left',
                                   fill='both',
                                   expand=True)
        self._cb_user_input.pack(side='left',
                                 fill='x',
                                 expand=True)

        self._cb_user_input.bind('<<ComboboxSelected>>', self._combobox_eh)

        if disabled:
            self.disable()

    #########################################################################
    # Event handling

    def _combobox_eh(self, _):
        """ Called when the user selected a combobox entry."""

        selection_text = self._cb_user_input.get()

        self._cb_user_input.selection_clear()

        self._selection_eh(selection_text)

    #########################################################################
    # Public methods

    def get_input(self):
        """ Returns the selected value."""

        return self._cb_user_input.get()

    def clear(self):

        self._cb_user_input.selection_clear()
        self._cb_user_input.set('')

    def update_options(
            self,

            new_options: []):
        """ Updates the options."""

        self.clear()

        self._cb_user_input.config(
            values=new_options
        )

    def enable(self):
        """ Enables all the buttons."""

        self._lbl_instruction.config(state='normal')
        self._cb_user_input.config(state='readonly')

    def disable(self):
        """ Disables all the buttons."""

        self._cb_user_input.config(state='disabled')
        self._lbl_instruction.config(state='disabled')

    #########################################################################
