from utils.train.train_sess_message import TrainSessMessage
from tkinter import ttk

import constants.output_constants as const
import tkinter as tk


class TrainSessOutputF(tk.Frame):
    """
    - Use to display messages from the training session.
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

        self._text_disabled = tk.Label()['disabledforeground']
        self._text_enable = tk.Label()['foreground']
        self._background = tk.Frame()['background']

        self._message = TrainSessMessage()

        self._ids_and_classes = []

        self._create_widgets()
        self._place_widgets()

        self._create_columns()

        if disabled:
            self.disable()
        else:
            self.enable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        self._style = ttk.Style()
        self._style.configure("Treeview",
                              background=self._background,
                              font=const.TRSO_TABLE_FONT)
        self._style.configure("Treeview.Heading",
                              background=self._background,
                              font=const.TRSO_HEADING_FONT)

        self._t_output = ttk.Treeview(
            self,

            height=const.TRSO_TABLE_HEIGHT,
            style='Treeview'
        )

        self._t_output.heading('#0',
                               text='Time')

        self.sb_x = tk.Scrollbar(
            self,

            orient=tk.HORIZONTAL,
            command=self._t_output.xview
        )

        self.sb_y = tk.Scrollbar(
            self,

            orient=tk.VERTICAL,
            command=self._t_output.yview
        )

        self._t_output.config(yscroll=self.sb_y.set,
                              xscroll=self.sb_x.set)

    def _place_widgets(self):

        self.sb_y.pack(side='right',
                       fill='y')

        self.sb_x.pack(side='bottom',
                       fill='x')

        self._t_output.pack(side='top',
                            fill='both',
                            expand=True)

    #########################################################################
    # Auxiliary methods

    def _create_columns(self):
        """
        - Creates the table columns.
        """

        column_names = const.TRSO_TABLE_COLUMNS

        self._t_output.config(columns=column_names)

        for index in range(len(column_names)):
            col = '#' + str(index + 1)

            self._t_output.column(column=col,
                                  anchor='center',
                                  minwidth=150,
                                  stretch=True)

            self._t_output.heading(column=col,
                                   text=column_names[index])

    def _show_message(self):
        """
        - Adds new message.
        """

        self._t_output.insert(
            parent='',
            index='end',
            text=self._message.time,
            values=(
                self._message.step,
                self._message.loss,
                self._message.examples_per_sec,
                self._message.seconds_per_batch
            )
        )

        self._t_output.yview_moveto(1)

    #########################################################################
    # Public methods

    def clear(self):
        """
        - Clears the table.
        """

        self._t_output.delete(*self._t_output.get_children())

    def new_message(
            self,

            message: TrainSessMessage):
        """
        - Displays a new message from the training session.

        :param message: TrainSessMessage
        """

        self._message = message

        self._show_message()

    def enable(self):
        """ Enables all the widgets."""

        self._style.configure("Treeview",
                              foreground=self._text_enable)
        self._style.configure("Treeview.Heading",
                              foreground=self._text_enable)

    def disable(self):
        """ Disables all the widgets."""

        self._style.configure("Treeview",
                              foreground=self._text_disabled)
        self._style.configure("Treeview.Heading",
                              foreground=self._text_disabled)

    #########################################################################
