import constants.widget_constants as const
import tkinter as tk


class SingleLineOutputF(tk.Frame):
    """ 
    - Use to display single line output with a short description before it.
    """

    def __init__(self,

                 parent,

                 description,
                 output_text,

                 disabled=False,
                 description_width=0,
                 font=const.SLO_FONT):
        """ 
        :param parent: Parent.

        :param description: Short description about the output.
        :param output_text: Output text.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.SLO_PADX,
                          pady=const.SLO_PADY)

        self._lbl_description = tk.Label(
            self,

            width=description_width,

            font=font,
            text=description
        )

        self._lbl_output_text = tk.Label(
            self,

            font=font,
            text=output_text
        )

        self._lbl_description.pack(side='left',)
        self._lbl_output_text.pack(side='right',
                                   fill='both',
                                   expand=True)

        if disabled:
            self.disable()

    #########################################################################
    # Public methods

    def update_output(
            self,

            output_text: str):
        """
        - Updates the output text.
        
        :param output_text: Output text 
        """

        self._lbl_output_text.config(text=output_text)

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_description.config(state='normal')
        self._lbl_output_text.config(state='normal')

    def disable(self):
        """ Disables all the widgets."""

        self._lbl_description.config(state='disabled')
        self._lbl_output_text.config(state='disabled')

    #########################################################################
