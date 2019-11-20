from utils.call_method_in_new_thread import CallMethodInNewThread
from controllers.session_controller import SessionController

from graphics.widgets.image_holder import ImageHolder
from graphics.widgets.guesses_f import GuessesF
from graphics.widgets.browse_f import BrowseF

from session.interact_session import InteractSession

from datetime import timedelta

import constants.manual_test_sess_constants as const
import constants.global_constants as g_const
import tkinter as tk


class ManualTestSessGUI(tk.Frame):
    """ 
     - GUI to let the user manually test a session by choosing pictures for
    which will be displayed the top const.GF_NUMBER_OF_GUESSES guesses.
    """

    def __init__(self,

                 parent,

                 enable_test_sess_buttons,
                 disable_test_sess_buttons):
        """
        :param parent: 
        :param enable_test_sess_buttons: 
        :param disable_test_sess_buttons: 
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.IW_WINDOW_PADX,
                          pady=const.IW_WINDOW_PADY)

        self._disable_test_sess_buttons = disable_test_sess_buttons
        self._enable_test_sess_buttons = enable_test_sess_buttons

        self._image_path = ''

        self._create_main_frames()
        self._populate_frames()
        self._place_frames()

    #########################################################################
    # Widget creation and placement

    def _create_main_frames(self):
        """ Creates the frames."""

        self._f_browse = tk.Frame(self)

        self._f_image_and_guesses = tk.Frame(self)

        self._f_left = tk.Frame(
            self._f_image_and_guesses,
            padx=const.IW_FRAMES_PADX,
            pady=const.IW_FRAMES_PADY
        )

        self._f_right = tk.Frame(
            self._f_image_and_guesses,
            padx=const.IW_FRAMES_PADX,
            pady=const.IW_FRAMES_PADY
        )

        self._f_run_button = tk.Frame(
            self._f_right,
            padx=const.RF_PADX,
            pady=const.RF_PADY
        )

        self._f_time = tk.Frame(
            self._f_right,
            padx=const.TF_PADX,
            pady=const.TF_PADY
        )

    def _populate_frames(self):
        """
        - Creates additional widgets that will be displayed in the frames.
        """

        self._f_session_file_details = BrowseF(
            parent=self._f_browse,

            user_instruction=const.BC_USER_INSTRUCTION,
            no_selection_message=const.BC_NO_SELECTION_MESSAGE,
            browse_window_title=const.BC_BROWSE_WINDOW_TITLE,
            initial_path=const.BC_INITIAL_DIRECTORY,
            supported_files=g_const.GLOBAL_SESSION_BROWSE_ENTRY,

            browse_button_eh=self._valid_session_path_and_name,
            directory=False
        )

        self._f_browse_image = BrowseF(
            parent=self._f_browse,

            user_instruction=const.BI_USER_INSTRUCTION,
            no_selection_message=const.BI_NO_SELECTION_MESSAGE,
            browse_window_title=const.BI_BROWSE_WINDOW_TITLE,
            initial_path=const.BI_INITIAL_DIRECTORY,
            supported_files=const.BI_SUPPORTED_FILES,

            browse_button_eh=self._new_image_eh,

            disabled=True
        )

        self._f_image_holder = ImageHolder(
            self._f_left,
            const.IHF_INITIAL_IMAGE
        )

        self._f_guesses = GuessesF(
            parent=self._f_right,
            texts=const.GF_NO_INPUT_PB_TEXT,
            percents=const.GF_NO_INPUT_PERCENTS
        )

        self._btn_run = tk.Button(
            self._f_run_button,
            command=self._run_button_eh,
            text=const.RF_BUTTON_TEXT,
            font=const.IW_FONT,
            state='disabled'
        )

        self._lbl_time_text = tk.Label(
            self._f_time,
            text=const.TF_FIXED_LABEL_TEXT,
            font=const.IW_FONT
        )

        self._lbl_time_info = tk.Label(
            self._f_time,
            text=const.TF_NO_INTERACTION_TIME,
            font=const.IW_FONT_I
        )

    def _place_frames(self):
        """ Places the frames and the additional widgets."""

        self._f_browse.pack(side='top',
                            fill='both',
                            expand=True)
        self._f_image_and_guesses.pack(side='top',
                                       fill='both',
                                       expand=True)

        self._f_session_file_details.pack(side='top',
                                          fill='both',
                                          expand=True)
        self._f_browse_image.pack(side='top',
                                  fill='both',
                                  expand=True)

        self._f_left.pack(side='left',
                          fill='both',
                          expand=True)
        self._f_right.pack(side='right',
                           fill='both',
                           expand=True)

        self._f_run_button.pack(side='top',
                                fill='both',
                                expand=True)
        self._f_guesses.pack(side='top',
                             fill='both',
                             expand=True)
        self._f_time.pack(side='top',
                          fill='both',
                          expand=True)

        self._btn_run.pack(side='top',
                           fill='both',
                           expand=True)
        self._lbl_time_text.pack(side='left',
                                 fill='both',
                                 expand=True)
        self._lbl_time_info.pack(side='right',
                                 fill='both',
                                 expand=True)

        self._f_image_holder.pack(side='top',
                                  fill='both',
                                  expand=True)

    #########################################################################
    # Event handling

    def _valid_session_path_and_name(
            self,
            session_path: str):
        """ Automatically called when the user selected a CNN file.
        
        :param session_path: Path and name of the CNN file.
        """

        self._f_browse_image.enable()
        self._btn_run.config(state='disabled')

        self._session_details = SessionController.read_main_session_file(
            session_file_path=session_path
        )

    def _new_image_eh(
            self,
            image_path: str):
        """ Automatically called when the user selected another image.

        :param image_path: Path and file name of the selected image.
        """

        self._btn_run.config(state='normal')

        self._f_image_holder.update_image(image_path)
        self._image_path = image_path

        self._update_running_time(const.TF_NO_INTERACTION_TIME)
        self._f_guesses.update_progress_bars(
            const.GF_NO_INPUT_PB_TEXT,
            const.GF_NO_INPUT_PERCENTS
        )

    def _run_button_eh(self):
        """ Automatically called when the "Run" button is pressed."""

        self._disable_test_sess_buttons()

        self._btn_run.config(state='disabled')
        self._f_browse_image.disable()

        self._interact_session = InteractSession(
            update_guesses_and_time=self.update_guesses_and_running_time,
            session_details=self._session_details
        )

        CallMethodInNewThread.call_method(
            self._interact_session.evaluate_image,
            image_path=self._image_path
        )

    #########################################################################
    # _update methods

    def _update_running_time(
            self,
            execution_time: timedelta):
        """ Updates the execution time.

        :param execution_time: Time required by the CNN to process the image.
        """

        self._f_browse_image.enable()
        self._btn_run.config(state='normal')

        self._lbl_time_info.config(text=execution_time)

    def _update_guesses(
            self,
            labels,
            guesses):
        """ Updates the progress bars.

        :param labels: - Array with the labels;
                       - Assumed int
                       - Assumed with the length equal to
                         const.GF_NUMBER_OF_GUESSES

        :param guesses: - Array with the guesses;
                        - Assumed with the length equal to
                          const.GF_NUMBER_OF_GUESSES
        """

        i = 0
        guesses_str = []
        while i < const.GF_NUMBER_OF_GUESSES:
            tmp_str = const.GF_LABELS[labels[i]] \
                      + '  -  ' \
                      + str(int(guesses[i]))

            guesses_str.append(tmp_str)

            i += 1

        self._f_guesses.update_progress_bars(guesses_str, guesses)

    #########################################################################
    # Public methods

    def update_guesses_and_running_time(
            self,
            labels,
            guesses,
            running_time: timedelta):
        """ Call this method to update the progress bars and the running
        time.

        :param labels: - Array with the labels;
                       - Assumed int
                       - Assumed with the length equal to
                         const.GF_NUMBER_OF_GUESSES

        :param guesses: - Array with the guesses;
                        - Assumed with the length equal to
                          const.GF_NUMBER_OF_GUESSES

        :param running_time: The time required by the CNN to process the
                             image.
        """

        self._update_guesses(labels, guesses)
        self._update_running_time(running_time)

        self._enable_test_sess_buttons()

    #########################################################################
