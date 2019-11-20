from graphics.widgets.verified_input_f import VerifiedInputF

import constants.input_constants as const
import utils.utils as utils
import tkinter as tk


class NumberInputF(tk.Frame):
    """ 
    - Use to get a number (int or float) from the user.
    """

    def __init__(self,

                 parent,

                 user_instruction: str,

                 valid_input_eh,
                 invalid_input_eh,

                 integer=True,

                 disabled=False):
        """
        :param parent: Parent.
        
        :param user_instruction: A short message to let the user know what
                                 he has to do.
                                 
        :param valid_input_eh: Method that will be called when the input is 
                               valid.
        :param invalid_input_eh: Method that will be called when the input is 
                                 invalid.
                               
        :param integer:     - Default: True;
                            - True for int input;
                            - False for float input.
                            
        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.NINRI_FRAME_PADX,
                          pady=const.NINRI_FRAME_PADY)

        self._lbl_user_instruction = tk.Label(
            self,

            font=const.NINRI_FONT,
            text=user_instruction
        )

        if integer:
            self._f_number_input = VerifiedInputF(
                parent=self,

                validation_method=utils.is_int,

                valid_input_eh=valid_input_eh,
                invalid_input_eh=invalid_input_eh
            )
        else:
            self._f_number_input = VerifiedInputF(
                parent=self,

                validation_method=utils.is_float,

                valid_input_eh=valid_input_eh,
                invalid_input_eh=invalid_input_eh
            )

        self._lbl_user_instruction.pack(side='left',
                                        fill='both',
                                        expand=True)

        self._f_number_input.pack(side='right',
                                  fill='both',
                                  expand=True)

        if disabled:
            self.disable()

    #########################################################################
    # Public methods

    def get_number(self):
        """ Returns the user input."""

        return self._f_number_input.get_input()

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_user_instruction.config(state='normal')
        self._f_number_input.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._f_number_input.disable()
        self._lbl_user_instruction.config(state='disabled')
