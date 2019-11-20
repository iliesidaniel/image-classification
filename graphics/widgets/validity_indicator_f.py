import constants.widget_constants as const
import utils.utils as utils
import tkinter as tk


class ValidityIndicatorF(tk.Frame):
    """ 
    - Use this to display images* to let the user know if his action is 
    correct.
    
    * If at least one of the images is not found, text will be displayed 
    instead.
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
                          parent)

        self._load_images()

        self._lbl_indicator = tk.Label(
            self,

            text=self._invalid_txt,
            image=self._img_invalid,
            font=const.VI_FONT
        )

        self._lbl_indicator.image = self._img_invalid

        self._lbl_indicator.pack(side='right',
                                 fill='both',
                                 expand=True)

        if disabled:
            self.disable()

    #########################################################################
    # Image handling

    def _load_images(self):
        """ 
        - Loads the images associated with a valid/invalid action.
        - If the images are found they will be loaded, resized and the text 
        objects will be set to ''. Otherwise self._img_invalid and 
        self._img_valid are set to None, self._valid_txt and
        self._invalid_txt to the values set in the const file.
        """

        try:
            self._img_valid = utils.load_and_resize_image(
                image_path_file_name=const.VI_VALID_IMG_PATH,
                height=const.VI_IMG_SIZE,
                width=const.VI_IMG_SIZE
            )

            self._img_invalid = utils.load_and_resize_image(
                image_path_file_name=const.VI_INVALID_IMG_PATH,
                height=const.VI_IMG_SIZE,
                width=const.VI_IMG_SIZE
            )

            self._valid_txt = ''
            self._invalid_txt = ''
        except FileNotFoundError:
            self._failed_to_load_images()

    def _failed_to_load_images(self):
        """ Called when at least one of the images is not found."""

        self._invalid_txt = const.VI_INVALID_TEXT
        self._valid_txt = const.VI_VALID_TEXT

        self._img_invalid = None
        self._img_valid = None

    #########################################################################
    # Public methods

    def valid(self):
        """ Call to display the image associated with a valid action."""

        self._lbl_indicator.config(
            text=self._valid_txt,
            image=self._img_valid
        )

        self._lbl_indicator.image = self._img_valid

    def invalid(self):
        """ Call to display the image associated with an invalid action."""

        self._lbl_indicator.config(
            text=self._invalid_txt,
            image=self._img_invalid
        )

        self._lbl_indicator.image = self._img_invalid

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_indicator.config(state='normal')

    def disable(self):
        """ Disables all the widgets."""

        self._lbl_indicator.config(state='disabled')

    #########################################################################
