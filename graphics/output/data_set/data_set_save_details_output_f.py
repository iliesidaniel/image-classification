from graphics.widgets.single_line_output_f import SingleLineOutputF
from graphics.output.save_details_output_f import SaveDetailsOutputF
from graphics.output.classes_output import ClassesOutputF

from utils.data_set.data_set_details import DataSetDetails

from tkinter import messagebox


import constants.output_constants as const
import sys


class DataSetSaveDetailsOutputF(SaveDetailsOutputF):

    def __init__(self,

                 parent,

                 disabled=False):
        """
        :param parent: Parent.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        SaveDetailsOutputF.__init__(self,
                                    parent,
                                    disabled)

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget handling

    def _create_widgets(self):

        super()._create_widgets()

        self._lbl_title.config(text=const.DSDO_TITLE_TEXT)

        self._slo_examples = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.DSDO_EXAMPLES_NBR_TEXT,
            output_text=const.DSDO_EXAMPLES_NBR_INITIAL_TEXT
        )

        self._slo_classes_nbr = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.DSDO_CLASSES_NBR_TEXT,
            output_text=const.DSDO_CLASSES_NBR_INITIAL_TEXT
        )

        self._slo_image_size = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.DSDO_IMAGE_SIZE_TEXT,
            output_text=const.DSDO_IMAGE_SIZE_INITIAL_TEXT
        )

        self._classes_output = ClassesOutputF(
            parent=self._f_subtitle,
        )

        self._classes_output.config(relief='flat')

    def _place_widgets(self):

        super()._place_widgets()

        self._slo_examples.pack(side='top',
                                fill='both',
                                expand=True)

        self._slo_classes_nbr.pack(side='top',
                                   fill='both',
                                   expand=True)

        self._slo_image_size.pack(side='top',
                                  fill='both',
                                  expand=True)

        self._classes_output.pack(side='top',
                                  fill='both',
                                  expand=True)

    @staticmethod
    def _kill():
        """
        - In case something goes wrong this method displays a message and 
        exits the application.        
        """

        messagebox.showerror(
            title=const.DSDO_ERROR_TITLE,
            message=const.DSDO_ERROR_MSG
        )

        sys.exit(4)

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

        classes = data_set_details.classes

        number_of_classes = len(classes.get_data_set_classes())

        self._slo_examples.update_output(
            output_text=data_set_details.number_of_examples)
        self._slo_classes_nbr.update_output(
            output_text=str(number_of_classes))
        self._slo_image_size.update_output(
            output_text=data_set_details.image_size)

        self._classes_output.update_classes(data_set_details.classes)

    def enable(self):
        """ Enables all the widgets."""

        self._slo_examples.enable()
        self._slo_classes_nbr.enable()
        super().enable()

    def disable(self):
        """ Disables all the widgets."""

        super().disable()
        self._slo_classes_nbr.disable()
        self._slo_examples.disable()

    #########################################################################
