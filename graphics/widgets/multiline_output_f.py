import constants.widget_constants as const
import tkinter as tk


class MultilineOutputF(tk.Frame):
    """ 
    - Use to display output on multiple lines with a short description 
    before it.
    """

    def __init__(self,

                 parent,

                 user_instruction,

                 disabled=False):
        """ 
        :param parent: Parent.

        :param user_instruction: Short description about the output.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.MLO_PADX,
                          pady=const.MLO_PADY)

        self._text_disabled = tk.Label()['disabledforeground']
        self._text_enable = tk.Label()['foreground']
        self._background = tk.Frame()['background']

        self._user_instruction = user_instruction
        self._output_text = ''

        self._create_widgets()
        self._place_widgets()

        self.set_output_text('')

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):

        self._lbl_instruction = tk.Label(
            self,

            width=28,
            font=const.MLO_FONT,
            text=self._user_instruction
        )

        self._f_output = tk.Frame(self)

        self._txt_user_output = tk.Text(
            self._f_output,

            padx=const.MLO_WIDGET_PADX / 2,
            pady=const.MLO_WIDGET_PADY / 2,

            bg=self._background,
            font=const.MLO_FONT,
            wrap='word',
            height=5,
            bd=1
        )

        self._sb_v_scroll = tk.Scrollbar(
            self._f_output,

            orient=tk.VERTICAL,
            command=self._txt_user_output.yview
        )

        self._txt_user_output.configure(
            yscrollcommand=self._sb_v_scroll.set)

    def _place_widgets(self):

        self._lbl_instruction.pack(side='left')

        self._sb_v_scroll.pack(side='right',
                               fill='y',
                               expand=False)

        self._txt_user_output.pack(side='left',
                                   fill='both',
                                   expand=True)

        self._f_output.pack(side='right',
                            fill='both',
                            expand=True)

    #########################################################################
    # Public methods

    def set_output_text(
            self,

            output_text: str):
        """
        - Updates the text.

        :param output_text: Output text.
        """

        self._output_text = output_text

        self._txt_user_output.config(state='normal')
        self._txt_user_output.delete(1.0, 'end')
        self._txt_user_output.insert('end', self._output_text)
        self._txt_user_output.config(state='disabled')

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_instruction.config(state='normal')

        self._txt_user_output.tag_add('text',
                                      '1.0',
                                      'end')
        self._txt_user_output.tag_config('text',
                                         foreground=self._text_enable)

    def disable(self):
        """ Disables all the widgets."""

        self._lbl_instruction.config(state='disabled')

        self._txt_user_output.tag_add('text',
                                      '1.0',
                                      'end')
        self._txt_user_output.tag_config('text',
                                         foreground=self._text_disabled)

    #########################################################################
