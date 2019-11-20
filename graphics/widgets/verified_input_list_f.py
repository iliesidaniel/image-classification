from graphics.widgets.scrollable_canvas_c import ScrollableCanvasC
from graphics.widgets.verified_input_f import VerifiedInputF

import constants.widget_constants as const
import tkinter as tk


class VerifiedInputListF(tk.Frame):
    """
    - Use to map index to a string.
    - Displayed value of the index is: index + 1.
    - If the list is a set, set the is_set parameter to True.
    """

    def __init__(self,

                 parent,

                 validation_method,

                 valid_input_eh,
                 invalid_input_eh,

                 disabled=False,
                 is_set=False,

                 input_entry_width=const.VIF_NBR_OF_INPUT_CHARS):
        """
        :param parent: Parent.

        :param validation_method: Method that will be called to validate 
                                  class name entry. 

        :param valid_input_eh: Method that will be called wen all the entries
                               are valid.
        :param invalid_input_eh: Method that will be called wen at least one
                                 of the entries is invalid.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        :param is_set:  - Default: False;
                        - True if the list is a set;
                        - False otherwise.
        """

        tk.Frame.__init__(self,
                          parent,

                          relief=const.VI_SUBFRAME_RELIEF,
                          padx=const.VI_SUBFRAME_PADX,
                          pady=const.VI_SUBFRAME_PADY,
                          bd=const.VI_SUBFRAME_BD)

        self._validation_method = validation_method
        self._input_entry_width = input_entry_width
        self._invalid_input_eh = invalid_input_eh
        self._valid_input_eh = valid_input_eh
        self._is_set = is_set

        self._input_list = []
        self._set_valid = []
        self._vi_input = []
        self._frames = []
        self._labels = []
        self._valid = []

        self._sc_scrollable = ScrollableCanvasC(
            parent=self,

            height=const.VI_SCROLL_REGION_HEIGHT,
        )

        self._sc_scrollable.pack(side='top',
                                 fill='both',
                                 expand=True)

        self._add_new_entry()

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _add_new_entry(self):
        """
        - Adds a new entry.
        """

        length = len(self._vi_input)
        identifier = str(length + 1)

        self._set_valid.append(False)
        self._valid.append(False)
        self._input_list.append('')

        # Widget creation
        self._frames.append(
            tk.Frame(
                self._sc_scrollable.f_main_frame,
            )
        )

        self._labels.append(
            tk.Label(
                self._frames[length],

                font=const.VIF_FONT,

                text=identifier
            )
        )

        self._vi_input.append(
            VerifiedInputF(
                parent=self._frames[length],

                validation_method=self._validation_method,

                form_id=length,

                valid_input_eh=self._valid_entry,
                invalid_input_eh=self._invalid_entry,

                disabled=False
            )
        )

        # Widget placement
        self._frames[length].pack(side='top',
                                  fill='x',
                                  expand=False)

        self._labels[length].pack(side='left',
                                  fill='x',
                                  expand=True)

        self._vi_input[length].pack(side='right',
                                    fill='x',
                                    expand=True)

        # Call the validation method
        self._check_validity()

    def _delete_last_entry(self):
        """
        - Deletes the last entry.
        """

        length = len(self._vi_input) - 1

        if length > 0:  # Making sure there is at least one entry.

            # Destroying the widgets for the last entry.
            self._vi_input[length].destroy()
            self._labels[length].destroy()
            self._frames[length].destroy()

            # Removing the entry data from all the lists.
            self._set_valid.pop()
            self._vi_input.pop()
            self._frames.pop()
            self._labels.pop()
            self._valid.pop()
            self._input_list.pop()

        self._check_validity()

    #########################################################################
    # Event handling

    def _valid_entry(
            self,

            entry_id: int):
        """
        - Called if the entry is valid.
        - If the parameter is_set is True this method also checks for 
        duplicates.

        :param entry_id: Entry id
        """

        self._input_list[entry_id] = self._vi_input[entry_id].get_input()
        self._vi_input[entry_id].valid()
        self._valid[entry_id] = True

        if self._is_set:
            self._invalidate_duplicates()

        self._check_validity()

    def _invalid_entry(
            self,

            entry_id: int):
        """
        - Called if the entry is invalid.

        :param entry_id: Entry id
        """

        self._vi_input[entry_id].invalid()
        self._valid[entry_id] = False

        self._check_validity()

    #########################################################################
    # Validation methods

    def _check_validity(self):
        """
        - Calls the event handler accordingly with the form validity state.
        """

        if self.form_is_valid():
            self._valid_input_eh()
        else:
            self._invalid_input_eh()

    def _invalidate_duplicates(self):
        """
        - Invalidates all duplicates.
        """

        # Setting all _set_valid elements to True to make sure only the valid
        # duplicates will have their state set to "Invalid".
        for entry_id in range(len(self._input_list)):
            if self._valid[entry_id]:
                self._vi_input[entry_id].valid()
                self._set_valid[entry_id] = True

        for entry_id in range(len(self._input_list) - 1):
            matches_list = []
            matches = 0

            for index in range(len(self._input_list)):
                entry = self._input_list[index]

                if entry == self._input_list[entry_id]:
                    matches = matches + 1
                    matches_list.append(index)

            if matches != 1:    # If the element is duplicated.
                # Setting the state for all duplicates to "Invalid".
                for index_match in matches_list:
                    self._vi_input[index_match].invalid()
                    self._set_valid[index_match] = False

    #########################################################################
    # Public methods

    def form_is_valid(self):
        """
        - Checks if all the entries are valid.

        :return:    - True if all the entries are valid;
                    - False otherwise.
        """

        for entry_id in range(len(self._input_list)):
            if not self._valid[entry_id]:
                return False

            # If is_set parameter was set to True this checks if the list is
            # a set.
            if self._is_set and not self._set_valid[entry_id]:
                return False

        return True

    def add_new_class(self):
        """ Call this method to add a new entry."""

        self._add_new_entry()

    def delete_last_class(self):
        """ Call this method to delete the last entry."""

        self._delete_last_entry()

    def get_input(self):
        """
        :return:    - List with the user input. 
                    - If the form is not valid it will return [].
        """

        if self.form_is_valid():
            return self._input_list
        else:
            return []

    def enable(self):
        """ Enables all the widgets."""

        for index in range(len(self._vi_input)):
            self._labels[index].config(state='normal')
            self._vi_input[index].enable()

    def disable(self):
        """ Disables all the widgets."""

        for index in range(len(self._vi_input)):
            self._labels[index].config(state='disabled')
            self._vi_input[index].disable()

    #########################################################################
