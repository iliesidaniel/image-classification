from utils.data_set.data_set_class import DataSetClass

from tkinter import messagebox
from tkinter import ttk


import constants.output_constants as const

import tkinter as tk
import sys


class ConfusionMatrixOutputF(tk.Frame):

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
                          relief=const.CMO_FRAME_RELIEF,
                          padx=const.CMO_FRAME_PADX,
                          pady=const.CMO_FRAME_PADY,
                          bd=const.CMO_FRAME_BD)

        self._text_disabled = tk.Label()['disabledforeground']
        self._text_enable = tk.Label()['foreground']
        self._background = tk.Frame()['background']

        self._confusion_matrix = []
        self._ids_and_classes = []

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()
        else:
            self.enable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        self.style = ttk.Style()
        self.style.configure("Treeview",
                             background=self._background,
                             font=const.CMO_TABLE_FONT)
        self.style.configure("Treeview.Heading",
                             background=self._background,
                             font=const.CMO_HEADING_FONT)

        self._lbl_title = tk.Label(
            self,

            font=const.CMO_TITLE_FONT,
            text=const.CMO_TITLE_TEXT,

            padx=const.CMO_TITLE_PADX,
            pady=const.CMO_TITLE_PADY,
        )

        self._f_output = tk.Frame(
            self,

            relief=const.CMO_SUBFRAME_RELIEF,
            bd=const.CMO_SUBFRAME_BD,
        )

        self._t_output = ttk.Treeview(
            self._f_output,

            height=const.CMO_TABLE_HEIGHT,
            style='Treeview'
        )

        self._t_output.heading('#0',
                               text='Class name')

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

        class_names = []

        for id_and_class in self._ids_and_classes:
            class_names.append(id_and_class.class_name)

        self._t_output.config(columns=class_names)

        self._t_output.column(column='#0',
                              minwidth=160,
                              anchor='center',
                              stretch=True)

        for id_and_class in self._ids_and_classes:
            self._t_output.column(column=id_and_class.class_name,
                                  anchor='center',
                                  minwidth=150,
                                  stretch=True)

            self._t_output.heading(column=id_and_class.class_name,
                                   text=id_and_class.class_name)

    def _show_matrix(self):
        """
        - Populates the table with the confusion matrix.         
        """

        for row in range(len(self._confusion_matrix)):
            self._t_output.insert(parent='',
                                  index='end',
                                  text=self._ids_and_classes[row].class_name,
                                  values=(self._confusion_matrix[row]))

    def _clear_table(self):
        """
        - Clears the table
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
                    'confusion matrix.'
        )

        sys.exit(2)

    #########################################################################
    # Public methods

    def set_confusion_matrix(
            self,

            confusion_matrix: []):
        """
        - Sets the confusion matrix.
        
        :param confusion_matrix: Confusion matrix. 
        """

        length = len(confusion_matrix)

        for row in range(length):
            for col in range(length):
                if not isinstance(confusion_matrix[row][col], int):
                    self._kill()
                else:
                    confusion_matrix[row][col] = round(
                        confusion_matrix[row][col],
                        3
                    )

        self._confusion_matrix = confusion_matrix

        self._clear_table()
        self._show_matrix()

    def set_classes(
            self,

            data_set_classes: []):
        """
        - Sets the list with the class names and their identifiers.
        
        :param data_set_classes: List with DataSetClass.
        :return: 
        """

        for id_and_class in data_set_classes:
            if not isinstance(id_and_class, DataSetClass):
                self._kill()

        self._ids_and_classes = data_set_classes

        self._clear_table()
        self._create_columns()

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
