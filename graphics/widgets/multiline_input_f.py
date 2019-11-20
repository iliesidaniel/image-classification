import constants.widget_constants as const
import tkinter as tk


class MultilineInputF(tk.Frame):
    """ 
    - Use to get user input as text.
    - NOTE There is no event handling to let you know when the user changes
      the input.
    """

    def __init__(self,

                 parent,

                 user_instruction,
                 input_changed_eh,

                 disabled=False):
        """ Creates and places the widgets."""

        tk.Frame.__init__(self,
                          parent,
                          padx=const.MI_FRAME_PADX,
                          pady=const.MI_FRAME_PADY)

        self._user_instruction = user_instruction
        self._input_changed_eh = input_changed_eh

        self._create_frames()
        self._place_frames()

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_frames(self):

        self._f_input = tk.Frame(self)

        self._lbl_instruction = tk.Label(
            self,

            font=const.MI_FONT,
            text=self._user_instruction
        )

        self._txt_user_input = tk.Text(
            self._f_input,

            font=const.MI_FONT,
            wrap='word',

            height=5,
            padx=22,
            pady=12,
        )

        self._txt_user_input.bind('<<Modified>>', self._input_changed)

        self._sb_v_scroll = tk.Scrollbar(
            self._f_input,

            orient=tk.VERTICAL,
            command=self._txt_user_input.yview
        )

        self._txt_user_input.configure(
            yscrollcommand=self._sb_v_scroll.set)

    def _place_frames(self):

        self._lbl_instruction.pack(side='left',
                                   fill='both',
                                   expand=True)

        self._sb_v_scroll.pack(side='right',
                               fill='y',
                               expand=False)
        self._txt_user_input.pack(side='left',
                                  fill='both',
                                  expand=True)

        self._f_input.pack(side='right',
                           fill='both',
                           expand=True)

    #########################################################################
    # Event handling

    def _input_changed(
            self,

            _):
        """
        - Automatically called when the user changes the desired file name.
        """

        flag = self._txt_user_input.edit_modified()

        if flag:
            self._input_changed_eh(self.get_input())

        self._txt_user_input.edit_modified(False)

    #########################################################################
    # Public methods

    def get_input(self):
        """ Returns the user input."""

        return self._txt_user_input.get("1.0", "end-1c")

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_instruction.config(state='normal')
        self._txt_user_input.config(state='normal')

    def disable(self):
        """ Disables all the widgets."""

        self._txt_user_input.config(state='disabled')
        self._lbl_instruction.config(state='disabled')

    #########################################################################
