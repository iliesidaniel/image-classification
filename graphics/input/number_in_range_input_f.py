import constants.global_constants as g_const
import constants.input_constants as const
import tkinter as tk


class NumberInRangeInputF(tk.Frame):
    """ 
    - Use to get a number that belongs to a certain interval (int or float) 
    from the user.
    """

    def __init__(self,
                 parent,

                 user_instruction: str,

                 value_changed_eh,

                 min_val,
                 max_val,
                 increment=1,

                 integer=True,

                 disabled=False):
        """
        :param parent: Parent.
        
        :param user_instruction: A short message to let the user know what
                                 he has to do.
                                 
        :param value_changed_eh: Method that will be called when the input is 
                                 changed.
                                 
        :param min_val: Minimum value. 
        :param max_val: Maximum value. 
                               
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

            text=user_instruction,
            font=const.NINRI_FONT,

            width=g_const.INPUT_WIDGET_LABEL_WIDTH
        )

        self._integer = integer

        if integer:
            value = tk.IntVar()

            self._f_number_input = tk.Spinbox(
                self,

                increment=increment,
                from_=min_val,
                to=max_val,

                command=value_changed_eh,
                font=const.NINRI_FONT,
                textvariable=value,
                state='readonly'
            )
        else:
            value = tk.DoubleVar()

            self._f_number_input = tk.Spinbox(
                self,

                increment=increment,
                from_=min_val,
                to=max_val,

                command=value_changed_eh,
                font=const.NINRI_FONT,
                textvariable=value,
                state='readonly'
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

        if self._integer:
            return int(self._f_number_input.get())
        else:
            return float(self._f_number_input.get())

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_user_instruction.config(state='normal')
        self._f_number_input.config(state='readonly')

    def disable(self):
        """ Disables all the widgets."""

        self._f_number_input.config(state='disabled')
        self._lbl_user_instruction.config(state='disabled')

    #########################################################################
