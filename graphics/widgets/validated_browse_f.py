from graphics.widgets.validity_indicator_f import ValidityIndicatorF
from graphics.widgets.browse_f import BrowseF

import constants.widget_constants as const
import tkinter as tk


class ValidatedBrowseF(tk.Frame):
    """ 
    - Use to get the path and name of a directory or a file. 
    - If the method "validation_method" returns True the "Valid" indicator 
    will be used, "Invalid" indicator otherwise.
    """

    def __init__(self,

                 parent,

                 no_selection_message: str,
                 user_instruction: str,
                 invalid_message: str,

                 browse_window_title: str,
                 initial_directory: str,
                 supported_files,

                 validation_method,

                 browse_button_eh,

                 directory=False,
                 disabled=False):
        """
        :param parent: Parent.

        :param no_selection_message: Message to display if no directory/file
                                     was selected.
        :param user_instruction: A short message to let the user know what
                                 he has to do.
        :param invalid_message: A short message to let the user know what
                                he did wrong.
        
        :param browse_window_title: Title of the browse window.
        :param initial_directory: Initial search directory.
        :param supported_files: - Supported files (allowed file extensions);
                                - Will be ignored if the directory parameter
                                  is True.

        :param validation_method: Method that will be called to validate the
                                  user input.

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

        # Widget creation
        self._f_browse = BrowseF(
            parent=self,

            no_selection_message=no_selection_message,
            browse_window_title=browse_window_title,
            initial_path=initial_directory,
            user_instruction=user_instruction,
            supported_files=supported_files,

            browse_button_eh=self._browse_btn_pressed,

            directory=directory,
            disabled=disabled
        )

        self._validity_indicator = ValidityIndicatorF(self)

        # Widget placement.
        self._f_browse.pack(side='left',
                            fill='both',
                            expand=True)
        self._validity_indicator.pack(side='right',
                                      fill='both',
                                      expand=False)

        # Saving constructor parameters that will be needed later.
        self._validation_method = validation_method
        self._browse_button_eh = browse_button_eh
        self._invalid_message = invalid_message

        if disabled:
            self.disable()

    #########################################################################
    # Event handling

    def _browse_btn_pressed(
            self,

            path: str):
        """ Automatically called when the user selects a directory/file."""

        self._browse_button_eh(path)

        if self._validation_method(path):
            self._validity_indicator.valid()
        else:
            self._validity_indicator.invalid()
            self._f_browse.update_status(self._invalid_message)

    #########################################################################
    # Public methods

    def enable(self):
        """ Enables all the widgets."""

        self._validity_indicator.enable()
        self._f_browse.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._f_browse.disable()
        self._validity_indicator.disable()

    #########################################################################
