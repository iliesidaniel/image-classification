from graphics.output.save_details_output_f import SaveDetailsOutputF
from graphics.widgets.single_line_output_f import SingleLineOutputF

from utils.train.session_details import SessionDetails

from tkinter import messagebox


import constants.output_constants as const
import sys


class TrainSessSaveDetailsOutputF(SaveDetailsOutputF):

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

        self._lbl_title.config(text=const.TSSD_TITLE_TEXT)

        self._slo_neural_network = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.TSSD_NN_MODEL_TEXT,
            output_text=const.TSSD_NN_MODEL_INITIAL_TEXT
        )

        self._slo_examples_per_batch = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.TSSD_BATCH_SIZE_TEXT,
            output_text=const.TSSD_BATCH_SIZE_INITIAL_TEXT
        )

        self._slo_number_of_epochs = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.TSSD_EPOCHS_NBR_TEXT,
            output_text=const.TSSD_EPOCHS_NBR_INITIAL_TEXT
        )

        self._slo_image_size = SingleLineOutputF(
            parent=self._f_subtitle,

            description_width=const.SD_DESCRIPTION_WIDTH,

            description=const.TSSD_IMAGE_SIZE_TEXT,
            output_text=const.TSSD_IMAGE_SIZE_INITIAL_TEXT
        )

    def _place_widgets(self):

        super()._place_widgets()

        self._slo_neural_network.pack(side='top',
                                      fill='both',
                                      expand=True)

        self._slo_examples_per_batch.pack(side='top',
                                          fill='both',
                                          expand=True)

        self._slo_number_of_epochs.pack(side='top',
                                        fill='both',
                                        expand=True)

        self._slo_image_size.pack(side='top',
                                  fill='both',
                                  expand=True)

    @staticmethod
    def _kill():
        """
        - In case something goes wrong this method displays a message and 
        exits the application.        
        """

        messagebox.showerror(
            title=const.TSSD_ERROR_TITLE,
            message=const.TSSD_ERROR_MSG
        )

        sys.exit(3)

    #########################################################################
    # Public methods

    def update_save_details(
            self,

            train_sess_details: SessionDetails):
        """
        - Updates the session details

        :param train_sess_details: TrainSessionSaveDetails with the 
                                   session's details.
        """

        if not isinstance(train_sess_details, SessionDetails) \
                or not train_sess_details.is_valid():
            self._kill()

        self.update_output_text(
            name=train_sess_details.name,
            description=train_sess_details.description
        )

        self._slo_neural_network.update_output(
            output_text=train_sess_details.neural_network)
        self._slo_examples_per_batch.update_output(
            output_text=train_sess_details.examples_per_batch)
        self._slo_number_of_epochs.update_output(
            output_text=train_sess_details.number_of_epochs)
        self._slo_image_size.update_output(
            output_text=train_sess_details.image_size)

    def enable(self):
        """ Enables all the widgets."""

        self._slo_examples_per_batch.enable()
        self._slo_number_of_epochs.enable()
        self._slo_neural_network.enable()
        self._slo_image_size.enable()
        super().enable()

    def disable(self):
        """ Disables all the widgets."""

        super().disable()
        self._slo_image_size.disable()
        self._slo_neural_network.disable()
        self._slo_number_of_epochs.disable()
        self._slo_examples_per_batch.disable()

    #########################################################################
