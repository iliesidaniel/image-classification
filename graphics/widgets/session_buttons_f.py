import constants.widget_constants as const
import utils.utils as utils
import tkinter as tk


class SessionButtonsF(tk.Frame):
    """ - Frame that contains 4 buttons:
            + Start
            + Pause
            + Stop
            + Cancel

        - Enable/disable:
            + n state | Start | Pause | Stop | Cancel |
            + Start   |   n   |   d   |  d   |    n   |
            + Pause   |   d   |   n   | n/d  |   n/d  |
            + Stop    |   d   |   d   |  d   |    d   |
            + Cancel  |   d   |   d   |  d   |    d   |

            + n = normal
            + d = disabled

        - All buttons can be disabled at construction, check constructor
        description.
    """

    def __init__(self,
                 parent,

                 start_eh,
                 pause_eh,
                 stop_eh,
                 cancel_eh,

                 disabled=False):
        """
        :param parent: Parent;

        :param start_eh: Method that will be called when the "Start" button
                         is pressed;
        :param pause_eh: Method that will be called when the "Pause" button
                         is pressed;
        :param stop_eh: Method that will be called when the "Stop" button
                        is pressed;
        :param cancel_eh: Method that will be called when the "Cancel" button
                          is pressed;

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.SB_FRAME_PADX,
                          pady=const.SB_FRAME_PADY)

        self._start_event_handler = start_eh
        self._pause_event_handler = pause_eh
        self._stop_event_handler = stop_eh
        self._cancel_event_handler = cancel_eh

        self._load_icons()
        self._create_frames()
        self._create_buttons()
        self._place_buttons()

        if disabled:
            self.disable()
        else:
            self.enable()

    #########################################################################
    # Widget creation and placement

    def _load_icons(self):
        """ Loads the images that will be displayed in the buttons."""

        self._start_image = utils.load_and_resize_image(
            const.SB_BTN_START_IMG_PATH,
            const.SB_IMG_WIDTH,
            const.SB_IMG_HEIGHT
        )
        self._pause_image = utils.load_and_resize_image(
            const.SB_BTN_PAUSE_IMG_PATH,
            const.SB_IMG_WIDTH,
            const.SB_IMG_HEIGHT
        )
        self._stop_image = utils.load_and_resize_image(
            const.SB_BTN_STOP_IMG_PATH,
            const.SB_IMG_WIDTH,
            const.SB_IMG_HEIGHT
        )
        self._cancel_image = utils.load_and_resize_image(
            const.SB_BTN_CANCEL_IMG_PATH,
            const.SB_IMG_WIDTH,
            const.SB_IMG_HEIGHT
        )

    def _create_frames(self):
        """ Creates the frames."""

        self._f_start = tk.Frame(
            self,
            padx=const.SB_BTN_FRAME_PADX,
            pady=const.SB_BTN_FRAME_PADY
        )

        self._f_pause = tk.Frame(
            self,
            padx=const.SB_BTN_FRAME_PADX,
            pady=const.SB_BTN_FRAME_PADY
        )

        self._f_stop = tk.Frame(
            self,
            padx=const.SB_BTN_FRAME_PADX,
            pady=const.SB_BTN_FRAME_PADY
        )

        self._f_cancel = tk.Frame(
            self,
            padx=const.SB_BTN_FRAME_PADX,
            pady=const.SB_BTN_FRAME_PADY
        )

    def _create_buttons(self):
        """ Creates the buttons."""

        self._btn_start = tk.Button(
            self._f_start,
            command=self._start_btn_pressed,
            text=const.SB_START_BUTTON_TEXT,
            padx=const.SB_BUTTON_PADX,
            pady=const.SB_BUTTON_PADY,
            image=self._start_image,
            font=const.SB_FONT,
            compound='left'
        )

        self._btn_pause = tk.Button(
            self._f_pause,
            command=self._pause_btn_pressed,
            text=const.SB_PAUSE_BUTTON_TEXT,
            padx=const.SB_BUTTON_PADX,
            pady=const.SB_BUTTON_PADY,
            image=self._pause_image,
            font=const.SB_FONT,
            compound='left'
        )

        self._btn_stop = tk.Button(
            self._f_stop,
            command=self._stop_btn_pressed,
            text=const.SB_STOP_BUTTON_TEXT,
            padx=const.SB_BUTTON_PADX,
            pady=const.SB_BUTTON_PADY,
            image=self._stop_image,
            font=const.SB_FONT,
            compound='left'
        )

        self._btn_cancel = tk.Button(
            self._f_cancel,
            command=self._cancel_btn_pressed,
            text=const.SB_CANCEL_BUTTON_TEXT,
            padx=const.SB_BUTTON_PADX,
            pady=const.SB_BUTTON_PADY,
            image=self._cancel_image,
            font=const.SB_FONT,
            compound='left'
        )

    def _place_buttons(self):
        """ Places the widgets."""

        self._btn_start.pack(side='left',
                             fill='both',
                             expand=True)
        self._btn_pause.pack(side='left',
                             fill='both',
                             expand=True)
        self._btn_stop.pack(side='left',
                            fill='both',
                            expand=True)
        self._btn_cancel.pack(side='left',
                              fill='both',
                              expand=True)

        self._f_start.pack(side='left',
                           fill='both',
                           expand=True)
        self._f_pause.pack(side='left',
                           fill='both',
                           expand=True)
        self._f_stop.pack(side='left',
                          fill='both',
                          expand=True)
        self._f_cancel.pack(side='left',
                            fill='both',
                            expand=True)

    #########################################################################
    # Event handling

    def _start_btn_pressed(self):
        """
        - Called automatically when the "Start" button is pressed.
        - "Start" button will have the state set to "disabled", the other
        buttons will have their state set to "normal".
        - Calls the method specified by the constructor parameter
        "start_event_handler".
        """

        self._btn_start.config(state='disabled')
        self._btn_pause.config(state='normal')
        self._btn_stop.config(state='normal')
        self._btn_cancel.config(state='normal')

        self._start_event_handler()

    def _pause_btn_pressed(self):
        """
        - Called automatically when the "Pause" button is pressed.
        - "Pause" button will have the state set to "disabled", the other
        buttons will have their state set to "normal".
        - Calls the method specified by the constructor parameter
        "pause_event_handler".
        """

        self._btn_start.config(state='normal')
        self._btn_pause.config(state='disabled')
        self._btn_stop.config(state='normal')
        self._btn_cancel.config(state='normal')

        self._pause_event_handler()

    def _stop_btn_pressed(self):
        """
        - Called automatically when the "Stop" button is pressed.
        - "Start" button will have the state set to "normal", the other
        buttons will have their state set to "disabled".
        - Calls the method specified by the constructor parameter
        "stop_event_handler".
        """

        self._btn_start.config(state='disabled')
        self._btn_pause.config(state='disabled')
        self._btn_stop.config(state='disabled')
        self._btn_cancel.config(state='disabled')

        self._stop_event_handler()

    def _cancel_btn_pressed(self):
        """
        - Called automatically when the "Cancel" button is pressed.
        - "Start" button will have the state set to "normal", the other
        buttons will have their state set to "disabled".
        - Calls the method specified by the constructor parameter
        "cancel_event_handler".
        """

        self._btn_start.config(state='disabled')
        self._btn_pause.config(state='disabled')
        self._btn_stop.config(state='disabled')
        self._btn_cancel.config(state='disabled')

        self._cancel_event_handler()

    #########################################################################
    # Public methods

    def enable(self):
        """ Enables the "Start" button and disables the others."""

        self._btn_start.config(state='normal')
        self._btn_pause.config(state='disabled')
        self._btn_stop.config(state='disabled')
        self._btn_cancel.config(state='disabled')

    def disable(self):
        """ Disables all the buttons."""

        self._btn_start.config(state='disabled')
        self._btn_pause.config(state='disabled')
        self._btn_stop.config(state='disabled')
        self._btn_cancel.config(state='disabled')

    def task_started(self):
        """ Call this method if the task started without using the "Start"
        button, it will set the correct enable / disable state.
        """

        self._start_btn_pressed()

    def task_finished(self):
        """ Call this method when the task is finished, it will set the
        correct enable / disable state.
        """

        self._stop_btn_pressed()

    #########################################################################
