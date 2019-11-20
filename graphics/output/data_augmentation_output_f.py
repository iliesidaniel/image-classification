from graphics.widgets.checkbox_item_output_f import CheckboxItemOutputF
from utils.train.data_augmentation import DataAugmentation


import constants.output_constants as const
import tkinter as tk


class DataAugmentationOutputF(tk.Frame):

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
                          relief=const.DAO_FRAME_RELIEF,
                          padx=const.DAO_FRAME_PADX,
                          pady=const.DAO_FRAME_PADY,
                          bd=const.DAO_FRAME_BD)

        self._cio_output = []

        # Widget creation
        self._lbl_title = tk.Label(
            self,

            font=const.DAO_TITLE_FONT,
            text=const.DAO_TITLE_TEXT,

            padx=const.DAO_TITLE_PADX,
            pady=const.DAO_TITLE_PADY,
        )

        self._f_option = tk.Frame(
            self,

            relief=const.DAO_SUBFRAME_RELIEF,
            padx=const.DAO_SUBFRAME_PADX,
            pady=const.DAO_SUBFRAME_PADY,
            bd=const.DAO_SUBFRAME_BD
        )

        # Widget placement
        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_option.pack(side='top',
                            fill='both',
                            expand=True)

        # Initial output
        initial_output = DataAugmentation()

        self.update_status(initial_output)

        if disabled:
            self.disable()

    #########################################################################
    # Public methods

    def update_status(
            self,

            data_augmentation_options: DataAugmentation):
        """
        - Updates the option's state.
        
        :param data_augmentation_options: DataAugmentation list.
        """

        options_list = data_augmentation_options.get_options_list()

        for index in range(len(self._cio_output)):
            self._cio_output[index].destroy()

        self._cio_output = []

        for index in range(len(options_list)):
            self._cio_output.append(
                CheckboxItemOutputF(
                    parent=self._f_option,

                    item_text=options_list[index][0],
                    checked=options_list[index][1],
                )
            )

            self._cio_output[index].pack(side='top')

    def enable(self):
        """ Enables all the widgets."""

        for index in range(len(self._cio_output)):
            self._cio_output[index].enable()

        self._lbl_title.config(state='normal')

    def disable(self):
        """ Disables all the widgets."""

        for index in range(len(self._cio_output)):
            self._cio_output[index].disable()

        self._lbl_title.config(state='disabled')

    #########################################################################
