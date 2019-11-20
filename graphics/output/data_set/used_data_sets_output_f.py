from graphics.output.data_set.used_data_set_output_f import UsedDataSetOutputF
from utils.data_set.used_data_sets import UsedDataSets

import constants.output_constants as const
import tkinter as tk


class UsedDataSetsOutputF(tk.Frame):
    """
    - Use to display the used data sets.
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
                          relief=const.UDSSO_FRAME_RELIEF,
                          padx=const.UDSSO_FRAME_PADX,
                          pady=const.UDSSO_FRAME_PADY,
                          bd=const.UDSSO_FRAME_BD)

        self._create_and_place_main_widgets()
        self._udso_list = []

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement.

    def _create_and_place_main_widgets(self):

        self._lbl_title = tk.Label(
            self,

            font=const.UDSSO_TITLE_FONT,
            text=const.UDSSO_TITLE_TEXT,

            padx=const.UDSSO_TITLE_PADX,
            pady=const.UDSSO_TITLE_PADY,
        )

        self._f_output = tk.Frame(
            self,

            relief=const.UDSSO_SUBFRAME_RELIEF,
            padx=const.UDSSO_SUBFRAME_PADX,
            pady=const.UDSSO_SUBFRAME_PADY,
            bd=const.UDSSO_SUBFRAME_BD
        )

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_output.pack(side='top',
                            fill='both',
                            expand=True)

    #########################################################################
    # Public methods

    def update_used_data_sets(
            self,

            used_data_sets: UsedDataSets):
        """
        - Updates the list with the used data sets.

        :param used_data_sets: UsedDataSets list.
        """

        data_sets = used_data_sets.get_used_data_sets()
        uds_number = len(data_sets)

        for index in range(uds_number):
            # Adds a new UsedDataSetOutputF to the _udso_list.
            self._udso_list.append(
                UsedDataSetOutputF(
                    parent=self._f_output,
                    data_set_index=index + 1
                )
            )

            # Updates the data set details.
            self._udso_list[index].update_save_details(
                data_set_details=data_sets[index]
            )

            # Displays the UsedDataSetOutputF
            self._udso_list[index].pack(side='top',
                                        fill='both',
                                        expand=True)

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_title.config(state='normal')

        for udso_entry in self._udso_list:
            udso_entry.enable()

    def disable(self):
        """ Disables all the widgets."""

        for udso_entry in self._udso_list:
            udso_entry.disable()

        self._lbl_title.config(state='disabled')

    #########################################################################
