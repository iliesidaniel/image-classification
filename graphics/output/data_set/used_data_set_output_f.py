from graphics.output.save_details_output_f import SaveDetailsOutputF
from graphics.widgets.single_line_output_f import SingleLineOutputF

from utils.data_set.data_set_details import DataSetDetails

from tkinter import messagebox


import constants.output_constants as const
import sys


class UsedDataSetOutputF(SaveDetailsOutputF):

    def __init__(self,

                 parent,

                 data_set_index: int,

                 disabled=False):
        """
        :param parent: Parent.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        SaveDetailsOutputF.__init__(self,
                                    parent,
                                    disabled)

        self._data_set_index = data_set_index

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        super()._create_widgets()

        title_text = const.USDO_TITLE_TEXT + str(self._data_set_index)

        self._lbl_title.config(text=title_text)

        self._slo_image_size = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.USDO_IMAGE_SIZE_TEXT,
            output_text=const.USDO_IMAGE_SIZE_INITIAL_TEXT
        )

        self._slo_number_of_files = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.USDO_NUMBER_OF_FILES_TEXT,
            output_text=const.USDO_NUMBER_OF_FILES_INITIAL_TEXT
        )

        self._slo_number_of_examples = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.USDO_NUMBER_OF_EXAMPLES_TEXT,
            output_text=const.USDO_NUMBER_OF_EXAMPLES_INITIAL_TEXT
        )

    def _place_widgets(self):

        super()._place_widgets()

        self._slo_image_size.pack(side='top',
                                  fill='both',
                                  expand=True)

        self._slo_number_of_files.pack(side='top',
                                       fill='both',
                                       expand=True)

        self._slo_number_of_examples.pack(side='top',
                                          fill='both',
                                          expand=True)

    @staticmethod
    def _kill():
        """
        - In case something goes wrong this method displays a message and 
        exits the application.        
        """

        messagebox.showerror(
            title=const.USDO_ERROR_TITLE,
            message=const.USDO_ERROR_MSG
        )

        sys.exit(5)

    #########################################################################
    # Public methods

    def update_save_details(
            self,

            data_set_details: DataSetDetails):
        """
        - Updates the data set details

        :param data_set_details: DataSetSaveDetails with the data set's 
                                 details.
        """

        if not isinstance(data_set_details, DataSetDetails) \
                or not data_set_details.is_valid():
            self._kill()

        self.update_output_text(
            name=data_set_details.name,
            description=data_set_details.description
        )

        self._slo_image_size.update_output(
            output_text=data_set_details.image_size
        )

        self._slo_number_of_files.update_output(
            output_text=str(
                data_set_details.number_of_files
            )
        )

        self._slo_number_of_examples.update_output(
            output_text=data_set_details.number_of_examples
        )

    def enable(self):
        """ Enables all the widgets."""

        self._slo_number_of_examples.enable()
        self._slo_number_of_files.enable()
        self._slo_image_size.enable()
        super().enable()

    def disable(self):
        """ Disables all the widgets."""

        super().disable()
        self._slo_image_size.disable()
        self._slo_number_of_files.disable()
        self._slo_number_of_examples.disable()

    #########################################################################
