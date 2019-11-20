import constants.gui_constants as const
import utils.utils as utils
import tkinter as tk


class KFoldCVSessButtonsF(tk.Frame):
    """ K-fold cross validation GUI buttons."""

    def __init__(self,

                 parent,

                 new_sess_eh,
                 existent_sess_eh):
        """ Creates and places the buttons"""

        tk.Frame.__init__(self,
                          parent,
                          padx=const.KFCVGB_PADX,
                          pady=const.KFCVGB_PADY)

        self._new_sess_eh = new_sess_eh
        self._existent_sess_eh = existent_sess_eh

        try:
            self._load_icons()
        except FileNotFoundError:
            self._load_icons_failed()

        self._create_frames()
        self._create_buttons()
        self._place_widgets()

    #########################################################################
    # Widget creation and placement

    def _load_icons(self):
        """ Loads the images that will be displayed in the buttons."""

        self._img_existent_sess = utils.load_and_resize_image(
            const.KFCVGB_EXISTENT_SESS_IMG_PATH,
            const.KFCVGB_IMG_WIDTH,
            const.KFCVGB_IMG_HEIGHT
        )
        self._img_new_sess = utils.load_and_resize_image(
            const.KFCVGB_NEW_SESS_IMG_PATH,
            const.KFCVGB_IMG_WIDTH,
            const.KFCVGB_IMG_HEIGHT
        )

    def _load_icons_failed(self):
        """ Called when at least one of the images was not found."""

        self._img_existent_sess = None
        self._img_new_sess = None

    def _create_frames(self):
        """ Creates the frames."""

        self._f_buttons = tk.Frame(
            self,
            padx=const.KFCVGB_PADX,
            pady=const.KFCVGB_PADY
        )
        self._f_new_sess = tk.Frame(
            self._f_buttons,
            padx=const.KFCVGB_BTN_FRAME_PADX,
            pady=const.KFCVGB_BTN_FRAME_PADY
        )
        self._f_existent_sess = tk.Frame(
            self._f_buttons,
            padx=const.KFCVGB_BTN_FRAME_PADX,
            pady=const.KFCVGB_BTN_FRAME_PADY
        )

    def _create_buttons(self):
        """ Creates the buttons."""

        self._btn_new_sess = tk.Button(
            self._f_new_sess,
            command=self._local_new_sess_eh,
            text=const.KFCVGB_NEW_SESS_BTN,
            padx=const.KFCVGB_BTN_PADX,
            pady=const.KFCVGB_BTN_PADY,
            image=self._img_new_sess,
            font=const.KFCVGB_FONT,
            compound='left',
            bd=2
        )

        self._btn_existent_sess = tk.Button(
            self._f_existent_sess,
            command=self._local_existent_sess_eh,
            text=const.KFCVGB_EXISTENT_SESS_BTN,
            padx=const.KFCVGB_BTN_PADX,
            pady=const.KFCVGB_BTN_PADY,
            image=self._img_existent_sess,
            font=const.KFCVGB_FONT,
            compound='left',
            bd=2
        )

    def _place_widgets(self):
        """ Places the widgets."""

        self._btn_new_sess.pack(fill='both',
                                expand=True)
        self._btn_existent_sess.pack(fill='both',
                                     expand=True)

        self._f_new_sess.pack(side='left',
                              fill='both',
                              expand=True)
        self._f_existent_sess.pack(side='left',
                                   fill='both',
                                   expand=True)

        self._f_buttons.pack(side='top',
                             fill='x',
                             expand=True)

    #########################################################################
    # Event handling

    def _raise_buttons(self):

        self._btn_existent_sess.config(relief="raised")
        self._btn_new_sess.config(relief="raised")

    def _local_existent_sess_eh(self):

        self._raise_buttons()
        self._btn_existent_sess.config(relief="sunken")
        self._existent_sess_eh()

    def _local_new_sess_eh(self):

        self._raise_buttons()
        self._btn_new_sess.config(relief="sunken")
        self._new_sess_eh()

    #########################################################################
    # Public methods

    def enable(self):
        """ Enables all the buttons."""

        self._btn_existent_sess.config(state='normal')
        self._btn_new_sess.config(state='normal')

    def disable(self):
        """ Disables all the buttons."""

        self._btn_new_sess.config(state='disabled')
        self._btn_existent_sess.config(state='disabled')

    #########################################################################
