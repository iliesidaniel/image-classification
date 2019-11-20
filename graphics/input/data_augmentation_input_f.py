from utils.train.data_augmentation import DataAugmentation

import constants.train_sess_constants as const
import tkinter as tk


class DataAugmentationInputF(tk.Frame):
    """ Use to get user input regarding data augmentation."""

    def __init__(self,
                 parent,

                 selection_eh,

                 disabled=False):
        """
        :param parent: Parent.

        :param selection_eh: Method that will be called when the input is 
                             changed.

        :param disabled:    - Default: False;
                            - If True all widgets will have their state set
                              to "disabled".
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.DA_FRAME_PADX,
                          pady=const.DA_FRAME_PADY)

        self._data_augmentation = DataAugmentation()

        self._brightness_variable = tk.BooleanVar()
        self._contrast_variable = tk.BooleanVar()
        self._flip_variable = tk.BooleanVar()
        self._crop_variable = tk.BooleanVar()

        self._selection_eh = selection_eh

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):
        """ Creates the widgets."""

        self._f_options = tk.Frame(
            self,

            padx=const.DA_MODIFIERS_PADX,
            pady=const.DA_MODIFIERS_PADY
        )

        self._lbl_info = tk.Label(
            self,

            text=const.DA_USER_INFO,
            font=const.DA_FONT
        )

        self._cb_crop = tk.Checkbutton(
            self._f_options,

            text=const.DA_CROP_TEXT,
            font=const.DA_FONT,

            command=self._option_selected,
            variable=self._crop_variable,
            offvalue=False,
            onvalue=True,

            state='disabled'    # TODO
        )

        self._cb_flip_lr = tk.Checkbutton(
            self._f_options,

            text=const.DA_FLIP_LR_TEXT,
            font=const.DA_FONT,

            command=self._option_selected,
            variable=self._flip_variable,
            offvalue=False,
            onvalue=True
        )

        self._cb_brightness = tk.Checkbutton(
            self._f_options,

            text=const.DA_BRIGHTNESS_TEXT,
            font=const.DA_FONT,

            command=self._option_selected,
            variable=self._brightness_variable,
            offvalue=False,
            onvalue=True,

            state='disabled'    # TODO
        )

        self._cb_contrast = tk.Checkbutton(
            self._f_options,

            text=const.DA_CONTRAST_TEXT,
            font=const.DA_FONT,

            command=self._option_selected,
            variable=self._contrast_variable,
            offvalue=False,
            onvalue=True
        )

    def _place_widgets(self):
        """ Places the widgets."""

        self._lbl_info.pack(side='top',
                            fill='both',
                            expand=True)

        self._cb_crop.pack(side='top',
                           fill='both',
                           expand=True)
        self._cb_flip_lr.pack(side='top',
                              fill='both',
                              expand=True)
        self._cb_brightness.pack(side='top',
                                 fill='both',
                                 expand=True)
        self._cb_contrast.pack(side='top',
                               fill='both',
                               expand=True)

        self._f_options.pack(side='left',
                             fill='both',
                             expand=True)

    #########################################################################
    # Event handling

    def _option_selected(self):
        """ Automatically called when one of the check buttons used for
        random distortions is pressed.
        """

        self._data_augmentation.crop = self._crop_variable.get()
        self._data_augmentation.contrast = self._contrast_variable.get()
        self._data_augmentation.flip_left_right = self._flip_variable.get()
        self._data_augmentation.brightness = self._brightness_variable.get()

        self._selection_eh()

    #########################################################################
    # Public methods

    def get_input(self):
        """ Returns user input."""

        return self._data_augmentation

    def enable(self):
        """ Enables all the widgets."""

        # self._cb_brightness.config(state='normal')    TODO
        self._cb_contrast.config(state='normal')
        self._cb_flip_lr.config(state='normal')
        self._lbl_info.config(state='normal')
        # self._cb_crop.config(state='normal')          TODO

    def disable(self):
        """ Disables all the widgets."""

        self._cb_crop.config(state='disabled')
        self._lbl_info.config(state='disabled')
        self._cb_flip_lr.config(state='disabled')
        self._cb_contrast.config(state='disabled')
        self._cb_brightness.config(state='disabled')

    #########################################################################
