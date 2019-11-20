import constants.test_sess_constants as const
import utils.utils as utils
import tkinter as tk


class TestGuiButtonsF(tk.Frame):
    """ Test GUI buttons."""

    def __init__(self,

                 parent,

                 manual_sess_eh,
                 automated_sess_eh,
                 k_fold_cv_sess_eh):
        """ Creates and places the buttons"""

        tk.Frame.__init__(self,
                          parent,
                          padx=const.TTGB_PADX,
                          pady=const.TTGB_PADY)

        self._manual_sess_eh = manual_sess_eh
        self._automated_sess_eh = automated_sess_eh
        self._k_fold_cv_sess_eh = k_fold_cv_sess_eh

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

        self._img_manual_sess = utils.load_and_resize_image(
            const.TTGB_MANUAL_SESS_IMG_PATH,
            const.TTGB_IMG_WIDTH,
            const.TTGB_IMG_HEIGHT
        )
        self._img_automated_sess = utils.load_and_resize_image(
            const.TTGB_AUTOMATED_SESS_IMG_PATH,
            const.TTGB_IMG_WIDTH,
            const.TTGB_IMG_HEIGHT
        )
        self._img_k_fold_cv_sess = utils.load_and_resize_image(
            const.TTGB_K_FOLD_CV_SESS_IMG_PATH,
            const.TTGB_IMG_WIDTH,
            const.TTGB_IMG_HEIGHT
        )

    def _load_icons_failed(self):
        """ Called when at least one of the images was not found."""

        self._img_manual_sess = None
        self._img_automated_sess = None
        self._img_k_fold_cv_sess = None

    def _create_frames(self):
        """ Creates the frames."""

        self._f_buttons = tk.Frame(
            self,
            padx=const.TTGB_PADX,
            pady=const.TTGB_PADY
        )

        self._f_manual_sess = tk.Frame(
            self._f_buttons,
            padx=const.TTGB_BTN_FRAME_PADX,
            pady=const.TTGB_BTN_FRAME_PADY,
        )
        self._f_automated_sess = tk.Frame(
            self._f_buttons,
            padx=const.TTGB_BTN_FRAME_PADX,
            pady=const.TTGB_BTN_FRAME_PADY
        )
        self._f_k_fold_cv_sess = tk.Frame(
            self._f_buttons,
            padx=const.TTGB_BTN_FRAME_PADX,
            pady=const.TTGB_BTN_FRAME_PADY
        )

    def _create_buttons(self):
        """ Creates the buttons."""

        self._btn_manual_sess = tk.Button(
            self._f_manual_sess,

            padx=const.TTGB_BTN_PADX,
            pady=const.TTGB_BTN_PADY,

            text=const.TTGB_MANUAL_SESS_BTN,
            image=self._img_manual_sess,
            font=const.TTGB_FONT,

            command=self._local_manual_sess_eh,
            compound='left',
            bd=2
        )

        self._btn_automated_sess = tk.Button(
            self._f_automated_sess,

            padx=const.TTGB_BTN_PADX,
            pady=const.TTGB_BTN_PADY,

            text=const.TTGB_AUTOMATED_SESS_BTN,
            image=self._img_automated_sess,
            font=const.TTGB_FONT,

            command=self._local_automated_sess_eh,
            compound='left',
            bd=2
        )

        self._btn_k_fold_cv_sess = tk.Button(
            self._f_k_fold_cv_sess,

            padx=const.TTGB_BTN_PADX,
            pady=const.TTGB_BTN_PADY,

            text=const.TTGB_K_FOLD_CV_SESS_BTN,
            image=self._img_k_fold_cv_sess,
            font=const.TTGB_FONT,

            command=self._local_k_fold_cv_sess_eh,
            compound='left',
            bd=2
        )

    def _place_widgets(self):
        """ Places the widgets."""

        self._btn_manual_sess.pack(fill='both',
                                   expand=True)
        self._btn_automated_sess.pack(fill='both',
                                      expand=True)
        self._btn_k_fold_cv_sess.pack(fill='both',
                                      expand=True)

        self._f_manual_sess.pack(side='left',
                                 fill='both',
                                 expand=True)
        self._f_automated_sess.pack(side='left',
                                    fill='both',
                                    expand=True)
        self._f_k_fold_cv_sess.pack(side='left',
                                    fill='both',
                                    expand=True)

        self._f_buttons.pack(side='top',
                             fill='x',
                             expand=True)

    def _raise_buttons(self):

        self._btn_manual_sess.config(relief="raised")
        self._btn_automated_sess.config(relief="raised")
        self._btn_k_fold_cv_sess.config(relief="raised")

    #########################################################################
    # Event handling

    def _local_manual_sess_eh(self):

        self._raise_buttons()
        self._btn_manual_sess.config(relief="sunken")
        self._manual_sess_eh()

    def _local_automated_sess_eh(self):

        self._raise_buttons()
        self._btn_automated_sess.config(relief="sunken")
        self._automated_sess_eh()

    def _local_k_fold_cv_sess_eh(self):

        self._raise_buttons()
        self._btn_k_fold_cv_sess.config(relief="sunken")
        self._k_fold_cv_sess_eh()

    #########################################################################
    # Public methods

    def enable(self):
        """ Enables all the buttons."""

        self._btn_manual_sess.config(state='normal')
        self._btn_automated_sess.config(state='normal')
        self._btn_k_fold_cv_sess.config(state='normal')

    def disable(self):
        """ Disables all the buttons."""

        self._btn_manual_sess.config(state='disabled')
        self._btn_automated_sess.config(state='disabled')
        self._btn_k_fold_cv_sess.config(state='disabled')

    #########################################################################
