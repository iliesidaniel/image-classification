import tkinter as tk

import constants.charts_constants as const
from utils.charts.chart_entries import ChartEntries


class ColumnChart(tk.Canvas):
    """ 
    - Use to draw column chart.
    """

    def __init__(self,

                 parent):
        """
        :param parent: Parent. 
        """

        tk.Canvas.__init__(self,
                           parent,
                           height=675,
                           width=1500)

        self._drawable_start_x = 150
        self._drawable_start_y = 500
        self._drawable_end_x = 1350
        self._drawable_end_y = 75

        self._canvas_start_x = 0
        self._canvas_start_y = 675
        self._canvas_end_x = 1500
        self._canvas_end_y = 0

        self._full_height = self._drawable_start_y - self._drawable_end_y
        self._full_width = self._drawable_end_x - self._drawable_start_x

        self._1_percent_height = self._full_height / 100
        self._1_percent_width = self._full_width / 100

        # self._draw_bg_and_drawable_bg()
        self._draw_axes()

        self._chart_entries = []
        self._m_line = None
        self._ci_lines = []
        self._columns = []
        self._texts = []

    #########################################################################

    def _draw_bg_and_drawable_bg(self):
        """
        - Draws rectangles that represent the total space used and the space
        on which the columns will be drawing.
        """

        # Total used space.
        self.create_rectangle(self._canvas_start_x,
                              self._canvas_start_y,
                              self._canvas_end_x,
                              self._canvas_end_y,
                              fill='light blue',
                              width=0)

        # Space used for drawing.
        self.create_rectangle(self._drawable_start_x,
                              self._drawable_start_y,
                              self._drawable_end_x,
                              self._drawable_end_y,
                              fill='light green',
                              width=0)

    def _draw(self):
        """ 
        - Draws the columns and the texts.
        """

        self._determine_col_and_sep_widths()
        self._clear()

        self._avg_y = 0

        for i in range(len(self._chart_entries)):
            percent = self._chart_entries[i].y

            self._last_point = self._last_point + self._separator_width

            height = round(self._1_percent_height * percent)
            width = self._last_point + self._column_width

            x1 = self._drawable_start_x + self._last_point
            y1 = self._drawable_start_y
            x2 = self._drawable_start_x + width
            y2 = self._drawable_start_y - height

            if percent == 0:
                y1 = y1 - 1
                y2 = y2 - 1

            self._draw_column(x1=x1,
                              y1=y1,
                              x2=x2,
                              y2=y2)

            x = int((x1 + x2) / 2)

            self._ci_lines.append(self.create_line(
                    x,
                    y2,
                    x,
                    y2 + self._chart_entries[i].confidence_interval_95,

                    width=const.CC_XOY_WIDTH,
                    fill='#d8fc0a'
                )
            )

            self._ci_lines.append(self.create_line(
                    x,
                    y2,
                    x,
                    y2 - self._chart_entries[i].confidence_interval_95,

                    width=const.CC_XOY_WIDTH,
                    fill='#d8fc0a'
                )
            )

            text = self._chart_entries[i].identifier[:11] + ' - ' + str(percent) + '%'
            y = y1 + 25
            x = x2

            self._draw_text(text=text,
                            x=x,
                            y=y)

            self._last_point = self._last_point + self._column_width
            self._avg_y += self._chart_entries[i].y

        self._avg_y = int(round(self._avg_y / len(self._chart_entries)))
        height = self._drawable_start_y \
            - round(self._1_percent_height * self._avg_y)

        self._m_line = self.create_line(
            self._drawable_start_x,
            height,
            self._drawable_end_x,
            height,

            width=const.CC_XOY_WIDTH,
            fill='#fc6e02'
        )

    def _draw_axes(self):
        """ 
        - Draws xOy axes.
        """

        self._ox = self.create_line(
            self._drawable_start_x - 2,
            self._drawable_start_y + const.CC_XOY_OX_Y_OFFSET,
            self._drawable_end_x + 50,
            self._drawable_start_y + const.CC_XOY_OX_Y_OFFSET,

            width=const.CC_XOY_WIDTH,
            fill=const.CC_XOY_FILL
        )

        self._oy = self.create_line(
            self._drawable_start_x,
            self._drawable_start_y,
            self._drawable_start_x,
            self._drawable_end_y - 50,

            width=const.CC_XOY_WIDTH,
            fill=const.CC_XOY_FILL
        )

    def _draw_column(
            self,

            x1: int,
            y1: int,
            x2: int,
            y2: int):
        """ 
        - Draws column
        """

        self._columns.append(
            self.create_rectangle(
                x1, y1, x2, y2,

                fill=const.CC_COLUMN_FILL,
                width=0)
        )

    def _draw_text(
            self,

            text: str,
            x: int,
            y: int):
        """ 
        - Draws text.
        """

        self._texts.append(
            self.create_text(
                x, y,

                anchor='se',
                angle=45,

                font=const.CC_COLUMN_TEXT_FONT,
                fill='#043b66',
                text=text
            )
        )

    def _determine_col_and_sep_widths(self):
        """ 
        - Determines how wide the columns and the spaces will be. 
        """

        column_nbr = len(self._chart_entries)
        separators_and_columns_nbr = column_nbr * 2 + 1

        width = self._full_width / separators_and_columns_nbr
        width = int(round(width))

        self._separator_width = width
        self._column_width = width
        self._last_point = 0

    def _clear(self):
        """
        - Removes all the columns and the texts.
        """

        for i in range(len(self._texts)):
            self.delete(self._ci_lines[i * 2 + 1])
            self.delete(self._ci_lines[i * 2])
            self.delete(self._columns[i])
            self.delete(self._texts[i])

        self.delete(self._m_line)

        self._ci_lines = []
        self._columns = []
        self._texts = []

    #########################################################################
    # Public methods

    def update_values(
            self,

            chart_entries: ChartEntries):
        """ 
        - Updates the ChartEntries list and redraws the chart.
        """

        if chart_entries is not None:
            self._chart_entries = chart_entries.get_entries()

            self._draw()

    #########################################################################
