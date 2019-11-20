from graphics.widgets.progress_bar_c import ProgressBarC

import constants.widget_constants as const
import tkinter as tk


class GuessesF(tk.Frame):
    """ Contains X progress bars, where X is const.GF_NUMBER_OF_GUESSES."""

    def __init__(self,

                 parent,

                 texts,
                 percents):
        """
        :param parent: Parent.

        :param texts: List of length n* with the text to display in each
                      progress bar.
        :param percents: List of length n* with the progress in percents for 
                         each bar.

        * n = const.GF_NUMBER_OF_GUESSES
        """

        tk.Frame.__init__(self,
                          parent)

        self._validate_text_and_percent_list(
            percents=percents,
            texts=texts
        )

        self._progress_bar = []

        self._texts = texts
        self._percents = percents

        self._draw_progress_bars()

    #########################################################################
    # Widget creation and placement

    def _draw_progress_bars(self):
        """ Draws the progress bars."""

        for index in range(const.GF_NUMBER_OF_GUESSES):
            tmp_progress_bar = ProgressBarC(
                parent=self,

                height=const.GF_PB_HEIGHT,
                width=const.GF_INITIAL_WIDTH,

                text=self._texts[index],
                fill_percent=self._percents[index],

                fill_color=const.GF_FILL_COLORS[index],
                text_color=const.GF_TEXT_COLORS[index],
                empty_color=const.GF_EMPTY_COLORS[index]
            )

            self._progress_bar.append(tmp_progress_bar)

            tmp_progress_bar.pack(side='top',
                                  fill='x',
                                  expand=True)

    #########################################################################
    # Static methods

    @staticmethod
    def _validate_text_and_percent_list(texts, percents):
        """  If the texts or percent do not have the required length 
        ValueError is raised.

        :param texts: List of length n* with the text to display in each
                      progress bar.
        :param percents: List of length n* with the progress in percents for
                         each bar.

        * n = const.GF_NUMBER_OF_GUESSES
        """

        if len(texts) != const.GF_NUMBER_OF_GUESSES \
                or len(percents) != const.GF_NUMBER_OF_GUESSES:
            raise ValueError('The number of guesses must be {0}'.
                             format(const.GF_NUMBER_OF_GUESSES))

    #########################################################################
    # Public methods

    def update_progress_bars(
            self,

            texts,
            percents):
        """ Updates the progress bar.

        :param texts: List of length n* with the text to display in each
                      progress bar.
        :param percents: List of length n* with the progress in percents for
                         each bar.

        * n = const.GF_NUMBER_OF_GUESSES
        """

        self._texts = texts
        self._percents = percents

        self._validate_text_and_percent_list(
            percents=percents,
            texts=texts
        )

        for index in range(const.GF_NUMBER_OF_GUESSES):
            self._progress_bar[index].update_progress(
                percent=self._percents[index],
                text=self._texts[index]
            )

    #########################################################################
