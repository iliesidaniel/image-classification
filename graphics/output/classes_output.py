from utils.data_set.data_set_classes import DataSetClasses
from tkinter import messagebox
from tkinter import ttk

import constants.output_constants as const
import tkinter as tk
import sys


class ClassesOutputF(tk.Frame):
    """
    - Use to display details about classes.
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
                          parent,
                          relief=const.CO_FRAME_RELIEF,
                          padx=const.CO_FRAME_PADX,
                          pady=const.CO_FRAME_PADY,
                          bd=const.CO_FRAME_BD)

        self._text_disabled = tk.Label()['disabledforeground']
        self._text_enable = tk.Label()['foreground']
        self._background = tk.Frame()['background']

        self._classes = []

        self._create_widgets()
        self._place_widgets()

        self._create_columns()

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        self.style = ttk.Style()
        self.style.configure("Treeview",
                             background=self._background,
                             font=const.CO_TABLE_FONT)
        self.style.configure("Treeview.Heading",
                             background=self._background,
                             font=const.CO_HEADING_FONT)

        self._lbl_title = tk.Label(
            self,

            font=const.CO_TITLE_FONT,
            text=const.CO_TITLE_TEXT,

            padx=const.CO_TITLE_PADX,
            pady=const.CO_TITLE_PADY,
        )

        self._f_output = tk.Frame(
            self,

            relief=const.CO_SUBFRAME_RELIEF,
            bd=const.CO_SUBFRAME_BD,
        )

        self._t_output = ttk.Treeview(
            self._f_output,

            height=const.CO_TABLE_HEIGHT,
            style='Treeview'
        )

        self._t_output['show'] = 'headings'

        self.sb_x = tk.Scrollbar(
            self._f_output,

            orient=tk.HORIZONTAL,
            command=self._t_output.xview
        )

        self.sb_y = tk.Scrollbar(
            self._f_output,

            orient=tk.VERTICAL,
            command=self._t_output.yview
        )

        self._t_output.config(yscroll=self.sb_y.set,
                              xscroll=self.sb_x.set)

    def _place_widgets(self):

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self.sb_y.pack(side='right',
                       fill='y')

        self.sb_x.pack(side='bottom',
                       fill='x')

        self._f_output.pack(side='top',
                            fill='both',
                            expand=True)

        self._t_output.pack(side='top',
                            fill='both',
                            expand=True)

    #########################################################################
    # Auxiliary methods

    def _create_columns(self):
        """
        - Creates the table columns.
        """

        class_names = const.CO_TABLE_COLUMNS

        self._t_output.config(columns=class_names)

        for index in range(len(class_names)):
            col = '#' + str(index + 1)

            self._t_output.column(column=col,
                                  anchor='center',
                                  minwidth=150,
                                  stretch=True)

            self._t_output.heading(column=col,
                                   text=class_names[index])

    def _show_classes(self):
        """
        - Populates the table with details about the classes.
        """

        for _class in self._classes:
            self._t_output.insert(
                parent='',
                index='end',
                values=(
                    _class.identifier,
                    _class.class_name,
                    _class.number_of_examples
                )
            )

    def _clear_table(self):
        """
        - Clears the table.
        """

        self._t_output.delete(*self._t_output.get_children())

    @staticmethod
    def _kill():
        """
        - In case something goes wrong this method displays a message and 
        exits the application.        
        """

        messagebox.showerror(
            title='Fatal error',
            message='Sorry.\n\nSomething went wrong while showing the '
                    'classes.'
        )

        sys.exit(564)

    #########################################################################
    # Public methods

    def update_classes(
            self,

            classes: DataSetClasses):
        """
        - Updates the classes.
        
        :param classes: DataSetClasses
        """

        self._classes = classes.get_data_set_classes()

        self._clear_table()
        self._show_classes()

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_title.config(state='normal')
        self.style.configure("Treeview",
                             foreground=self._text_enable)
        self.style.configure("Treeview.Heading",
                             foreground=self._text_enable)

    def disable(self):
        """ Disables all the widgets."""

        self._lbl_title.config(state='disabled')
        self.style.configure("Treeview",
                             foreground=self._text_disabled)
        self.style.configure("Treeview.Heading",
                             foreground=self._text_disabled)

    #########################################################################
