from graphics.input.initial_data_set_picker_f import InitialDataSetPickerF
from graphics.widgets.combobox_input_f import ComboboxInputF

from utils.data_set.initial_data_sets import InitialDataSets

import constants.input_constants as const
import tkinter as tk


class InitialDataSetsPickerF(tk.Frame):
    """
    - Use to get input regarding the data sets that will be used to create 
    the new data set.
    """

    def __init__(self,

                 parent,

                 classes: [],

                 valid_input_eh,
                 invalid_input_eh,

                 disabled=False):
        """
        :param parent: Parent.

        :param classes: Classes.

        :param valid_input_eh: Method that will be called when the form is 
                               completed. 
        :param invalid_input_eh: Method that will be called when the form is 
                                 not completed. 

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.IDSSP_FRAME_PADX,
                          pady=const.IDSSP_FRAME_PADY,
                          relief='raised',
                          bd=3)

        self._invalid_input_eh = invalid_input_eh
        self._valid_input_eh = valid_input_eh
        self._classes = classes

        self._idsp_input = []

        self._create_frames()
        self._place_widgets()

        self._add_idsp()

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_frames(self):
        """ Creates the frames."""

        self._lbl_title = tk.Label(
            self,

            padx=const.IDSSP_TITLE_PADX,
            pady=const.IDSSP_TITLE_PADY,

            text=const.IDSSP_TITLE_TEXT,
            font=const.IDSSP_TITLE_FONT
        )

        self._f_pickers = tk.Frame(
            self,

            relief='sunken',
            bd=3
        )

        self._f_add_picker = tk.Frame(
            self,

            padx=const.IDSSP_WIDGETS_PADX,
            pady=const.IDSSP_WIDGETS_PADY,
        )

        self._f_delete_picker = tk.Frame(
            self,

            padx=const.IDSSP_WIDGETS_PADX,
            pady=const.IDSSP_WIDGETS_PADY,
        )

        self._btn_add_data_set_picker = tk.Button(
            self._f_add_picker,

            padx=const.IDSSP_BUTTON_PADX,
            pady=const.IDSSP_BUTTON_PADY,
            bd=const.IDSSP_BUTTON_BD,

            text=const.IDSSP_ADD_BTN_TEXT,
            command=self._add_idsp_eh,
            font=const.IDSSP_FONT
        )

        self._cb_delete_idsp = ComboboxInputF(
            self._f_delete_picker,

            user_instruction=const.IDSSP_CB_INSTRUCTION_TEXT,
            user_options=[],

            selection_eh=self._idsp_id_delete_selected_eh,
        )

        self._btn_delete = tk.Button(
            self._f_delete_picker,

            padx=const.IDSSP_BUTTON_PADX,
            pady=const.IDSSP_BUTTON_PADY,
            bd=const.IDSSP_BUTTON_BD,

            state='disabled',

            text=const.IDSSP_DELETE_BTN_TEXT,
            command=self._delete_idsp_eh,
            font=const.IDSSP_FONT
        )

    def _place_widgets(self):
        """ Places the widgets."""

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_pickers.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_add_picker.pack(side='top',
                                fill='both',
                                expand=True)

        self._f_delete_picker.pack(side='top',
                                   fill='both',
                                   expand=True)

        self._btn_add_data_set_picker.pack(side='top')

        self._cb_delete_idsp.pack(side='left',
                                  fill='both',
                                  expand=True)

        self._btn_delete.pack(side='right')

    def _add_idsp(self):
        """ 
        - Adds to the _idsp_input lis a new data set picker and displays 
        it."""

        length = len(self._idsp_input)

        self._idsp_input.append(
            InitialDataSetPickerF(
                parent=self._f_pickers,

                picker_id=length + 1,

                classes=self._classes,

                valid_input_eh=self._valid_idsp_form,
                invalid_input_eh=self._invalid_idsp_form
            )
        )

        self._idsp_input[length].pack(side='top',
                                      fill='both',
                                      expand=True)

    #########################################################################
    # Event handling

    def _add_idsp_eh(self):
        """
        - Called when the add new data set button is pressed.
        """

        self._add_idsp()
        self._update_delete_list()
        self._invalid_idsp_form()

    def _delete_idsp_eh(self):
        """
        - Called when the delete button is pressed.
        """

        tmp = self._cb_delete_idsp.get_input()

        if tmp:
            index_to_delete = int(tmp) - 1

            self._idsp_input[index_to_delete].destroy()
            del self._idsp_input[index_to_delete]

            for index in range(index_to_delete, len(self._idsp_input)):
                self._idsp_input[index].update_picker_id(index + 1)

            self._update_delete_list()

            self._check_form_validity()

    def _idsp_id_delete_selected_eh(
            self,

            _):
        """ 
        - Called when the user selects a data set index for deletion.
        - Enables the delete button.
        """

        self._btn_delete.config(state='normal')
        self._btn_delete.flash()

    #########################################################################
    # Helper methods

    def _check_form_validity(self):
        """
        - Checks if the form is valid.
        """

        for idsp in self._idsp_input:
            if not idsp.form_is_valid():
                self._invalid_input_eh()
                return

        self._valid_input_eh()

    def _valid_idsp_form(self):
        """
        - Called when the form is completed.
        """

        self._check_form_validity()

    def _invalid_idsp_form(self):
        """
        - Called when the form is not completed.
        """

        self._invalid_input_eh()

    def _update_delete_list(self):
        """
        - Updates the list with the pickers that can be deleted.
        """

        number_of_pickers = len(self._idsp_input) + 1

        pickers_that_can_be_deleted = []
        for i in range(2, number_of_pickers):
            pickers_that_can_be_deleted.append(i)

        self._cb_delete_idsp.update_options(pickers_that_can_be_deleted)

        self._btn_delete.config(state='disabled')

    #########################################################################
    # Public methods

    def update_classes(
            self,

            classes: []):

        self._classes = classes

        for data_set_picker in self._idsp_input:
            data_set_picker.update_classes(classes=classes)

    def get_input(self):
        """
        :return:    - List with the relations between the new data set 
                    identifier (list index) and the old data set identifier.
                     - [] if the form is not completed.
        """

        data_sets_details = InitialDataSets()

        for data_set in self._idsp_input:
            print(str(data_set))
            data_sets_details.add(new_data_set=data_set.get_input())

        return data_sets_details

    def enable(self):
        """ Enables all the widgets."""

        self._btn_add_data_set_picker.config(state='normal')
        self._lbl_title.config(state='normal')
        self._cb_delete_idsp.enable()

        for entry in self._idsp_input:
            entry.enable()

    def disable(self):
        """ Disables all the widgets."""

        for entry in self._idsp_input:
            entry.disable()

        self._cb_delete_idsp.disable()
        self._lbl_title.config(state='disabled')
        self._btn_delete.config(state='disabled')
        self._btn_add_data_set_picker.config(state='disabled')

    #########################################################################
