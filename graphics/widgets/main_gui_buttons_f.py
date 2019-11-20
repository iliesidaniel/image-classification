import constants.main_window_constants as const
import utils.utils as utils
import tkinter as tk


class MainGuiButtonsF(tk.Frame):
    """ Main GUI buttons."""

    def __init__(self,

                 parent,

                 info_eh,
                 create_data_set_eh,
                 train_eh,
                 test_eh,
                 help_eh,
                 exit_eh):
        """ Creates and places the buttons"""

        tk.Frame.__init__(self,
                          parent,
                          padx=const.MGB_PADX,
                          pady=const.MGB_PADY)

        self._create_data_set_eh = create_data_set_eh
        self._train_eh = train_eh
        self._info_eh = info_eh
        self._test_eh = test_eh
        self._help_eh = help_eh
        self._exit_eh = exit_eh

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

        self._img_info = utils.load_and_resize_image(
            const.MGB_BTN_INFO_IMG_PATH,
            const.MW_IMG_WIDTH,
            const.MW_IMG_HEIGHT
        )
        self._img_data_set = utils.load_and_resize_image(
            const.MGB_BTN_CREATE_IMG_PATH,
            const.MW_IMG_WIDTH,
            const.MW_IMG_HEIGHT
        )
        self._img_train_sess = utils.load_and_resize_image(
            const.MGB_BTN_TRAIN_IMG_PATH,
            const.MW_IMG_WIDTH,
            const.MW_IMG_HEIGHT
        )
        self._img_test_sess = utils.load_and_resize_image(
            const.MGB_BTN_TEST_IMG_PATH,
            const.MW_IMG_WIDTH,
            const.MW_IMG_HEIGHT
        )
        self._img_help = utils.load_and_resize_image(
            const.MGB_BTN_HELP_IMG_PATH,
            const.MW_IMG_WIDTH,
            const.MW_IMG_HEIGHT
        )
        self._exit_image = utils.load_and_resize_image(
            const.MGB_BTN_EXIT_IMG_PATH,
            const.MW_IMG_WIDTH,
            const.MW_IMG_HEIGHT
        )

    def _load_icons_failed(self):
        """ Called when at least one of the images was not found."""

        self._img_data_set = None
        self._img_train_sess = None
        self._img_test_sess = None
        self._exit_image = None
        self._img_help = None
        self._img_info = None

    def _create_frames(self):
        """ Creates the frames."""

        self._f_buttons = tk.Frame(
            self,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY
        )

        self._f_info = tk.Frame(
            self._f_buttons,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY
        )

        self._f_data_set = tk.Frame(
            self._f_buttons,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY
        )

        self._f_train = tk.Frame(
            self._f_buttons,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY
        )

        self._f_test = tk.Frame(
            self._f_buttons,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY
        )

        self._f_help = tk.Frame(
            self._f_buttons,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY
        )

        self._f_exit = tk.Frame(
            self._f_buttons,
            padx=const.MW_FRAMES_PADX,
            pady=const.MW_FRAMES_PADY
        )

    def _create_buttons(self):
        """ Creates the buttons."""

        self._btn_info = tk.Button(
            self._f_info,

            state='disabled',       # TODO

            padx=const.MW_BTN_PADX,
            pady=const.MW_BTN_PADY,

            text=const.MGB_INFO_BTN,
            image=self._img_info,
            font=const.MW_FONT,

            command=self._local_info_eh,
            compound='left',
            bd=3
        )

        self._btn_data_set = tk.Button(
            self._f_data_set,

            padx=const.MW_BTN_PADX,
            pady=const.MW_BTN_PADY,

            text=const.MGB_DATA_SET_BTN,
            image=self._img_data_set,
            font=const.MW_FONT,

            command=self._local_create_data_set_eh,
            compound='left',
            bd=3
        )

        self._btn_train = tk.Button(
            self._f_train,

            padx=const.MW_BTN_PADX,
            pady=const.MW_BTN_PADY,

            text=const.MGB_TRAIN_BTN,
            image=self._img_train_sess,
            font=const.MW_FONT,

            command=self._local_train_eh,
            compound='left',
            bd=3
        )

        self._btn_test = tk.Button(
            self._f_test,

            padx=const.MW_BTN_PADX,
            pady=const.MW_BTN_PADY,

            text=const.MGB_TEST_BTN,
            image=self._img_test_sess,
            font=const.MW_FONT,

            command=self._local_test_eh,
            compound='left',
            bd=3
        )

        self._btn_help = tk.Button(
            self._f_help,

            state='disabled',       # TODO

            padx=const.MW_BTN_PADX,
            pady=const.MW_BTN_PADY,

            text=const.MGB_HELP_BTN,
            image=self._img_help,
            font=const.MW_FONT,

            command=self._local_help_eh,
            compound='left',
            bd=3
        )

        self._btn_exit = tk.Button(
            self._f_exit,

            padx=const.MW_BTN_PADX,
            pady=const.MW_BTN_PADY,

            text=const.MGB_EXIT_BTN,
            image=self._exit_image,
            font=const.MW_FONT,

            command=self._exit_eh,
            compound='left',
            bd=3
        )

    def _place_widgets(self):

        self._btn_info.pack(fill='both',
                            expand=True)
        self._btn_data_set.pack(fill='both',
                                expand=True)
        self._btn_train.pack(fill='both',
                             expand=True)
        self._btn_test.pack(fill='both',
                            expand=True)
        self._btn_help.pack(fill='both',
                            expand=True)
        self._btn_exit.pack(fill='both',
                            expand=True)

        self._f_info.pack(side='left',
                          fill='both',
                          expand=True)
        self._f_data_set.pack(side='left',
                              fill='both',
                              expand=True)
        self._f_train.pack(side='left',
                           fill='both',
                           expand=True)
        self._f_test.pack(side='left',
                          fill='both',
                          expand=True)
        self._f_help.pack(side='left',
                          fill='both',
                          expand=True)
        self._f_exit.pack(side='left',
                          fill='both',
                          expand=True)

        self._f_buttons.pack(side='top',
                             fill='x')

    def _raise_buttons(self):
        self._btn_info.config(relief="raised")
        self._btn_data_set.config(relief="raised")
        self._btn_train.config(relief="raised")
        self._btn_test.config(relief="raised")
        self._btn_help.config(relief="raised")

    #########################################################################
    # Event handling

    def _local_info_eh(self):
        self._raise_buttons()
        self._btn_info.config(relief="sunken")
        self._info_eh()

    def _local_create_data_set_eh(self):
        self._raise_buttons()
        self._btn_data_set.config(relief="sunken")
        self._create_data_set_eh()

    def _local_train_eh(self):
        self._raise_buttons()
        self._btn_train.config(relief="sunken")
        self._train_eh()

    def _local_test_eh(self):
        self._raise_buttons()
        self._btn_test.config(relief="sunken")
        self._test_eh()

    def _local_help_eh(self):
        self._raise_buttons()
        self._btn_help.config(relief="sunken")
        self._help_eh()

    #########################################################################
    # Public methods

    def enable(self):
        self._btn_data_set.config(state='normal')
        self._btn_train.config(state='normal')
        # self._btn_info.config(state='normal')     TODO
        self._btn_test.config(state='normal')
        # self._btn_help.config(state='normal')     TODO

    def disable(self):
        self._btn_data_set.config(state='disabled')
        self._btn_train.config(state='disabled')
        # self._btn_info.config(state='disabled')   TODO
        self._btn_test.config(state='disabled')
        # self._btn_help.config(state='disabled')   TODO

    #########################################################################
