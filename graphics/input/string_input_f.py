from graphics.widgets.verified_input_f import VerifiedInputF

import constants.input_constants as const
import utils.utils as utils
import tkinter as tk


class StringInputF(tk.Frame):

    def __init__(self,

                 parent,

                 user_instruction: str,

                 input_changed_valid_eh,
                 input_changed_invalid_eh,

                 allow_space=False,

                 disabled=False):

        tk.Frame.__init__(self,
                          parent)

        self._input_changed_invalid_eh = input_changed_invalid_eh
        self._input_changed_valid_eh = input_changed_valid_eh
        self._allow_space = allow_space

        self._lbl_user_instruction = tk.Label(
            self,

            text=user_instruction,
            font=const.SI_FONT
        )

        self._vi_string_input = VerifiedInputF(
            parent=self,

            validation_method=self._is_string_valid,

            valid_input_eh=self._valid_input_eh,
            invalid_input_eh=self._invalid_input_eh,

            disabled=False
        )

        self._lbl_user_instruction.pack(side='left',
                                        fill='both',
                                        expand=True)
        self._vi_string_input.pack(side='right',
                                   fill='both',
                                   expand=True)

        if disabled:
            self.disable()

    #########################################################################
    # Event handling

    def _valid_input_eh(self):

        if self._input_changed_valid_eh is not None:
            self._input_changed_valid_eh()

    def _invalid_input_eh(self):

        if self._input_changed_invalid_eh is not None:
            self._input_changed_invalid_eh()

    #########################################################################
    # Validation Methods

    def _is_string_valid(
            self,

            user_input: str):
        """
        :param user_input: User input
               
         :return: - True if the string is valid
                  - False otherwise
        """

        if self._allow_space:
            allowed = const.SI_ALLOWED_CHARACTERS_SPACE
        else:
            allowed = const.SI_ALLOWED_CHARACTERS

        rez = utils.string_is_valid(
            string_to_check=user_input,
            allowed_characters=allowed
        )

        return rez

    def _get_input(self):
        """ Returns user input."""

        return self._vi_string_input.get_input()

    #########################################################################
    # Public methods

    def get_validated_input(self):
        """ Returns user input."""

        user_input = self._vi_string_input.get_input()

        if self._is_string_valid(user_input=user_input):
            rez = self._get_input()
        else:
            rez = ''

        return rez

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_user_instruction.config(state='normal')
        self._vi_string_input.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._vi_string_input.disable()
        self._lbl_user_instruction.config(state='disabled')

    #########################################################################
