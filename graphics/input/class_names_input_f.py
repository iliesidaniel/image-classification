from graphics.widgets.verified_input_list_f import VerifiedInputListF

import constants.input_constants as const
import utils.utils as utils
import tkinter as tk


class ClassNamesInputF(tk.Frame):
    """
    - Use to map indexes to class names.
    - {index} -> class name, where internally index is [0,->), but displayed
    and latter saved [1, ->).
    """

    def __init__(self,

                 parent,

                 valid_input_eh,
                 invalid_input_eh,

                 disabled=False):
        """
        :param parent: Parent.
        
        :param valid_input_eh: Method that will be called when the form is 
                               valid.
        :param invalid_input_eh: Method that will be called when the form is
                                 invalid.
        
        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.CNI_FRAME_PADX,
                          pady=const.CNI_FRAME_PADY,
                          relief='raised',
                          bd=3)

        self._invalid_input_eh = invalid_input_eh
        self._valid_input_eh = valid_input_eh

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):
        """ Creates the widgets."""

        self._lbl_title = tk.Label(
            self,

            padx=const.CNI_TITLE_PADX,
            pady=const.CNI_TITLE_PADY,

            text=const.CNI_TITLE_TEXT,
            font=const.CNI_TITLE_FONT
        )

        self._f_buttons = tk.Frame(
            self,

            padx=const.CNI_WIDGETS_PADX,
            pady=const.CNI_WIDGETS_PADY,
        )

        self._vil_class_name_input = VerifiedInputListF(
            parent=self,

            validation_method=self._check_class_name,

            valid_input_eh=self._valid_input_eh,
            invalid_input_eh=self._invalid_input_eh,

            disabled=False,
            is_set=True
        )

        self._btn_add_new_class = tk.Button(
            self._f_buttons,

            command=self._add_new_class,

            padx=const.CNI_BUTTONS_PADX,
            pady=const.CNI_BUTTONS_PADY,

            text=const.CNI_ADD_BTN_TEXT,
            font=const.CNI_FONT,
            bd=3
        )

        self._btn_delete_last_class = tk.Button(
            self._f_buttons,

            command=self._delete_last_class,

            padx=const.CNI_BUTTONS_PADX,
            pady=const.CNI_BUTTONS_PADY,

            text=const.CNI_DELETE_BTN_TEXT,
            font=const.CNI_FONT,
            bd=3
        )

    def _place_widgets(self):
        """ Places the widgets."""

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._vil_class_name_input.pack(side='top',
                                        fill='both',
                                        expand=True)

        self._f_buttons.pack(fill='both',
                             expand=True)

        self._btn_add_new_class.pack(side='left',
                                     fill='both',
                                     expand=True)
        self._btn_delete_last_class.pack(side='right',
                                         fill='both',
                                         expand=True)

    #########################################################################
    # Event handling

    def _add_new_class(self):
        """
        - Call the required methods to add a new entry.       
        """

        self._vil_class_name_input.add_new_class()

    def _delete_last_class(self):
        """
        - Call the required methods to delete the last entry.        
        """

        self._vil_class_name_input.delete_last_class()

    #########################################################################
    # Validation methods

    @staticmethod
    def _check_class_name(class_name: str):
        """
        - Checks if the class name contains only the allowed characters.
        
        :param class_name: Class name
        
        :return:    - True if the class is valid.
                    - False otherwise.
        """

        return utils.string_is_valid(
            class_name,
            const.CNI_ALLOWED_CHARACTER
        )

    #########################################################################
    # Public methods

    def get_input(self):
        """
        :return: List with the class names. 
        """

        return self._vil_class_name_input.get_input()

    def enable(self):
        """ Enables all the widgets."""

        self._btn_delete_last_class.config(state='normal')
        self._btn_add_new_class.config(state='normal')
        self._lbl_title.config(state='normal')
        self._vil_class_name_input.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._vil_class_name_input.disable()
        self._lbl_title.config(state='disabled')
        self._btn_add_new_class.config(state='disabled')
        self._btn_delete_last_class.config(state='disabled')

    #########################################################################
