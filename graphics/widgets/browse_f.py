from tkinter import filedialog

import constants.widget_constants as const
import tkinter as tk


class BrowseF(tk.Frame):
    """ Use to get the path and name of a directory or a file."""

    def __init__(self,
                 parent,

                 user_instruction: str,
                 no_selection_message: str,
                 initial_path: str,
                 supported_files,
                 browse_window_title: str,

                 browse_button_eh,

                 directory=False,
                 disabled=False):
        """
        :param parent: Parent.

        :param user_instruction: A short message to let the user know what
                                 he has to do.
        :param no_selection_message: Message to display if no directory/file
                                     was selected.
        :param initial_path: Initial path.
        :param supported_files: - Supported files (allowed file extensions);
                                - Will be ignored if the directory parameter
                                  is True.
        :param browse_window_title: Title of the browse window.

        :param browse_button_eh: Method that will be called when the user
                                    selects a directory/file.

        :param directory:   - Default: False;
                            - True to search for a directory;
                            - False to search for a file.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.BF_FRAME_PADX,
                          pady=const.BF_FRAME_PADY)

        self._get_directory = directory

        self._no_selection_message = no_selection_message
        self._browse_window_title = browse_window_title
        self._browse_button_event = browse_button_eh
        self._user_instruction = user_instruction
        self._supported_files = supported_files
        self._initial_path = initial_path

        self._selected_path = ''

        self._create_and_place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_and_place_widgets(self):
        """ Creates the frames."""

        self._f_messages = tk.Frame(
            self,
            padx=const.BF_LABEL_FRAME_PADX,
            pady=const.BF_LABEL_FRAME_PADY
        )

        self._lbl_user_instruction = tk.Label(
            self._f_messages,
            font=const.BF_INSTRUCTION_FONT,
            text=self._user_instruction
        )

        self._lbl_status = tk.Label(
            self._f_messages,
            font=const.BF_FILE_INFO_FONT,
            text=self._no_selection_message
        )

        self._btn_browse = tk.Button(
            self,
            font=const.BF_BROWSE_BUTTON_FONT,
            text=const.BF_BUTTON_TEXT,
            command=self._button_pressed
        )

        self._lbl_user_instruction.pack(side='top',
                                        fill='both',
                                        expand=True)
        self._lbl_status.pack(side='bottom',
                              fill='both',
                              expand=True)

        self._f_messages.pack(side='left',
                              fill='both',
                              expand=True)
        self._btn_browse.pack(side='right',
                              fill='both',
                              expand=True)

    #########################################################################
    # Event handling

    def _button_pressed(self):
        """ Automatically called when the user selects a directory/file."""

        if self._get_directory:
            self._get_directory_path()
        else:
            self._get_file_path()

    #########################################################################
    # Methods for browsing files

    def _get_file_path(self):
        """ Opens the browse window and calls the method provided by the
        browse_button_event parameter passing the path and the name of the
        selected file.
        """

        self._selected_path = filedialog.askopenfilename(
            initialdir=self._initial_path,
            filetypes=self._supported_files,
            title=self._browse_window_title
        )

        self._validate_selection(self._update_file_status)

    def _update_file_status(self):
        """ Displays the parent directory and the name of the selected
        file.
        """

        if self._selected_path != '':
            parsed_file_name = self._selected_path.split('/')
            len_parsed = len(parsed_file_name)

            new_file_info = '../' + parsed_file_name[len_parsed - 2]
            new_file_info += '/' + parsed_file_name[len_parsed - 1]

            self._update_status(new_status=self._selected_path,
                                internal_call=True)

    #########################################################################
    # Methods for browsing directories

    def _get_directory_path(self):
        """ Opens the browse window and calls the method provided by the
        browse_button_event parameter passing the path of the selected
        directory.
        """

        self._selected_path = filedialog.askdirectory(
            initialdir=self._initial_path,
            title=self._browse_window_title
        )

        self._validate_selection(self._update_directory_status)

    def _update_directory_status(self):
        """ Displays information about the selected directory."""

        if self._selected_path != '':
            self._update_status(new_status=self._selected_path,
                                internal_call=True)

    #########################################################################
    # Auxiliary methods

    def _validate_selection(
            self,

            method_to_call_when_valid):
        """ 
        - Checks if the selection is valid.
        """

        if isinstance(self._selected_path, str) \
                and self._selected_path != '':
            method_to_call_when_valid()

            self._browse_button_event(self._selected_path)

    def _update_status(
            self,

            new_status,

            internal_call=False):
        """ 
        - Created for ValidatedBrowseF to be used when the user input is 
        invalid.
        - Since the status label is updated automatically after the user 
        selects a file/directory you don't have to use this method. For an
        example check ValidatedBrowseF._browse_btn_pressed.
        """

        if new_status != '' or not internal_call:
            self._lbl_status.config(text=new_status)
        else:
            self._lbl_status.config(text=self._initial_path)

    #########################################################################
    # Public methods

    def update_status(
            self,

            new_status):
        """ 
        - Created for ValidatedBrowseF to be used when the user input is 
        invalid.
        - Since the status label is updated automatically after the user 
        selects a file/directory you don't have to use this method. For an
        example check ValidatedBrowseF._browse_btn_pressed.
        """

        self._update_status(new_status=new_status)

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_user_instruction.config(state='normal')
        self._lbl_status.config(state='normal')
        self._btn_browse.config(state='normal')

    def disable(self):
        """ Disables all the widgets."""

        self._btn_browse.config(state='disabled')
        self._lbl_status.config(state='disabled')
        self._lbl_user_instruction.config(state='disabled')

    #########################################################################
