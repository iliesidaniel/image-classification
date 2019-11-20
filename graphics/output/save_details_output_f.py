from graphics.widgets.single_line_output_f import SingleLineOutputF
from graphics.widgets.multiline_output_f import MultilineOutputF

import constants.output_constants as const
import tkinter as tk


class SaveDetailsOutputF(tk.Frame):
    """
    - Use to display save details (name and description).
    """

    def __init__(self,

                 parent,

                 disabled=False):
        """
        :param parent: Parent.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          relief=const.SD_FRAME_RELIEF,
                          padx=const.SD_FRAME_PADX,
                          pady=const.SD_FRAME_PADY,
                          bd=const.SD_FRAME_BD)

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        self._lbl_title = tk.Label(
            self,

            font=const.SD_TITLE_FONT,
            text=const.SD_TITLE_TEXT,

            padx=const.SD_TITLE_PADX,
            pady=const.SD_TITLE_PADY,
        )

        self._f_subtitle = tk.Frame(
            self,

            relief=const.SD_SUBFRAME_RELIEF,
            padx=const.SD_SUBFRAME_PADX,
            pady=const.SD_SUBFRAME_PADY,
            bd=const.SD_SUBFRAME_BD
        )

        self._slo_name = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,
            font=const.SD_FONT,

            description=const.SD_NAME_TEXT,
            output_text=const.SD_INITIAL_NAME_TEXT
        )

        self._mo_description = MultilineOutputF(
            parent=self._f_subtitle,

            user_instruction=const.SD_DESCRIPTION_TEXT,
        )

    def _place_widgets(self):

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_subtitle.pack(side='top',
                              fill='both',
                              expand=True)

        self._slo_name.pack(side='top',
                            fill='both',
                            expand=True)

        self._mo_description.pack(side='top',
                                  fill='both',
                                  expand=True)

    #########################################################################
    # Public methods

    def create_and_place_elements(self):
        """
        - Creates and places the widgets.
        """

        self._create_widgets()
        self._place_widgets()

    def update_output_text(
            self,

            name: str,
            description: str):
        """
        - Updates the name and the description.

        :param name: Name. 
        :param description: Description text.
        """

        self._slo_name.update_output(name)

        self._mo_description.set_output_text(
            output_text=description
        )

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_title.config(state='normal')
        self._mo_description.enable()
        self._slo_name.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._slo_name.disable()
        self._mo_description.disable()
        self._lbl_title.config(state='disabled')

    #########################################################################
