from utils.data_set.classes_correlation_between_data_sets import ClassesCorrelationBetweenDataSets
from utils.data_set.class_correlation_between_data_sets import ClassCorrelationBetweenDataSets

from graphics.widgets.combobox_input_f import ComboboxInputF

from tkinter import messagebox
from copy import deepcopy

import constants.input_constants as const
import tkinter as tk
import sys


class ClassIdentifiersInputF(tk.Frame):
    """
    - Use to correlate class names and the identifiers in the old data set.  
    """

    def __init__(self,

                 parent,

                 valid_input_eh,
                 invalid_input_eh,

                 disabled=False):
        """
        :param parent: Parent

        :param valid_input_eh: Method that will be called when the form is 
                               completed.
        :param invalid_input_eh: Method that will be called after each user 
                                 input if the form is not/no longer 
                                 completed.
            
        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """
        tk.Frame.__init__(self,
                          parent,
                          relief=const.CII_FRAME_RELIEF,
                          padx=const.CII_FRAME_PADX,
                          pady=const.CII_FRAME_PADY,
                          bd=const.CII_FRAME_BD)

        self._invalid_input_eh = invalid_input_eh
        self._valid_input_eh = valid_input_eh

        self._number_of_classes = 0
        self._current_entry = 0

        self._correlations = ClassesCorrelationBetweenDataSets()

        self._ci_correlations_input = []
        self._identifiers_left = []
        self._identifiers = []
        self._classes = []

        self._lbl_title = tk.Label(
            self,

            padx=const.CII_TITLE_PADX,
            pady=const.CII_TITLE_PADY,

            text=const.CII_TITLE_TEXT,
            font=const.CII_TITLE_FONT
        )

        self._f_main_frame = tk.Frame(
            self,

            relief=const.CII_WIDGETS_RELIEF,
            padx=const.CII_WIDGETS_PADX,
            pady=const.CII_WIDGETS_PADY,
            bd=const.CII_WIDGETS_BD
        )

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_main_frame.pack(side='top',
                                fill='both',
                                expand=True)

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _add_new_entry(
            self,

            class_name: str):
        """
        - Adds and displays a new input entry.
        """

        length = len(self._ci_correlations_input)

        number_of_identifiers = len(self._identifiers)
        number_of_classes = len(self._classes)

        if number_of_classes == number_of_identifiers:
            self._ci_correlations_input.append(
                ComboboxInputF(
                    parent=self._f_main_frame,

                    user_instruction=class_name,
                    user_options=self._identifiers_left,

                    selection_eh=self._identifier_selected,

                    disabled=False
                )
            )

            # Widget placement
            self._ci_correlations_input[length].pack(side='top',
                                                     fill='x',
                                                     expand=True)

    #########################################################################
    # Event handling

    def _identifier_selected(
            self,

            old_identifier: str):
        """
        - Called when an identifier was selected for the last displayed 
        class.

        :param old_identifier: Initial data set identifier.
        """

        self.disable()

        if self._current_entry < self._number_of_classes:
            new_identifier = self._current_entry

            new_correlation = ClassCorrelationBetweenDataSets()
            new_correlation.identifier_in_new_data_set = new_identifier
            new_correlation.identifier_in_old_data_set = old_identifier

            self._correlations.add(new_correlation=new_correlation)

            self._update_list_of_identifiers_left_for_selection(old_identifier)
            self._current_entry = self._current_entry + 1

            if self._current_entry != self._number_of_classes:
                self._add_new_entry(self._classes[self._current_entry])

                self._invalid_input_eh()
            else:
                self._valid_input_eh()
        else:
            messagebox.showerror(
                title=const.CII_ERROR_TITLE,
                message=const.CII_ERROR_MSG
            )
            sys.exit(1)

    def _update_list_of_identifiers_left_for_selection(
            self,

            selected_identifier: str):
        """
        - Removes the selected identifier from the list of the identifiers 
        left to be selected.
        
        :param selected_identifier: Selected identifier for the last 
                                    displayed class. 
        """

        for index in range(len(self._identifiers_left)):
            if self._identifiers_left[index] == selected_identifier:
                del self._identifiers_left[index]
                break

    def _delete_entries(self):
        """
        - Destroys all input entries.          
        """

        for entry in self._ci_correlations_input:
            entry.destroy()

        self._ci_correlations_input = []

        del self._correlations
        self._correlations = ClassesCorrelationBetweenDataSets()

    #########################################################################
    # Public methods

    def get_input(self):
        """
        :return:    - List with the relations between the new data set 
                    identifier (list index) and the old data set identifier.
                     - [] if the form is not completed.
        """

        if self._current_entry == self._number_of_classes:
            return self._correlations
        else:
            return ClassesCorrelationBetweenDataSets()

    def update_classes(
            self,

            class_names: []):
        """
        - Call to update the list with the class names.
        """

        self._delete_entries()

        self._number_of_classes = len(class_names)

        self._identifiers_left = deepcopy(self._identifiers)
        self._classes = class_names
        self._current_entry = 0

        number_of_classes = len(class_names)
        number_of_identifiers = len(self._identifiers)

        if number_of_identifiers != 0 \
                and number_of_classes != 0:
            self._add_new_entry(self._classes[0])

    def update_data_set_identifier(
            self,

            identifiers: []):
        """
        - Call to update the list with the identifiers.
        """

        if len(identifiers) != 0 and len(self._classes) != 0:
            if self._number_of_classes < len(identifiers):
                messagebox.showerror(
                    title='Wrong input',
                    message='The data set you selected has a different '
                            'number of classes.\n\n'
                            'Please add more classes to the new data set and'
                            ' try again OR select another data set.'
                )

                # TODO raise ValueError
            elif self._number_of_classes > len(identifiers):
                messagebox.showerror(
                    title='Wrong input',
                    message='The data set you selected has a different '
                            'number of classes.\n\n'
                            'Please remove classes from the new data set and'
                            ' try again OR select another data set.'
                )

                # TODO raise ValueError
            else:
                self._delete_entries()

                self._identifiers_left = deepcopy(identifiers)
                self._identifiers = deepcopy(identifiers)

                self._current_entry = 0

                self._add_new_entry(self._classes[0])

    def enable(self):
        """
        - Enables the title label.
        - Enables the last displayed entry IF it's not the entry for the 
        last class. 
        """

        if len(self._ci_correlations_input) != 0 \
                and len(self._identifiers_left) != 0:
            self._ci_correlations_input[-1].enable()

        self._lbl_title.config(state='normal')

    def disable(self):
        """
        - Disables the title label.
        - Disables the last entry. 
        """

        if len(self._ci_correlations_input) != 0:
            self._ci_correlations_input[-1].disable()

        self._lbl_title.config(state='disabled')

    #########################################################################
