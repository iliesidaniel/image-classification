from graphics.input.file_and_directory_name_input_f import FileAndDirectoryNameInputF
from graphics.widgets.multiline_input_f import MultilineInputF
from graphics.widgets.browse_f import BrowseF

from utils.new_file_details import NewFileDetails

from copy import deepcopy


import constants.input_constants as const
import file_experts.file_expert as fe
import tkinter as tk


class FileSaveDetailsInputF(tk.Frame):
    """ Use to get input for a new file (path and name)."""

    def __init__(self,

                 parent,

                 file_extension: str,

                 valid_input_eh,
                 invalid_input_eh,

                 disabled=False):
        """
        :param parent: Parent.

        :param file_extension: File's extension.

        :param valid_input_eh: Method that will be called when the input is 
                               valid.
        :param invalid_input_eh: Method that will be called when the input is
                                 invalid.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.SDI_FRAME_PADX,
                          pady=const.SDI_FRAME_PADY,
                          relief='raised',
                          bd=3)

        self._invalid_input_eh = invalid_input_eh
        self._valid_input_eh = valid_input_eh
        self._file_extension = file_extension

        self._file_input = NewFileDetails()

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

            justify='left',

            padx=const.SDI_TITLE_PADX,
            pady=const.SDI_TITLE_PADY,

            text=const.SDI_TITLE_TEXT,
            font=const.SDI_TITLE_FONT
        )

        self._f_main_frame = tk.Frame(
            self,

            relief=const.SDI_WIDGETS_RELIEF,
            padx=const.SDI_WIDGETS_PADX,
            pady=const.SDI_WIDGETS_PADY,
            bd=const.SDI_WIDGETS_BD
        )

        self._f_browse = BrowseF(
            parent=self._f_main_frame,

            initial_path=const.SDI_BF_INITIAL_DIRECTORY,
            no_selection_message=const.SDI_BF_NO_SELECTION,
            user_instruction=const.SDI_BF_USER_INSTRUCTION,
            browse_window_title=const.SDI_BF_WINDOW_TITLE,

            browse_button_eh=self._directory_path_changed_eh,

            supported_files=None,
            directory=True)

        self._f_name_input = FileAndDirectoryNameInputF(
            parent=self._f_main_frame,

            initial_directory_path=const.SDI_BF_INITIAL_DIRECTORY,
            file_extension=self._file_extension,

            name_change_eh=self._file_name_changed_eh,

            disabled=True
        )

        self._description = MultilineInputF(
            parent=self._f_main_frame,

            user_instruction=const.SDI_FNI_DESCRIPTION_TEXT,
            input_changed_eh=self._description_changed_eh,

            disabled=True
        )

    def _place_widgets(self):
        """ Places the widgets."""

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_browse.pack(side='top',
                            fill='both',
                            expand=True)
        self._f_name_input.pack(side='top',
                                fill='both',
                                expand=True)
        self._description.pack(side='top',
                               fill='both',
                               expand=True)

        self._f_main_frame.pack(side='top',
                                fill='both',
                                expand=True)

    #########################################################################
    # Event handling

    def _directory_path_changed_eh(
            self,

            directory_path: str):
        """ Automatically called when the directory is changed.

        :param directory_path: Path of the new directory.
        """

        self._f_name_input.change_directory_path(directory_path)

        if isinstance(directory_path, str) \
                and directory_path != '' \
                and fe.is_directory(directory_path):
            self._file_input.directory_path = directory_path
            self._f_name_input.enable()

            # If the user completed the form but at some point the directory
            # was no longer valid but now it is. This will trigger the file
            # name change event handler.
            if self._file_input.file_name != '':
                self._file_name_changed_eh(self._file_input.file_name)
        else:
            self._file_input.directory_path = ''

            self._f_name_input.disable()
            self._description.disable()

            self._invalid_input_eh()

    def _file_name_changed_eh(
            self,

            new_file_name: str):
        """ Automatically called when the file name is changed.

        :param new_file_name: New file name.
        """

        self._file_input.file_name = new_file_name

        # A file name is valid if it is not '', if you want to see why check
        # FileNameInputF.
        if new_file_name != '':
            # If the file name is valid.
            self._description.enable()

            # If the user completed the form but at some point the file name
            # was no longer valid but now it is. This will enable the
            # description input form and also call the valid input event
            # handler.
            if self._file_input.description != '':
                self._description.enable()
                self._valid(self._file_input)
        else:
            # If the file name is invalid.
            self._description.disable()
            self._invalid()

    def _description_changed_eh(
            self,

            description):
        """
        - Called when the user changes the description.

        :param description: New description.
        """

        if description != '':
            self._file_input.description = description

            self._valid(self.get_new_file_details())
        else:
            self._file_input.description = ''

            self._invalid()

    def _valid(self, param):
        """
        - Called when the input details for the data set are valid.

        :param param: Parameter to send to the valid event handler.
        """

        self._valid_input_eh(param)

    def _invalid(self):
        """
        - Called when the input details for the data set are invalid.
        """

        self._invalid_input_eh()

    #########################################################################
    # Public methods

    def change_file_extension(
            self,

            new_file_extension: str):
        """ Call this method to changed the file extension.

        :param new_file_extension: New file extension.
        """

        self._file_extension = new_file_extension
        self._f_name_input.change_file_extension(
            new_file_extension)

    def get_new_file_details(self):
        """ Returns the input for path and file name.

        :return: (directory path, file name)
        """

        return deepcopy(self._file_input)

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_title.config(state='normal')
        self._f_name_input.enable()
        self._description.enable()
        self._f_browse.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._f_browse.disable()
        self._description.disable()
        self._f_name_input.disable()
        self._lbl_title.config(state='disabled')

    #########################################################################
