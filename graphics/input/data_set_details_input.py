from graphics.input.file_save_details_input_f import FileSaveDetailsInputF
from graphics.input.number_in_range_input_f import NumberInRangeInputF


import constants.global_constants as const


class DataSetDetailsInput(FileSaveDetailsInputF):

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

        FileSaveDetailsInputF.__init__(
            self,
            parent,
            file_extension,
            valid_input_eh,
            invalid_input_eh,
            disabled)

        self._image_size_input = NumberInRangeInputF(
            parent=self._f_main_frame,

            user_instruction='Image size',

            value_changed_eh=self._do_nothing,

            min_val=const.IMAGE_SIZE_MIN,
            max_val=const.IMAGE_SIZE_MAX,
            increment=const.IMAGE_SIZE_INCREASE_STEP,

            integer=True,

            disabled=True
        )

        self._number_of_files_input = NumberInRangeInputF(
            parent=self._f_main_frame,

            user_instruction='Number of files',

            value_changed_eh=self._do_nothing,

            min_val=1,
            max_val=20,
            increment=1,

            integer=True,

            disabled=True
        )

        self._image_size_input.pack(side='top',
                                    fill='both',
                                    expand=True)
        self._number_of_files_input.pack(side='top',
                                         fill='both',
                                         expand=True)

    #########################################################################
    # Auxiliary methods

    def _do_nothing(self):

        pass

    def _valid(self, param):
        """
        - Called when the input details for the data set are valid.
        
        :param param: Parameter to send to the valid event handler.
        """

        super(DataSetDetailsInput, self)._valid(param)

        self._number_of_files_input.enable()
        self._image_size_input.enable()

    def _invalid(self):
        """
        - Called when the input details for the data set are invalid.
        """

        super(DataSetDetailsInput, self)._invalid()

        self._number_of_files_input.disable()
        self._image_size_input.disable()

    #########################################################################
    # Public methods

    # ~~~~~~~~~~~~~~~~~~~~~Image size~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def get_image_size(self):
        """
        - Returns the image size.
        """

        return self._image_size_input.get_number()

    # ~~~~~~~~~~~~~~~~~~~~~Number of files~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def get_number_of_files(self):
        """
        - Returns the number of files.
        """

        return self._number_of_files_input.get_number()

    # ~~~~~~~~~~~~~~~~~~~~~Enable / disable~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def enable(self):
        """ Enables all the widgets."""

        super(DataSetDetailsInput, self).enable()
        self._number_of_files_input.enable()
        self._image_size_input.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._image_size_input.disable()
        self._number_of_files_input.disable()
        super(DataSetDetailsInput, self).disable()

    #########################################################################
