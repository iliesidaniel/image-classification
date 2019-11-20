from graphics.widgets.validity_indicator_f import ValidityIndicatorF

import constants.widget_constants as const
import tkinter as tk


class CheckboxItemOutputF(tk.Frame):
    """ 
    - Use to display if an entry was checked or not during input.
    """

    def __init__(self,

                 parent,

                 item_text,
                 checked,

                 disabled=False):
        """
        :param parent: Parent. 
        
        :param checked: True if the item was checked during input.
        :param item_text: Item text. 
        
        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.CIO_FRAME_PADX,
                          pady=const.CIO_FRAME_PADY)

        self._vi_checked_indicator = ValidityIndicatorF(self)

        self._lbl_item_text = tk.Label(
            self,

            font=const.CIO_FONT,
            text=item_text,
            anchor='w'
        )

        if checked:
            self.check()
        else:
            self.uncheck()

        self._vi_checked_indicator.pack(side='left',
                                        fill='x',
                                        expand=True)
        self._lbl_item_text.pack(side='right',
                                 fill='x',
                                 expand=True)

        if disabled:
            self.disable()

    #########################################################################
    # Public methods

    def check(self):
        self._vi_checked_indicator.valid()

    def uncheck(self):
        self._vi_checked_indicator.invalid()

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_item_text.config(state='normal')
        self._vi_checked_indicator.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._vi_checked_indicator.disable()
        self._lbl_item_text.config(state='disabled')

    #########################################################################
