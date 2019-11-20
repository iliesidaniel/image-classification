from graphics.widgets.validity_indicator_f import ValidityIndicatorF

import constants.widget_constants as const
import tkinter as tk


class VerifiedInputF(tk.Frame):
    """
    - Entry with validity indicator.
    - Use to make sure the user input is correct (the validation is done by 
    the method provided to the constructor parameter named validation_method,
    if the method returns True then the valid indicator is displayed, invalid
    indicator if it returns False. 
    - After each change in the Entry either valid_input_eh or 
    invalid_input_eh will be called accordingly to the value returned by 
    validation_method.
    - All elements can be enabled or disabled, either at construction time 
    or later.
    """

    def __init__(self,

                 parent,

                 validation_method,

                 valid_input_eh,
                 invalid_input_eh,

                 form_id=None,
                 disabled=False,

                 input_entry_width=const.VIF_NBR_OF_INPUT_CHARS):
        """ 
        - Creates and places the widgets.
        - For more details check class description.
        - If you did not set the parameter form_id use check_input, if you 
        set it, use check_input_id instead.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.VIF_FRAME_PADX,
                          pady=const.VIF_FRAME_PADY)

        self._input_entry_width = input_entry_width
        self._validation_method = validation_method

        if form_id is not None and not isinstance(form_id, int):
                raise TypeError('form_if must be int')

        self._form_id = form_id
        self._valid_input_eh = valid_input_eh
        self._invalid_input_eh = invalid_input_eh

        self._create_widgets()
        self._place_widgets()

        self._input = None

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):

        _sv = tk.StringVar()
        _sv.trace("w", lambda name, index, mode,
                  sv=_sv: self._input_changed(sv))

        self._e_input = tk.Entry(
            self,

            width=self._input_entry_width,

            font=const.VIF_FONT,
            justify='center',
            textvariable=_sv
        )

        self._vi = ValidityIndicatorF(self)

    def _place_widgets(self):

        self._e_input.pack(side='left',
                           fill='both',
                           expand=True)
        self._vi.pack(side='left',
                      fill='both',
                      expand=True)

    #########################################################################
    # Event handling

    def _input_changed(
            self,
            sv: tk.StringVar):
        """
        - Automatically called when the user changes the desired file name.
        """

        self._input = sv.get()

        if self._form_id is not None:
            self.check_input_id()
        else:
            self.check_input()

    #########################################################################
    # Public methods

    def get_input(self):
        """ Returns the user input."""

        return self._input

    def check_input_id(self):
        """ 
        - Call to check if the input is still valid.
        - The input's validity is checked automatically so you don't have to 
        call this method unless you use this class in combination with 
        another input form and the validity is determined by checking all of 
        them, FileNameInputFrame is such a case.
        """

        if self._validation_method(self.get_input()):
            self._vi.valid()

            self._valid_input_eh(self._form_id)
        else:
            self._vi.invalid()

            self._invalid_input_eh(self._form_id)

    def check_input(self):
        """ 
        - Call to check if the input is still valid.
        - The input's validity is checked automatically so you don't have to 
        call this method unless you use this class in combination with 
        another input form and the validity is determined by checking all of 
        them, FileNameInputFrame is such a case.
        - Use this method if didn't set the constructor parameter form_id.
        """

        if self._validation_method(self.get_input()):
            self._vi.valid()

            self._valid_input_eh()
        else:
            self._vi.invalid()

            self._invalid_input_eh()

    def valid(self):
        """
        * IMPORTANT!!! This method overwrites the check made by the 
        validation method.
        
        - Sets the indicator to "Valid".
        - For example this is used by VerifiedInputListF.
        """

        self._vi.valid()

    def invalid(self):
        """
        * IMPORTANT!!! This method overwrites the check made by the 
        validation method.
        
        - Sets the indicator to "Invalid".
        - For example this is used by VerifiedInputListF.
        """

        self._vi.invalid()

    def enable(self):
        """ Enables all the widgets."""

        self._e_input.config(state='normal')
        self._vi.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._vi.disable()
        self._e_input.config(state='disabled')

    #########################################################################
