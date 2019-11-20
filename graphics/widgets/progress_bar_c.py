import constants.global_constants as const
import tkinter as tk
import time


class ProgressBarC(tk.Canvas):
    """
    - Simple progress bar that will resize automatically when the dimensions
    of the parent are changed.
    - Some information about the progress can be displayed in the progress bar
    with the text parameter (at construction and later by calling the
    update_progress() method).
    - To update the text and progress call update_progress().
    - The colors can be changed by calling change_colors().
    """

    def __init__(self,
                 parent,

                 width: int,
                 height: int,

                 text: str,
                 fill_percent: int,

                 fill_color: str,
                 empty_color: str,
                 text_color: str):
        """
        :param parent: Parent widget.

        :param width: Width.
        :param height: Height.

        :param text: Text that will be displayed in the progress bar.
        :param fill_percent: Assumed to be integer, >= 0 and <= 100.

        :param fill_color: Progress color.
        :param empty_color: Empty space color.
        :param text_color: Text color.
        """

        tk.Canvas.__init__(self,
                           parent,
                           width=width,
                           height=height)

        self._width = width
        self._height = height

        self._text = text

        self._fill_percent = fill_percent

        self._fill_color = fill_color
        self._empty_color = empty_color
        self._text_color = text_color

        self.bind("<Configure>", self._resize)

        self._time_of_last_update = time.time() - 10
        self._draw_progress_bar()

    #########################################################################

    def _draw_progress_bar(self):
        """ Draws the Progress bar"""

        # See _determine_fill_length() description.
        fill_width = self._determine_fill_length()

        # This rectangle represents the progress.
        self._pb_fill_rectangle = self.create_rectangle(
            0,
            0,
            fill_width,
            self._height,
            fill=self._fill_color,
            width=0
        )

        # This rectangle represents how much is left to do.
        self._pb_empty_rectangle = self.create_rectangle(
            fill_width,
            0,
            self._width + 1,
            self._height,
            fill=self._empty_color,
            width=0
        )

        # Text that will be displayed in the progress bar.
        self._pb_fill_text = self.create_text(
            self._width / 2,
            self._height / 2,
            font=const.GLOBAL_FONT_M,
            fill=self._text_color,
            text=self._text,
            width=0
        )

    def _determine_fill_length(self):
        """ Determines how long the filling rectangle has to be in order to
        respect the progress percentage.

        :return: Filling rectangle width.
        """

        fill_width = self._width / 100 * self._fill_percent + 1

        return fill_width

    def _resize(self, event):
        """ Called automatically when the window is resized."""

        self.delete("all")

        self._width = event.width

        self._draw_progress_bar()

    #########################################################################
    # Public methods

    def update_progress(
            self,

            percent: int,
            text: str):
        """
        - Updates the progress to the new progress percentage and the text
        showed in the progress bar.
        - The parameters are considered correct.

        :param percent:    - >= 0 and <= 100;
                           - New progress percent.
        :param text: New progress bar text.
        """

        self._fill_percent = percent
        current_time = time.time()
        self._text = text

        if current_time - self._time_of_last_update >= 0.5 \
                or self._fill_percent == 100:

            self._time_of_last_update = current_time
            self._draw_progress_bar()

    def change_colors(
            self,

            background_color: str,
            fill_color: str,
            text_color: str):
        """
        - Changes the colors.
        - The parameters are considered correct.
        - Example:  - '#4286f4';
                    - '#333333'.

        :param background_color: Background color.
        :param fill_color: Progress color.
        :param text_color: Text color.
        """

        self._empty_color = background_color
        self._fill_color = fill_color
        self._text_color = text_color

        self._draw_progress_bar()

    #########################################################################
