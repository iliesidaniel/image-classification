from graphics.widgets.verified_input_f import VerifiedInputF

import file_experts.file_expert as file_expert
import constants.input_constants as const
import tkinter as tk


class FileAndDirectoryNameInputF(tk.Frame):
    """ Use to get user input for the new directory / file name."""

    def __init__(self,
                 parent,

                 file_extension: str,
                 initial_directory_path: str,

                 name_change_eh,

                 file_input=False,
                 disabled=False):
        """
        :param parent: Parent.

        :param file_extension: New file's extension.
        :param initial_directory_path: Initial save directory.

        :param name_change_eh: Method that will be called when the file
                                    name is changed.

        :param file_input:    - Default: False;
                              - True if used to get input for a new file 
                              name.

        :param disabled:    - Default: True;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.FNI_FRAME_PADX,
                          pady=const.FNI_FRAME_PADY)

        self._name_change_eh = name_change_eh
        self._allowed_characters = const.FNI_ALLOWED_CHARACTERS
        self._directory_path = initial_directory_path
        self._file_extension = file_extension
        self._file_input = file_input

        if file_input:
            self._validation_method = self._is_file_name_valid
        else:
            self._validation_method = self._is_directory_name_valid

        self._create_widgets()
        self._place_widgets()

        self._file_name = ''

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):
        """ Creates the widgets."""

        self._f_user_information = tk.Frame(
            self,
            padx=const.FNI_WIDGETS_PADX,
            pady=const.FNI_WIDGETS_PADY
        )

        self._lbl_user_instruction = tk.Label(
            self._f_user_information,
            text=const.FNI_USER_INSTRUCTION,
            font=const.FNI_L_FONT
        )

        self._lbl_allowed_characters = tk.Label(
            self._f_user_information,
            text=const.FNI_ALLOWED_MSG,
            font=const.FNI_S_FONT
        )

        self._vi_name_input = VerifiedInputF(
            parent=self,

            validation_method=self._validation_method,

            valid_input_eh=self._name_changed_eh,
            invalid_input_eh=self._name_changed_eh,

            disabled=True
        )

        if self._file_input:
            self._lbl_file_extension = tk.Label(
                self,

                padx=const.FNI_WIDGETS_PADX,
                pady=const.FNI_WIDGETS_PADY,
                text=self._file_extension,
                font=const.FNI_S_FONT
            )

    def _place_widgets(self):
        """ Places the widgets."""

        self._lbl_user_instruction.pack(side='top',
                                        fill='both',
                                        expand=True)
        self._lbl_allowed_characters.pack(side='top',
                                          fill='both',
                                          expand=True)
        self._f_user_information.pack(side='left',
                                      fill='both',
                                      expand=True)

        self._vi_name_input.pack(side='left',
                                 fill='both',
                                 expand=True)

        if self._file_input:
            self._lbl_file_extension.pack(side='left',
                                          fill='both',
                                          expand=True)

    #########################################################################
    # Event handling

    def _name_changed_eh(self):
        """ 
        - Automatically called when the user changes the desired name.
        """

        self._file_name = self._vi_name_input.get_input()
        new_file_name = self.get_name()

        self._name_change_eh(new_file_name)

    #########################################################################
    # Validation methods

    def _is_file_name_valid(
            self,

            file_name: str):
        """ 
        - Checks if the file name is valid.
        - A file name is valid if it contains only the allowed
        characters, the save location exists and does not contain a
        file with the same name and extension.

        :return:    - True if the file name is valid;
                    - False otherwise.
        """

        rez = file_expert.is_file_name_valid(
            allowed_characters=const.FNI_ALLOWED_CHARACTERS,
            directory_path=self._directory_path,
            file_extension=self._file_extension,
            file_name=file_name
        )

        return rez

    def _is_directory_name_valid(
            self,

            directory_name: str):
        """ 
        - Checks if the directory name is valid.
        - A directory name is valid if it contains only the allowed
        characters, the save location exists and does not contain a
        directory with the same name.

        :return:    - True if the directory name is valid;
                    - False otherwise.
        """

        rez = file_expert.is_directory_name_valid(
            allowed_characters=const.FNI_ALLOWED_CHARACTERS,
            directory_path=self._directory_path,
            directory_name=directory_name
        )

        return rez

    #########################################################################
    # Public methods

    def change_directory_path(
            self,
            new_directory_path: str):
        """ Changes the save location.

        :param new_directory_path: New save directory.
        """

        self._directory_path = new_directory_path
        self._vi_name_input.check_input()

    def change_file_extension(
            self,
            new_file_extension: str):
        """ Changes the file extension.

        :param new_file_extension: New file extension.
        """

        if self._file_input:
            self._file_extension = new_file_extension
            self._lbl_file_extension.config(text=self._file_extension)

            self._vi_name_input.check_input()

    def get_name(self):
        """ Returns the file/directory name if it's valid, '' otherwise.

        :return:    - File/Directory name if it is valid;
                    - '' otherwise.
        """

        name = self._vi_name_input.get_input()

        if self._file_input and self._is_file_name_valid(name):
            return name

        if not self._file_input and self._is_directory_name_valid(name):
            return name

        return ''

    def enable(self):
        """ Enables all the widgets."""

        if self._file_input:
            self._lbl_file_extension.config(state='normal')

        self._lbl_allowed_characters.config(state='normal')
        self._lbl_user_instruction.config(state='normal')
        self._vi_name_input.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._vi_name_input.disable()
        self._lbl_user_instruction.config(state='disabled')
        self._lbl_allowed_characters.config(state='disabled')

        if self._file_input:
            self._lbl_file_extension.config(state='disabled')

    #########################################################################
