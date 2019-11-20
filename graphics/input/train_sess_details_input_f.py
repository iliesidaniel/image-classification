from utils.train.session_details import SessionDetails

from graphics.widgets.combobox_input_f import ComboboxInputF
from graphics.widgets.browse_f import BrowseF


import constants.train_sess_constants as const
import tkinter as tk


class TrainSessDetailsInputF(tk.Frame):
    """
    - Use to get user input regarding the details of a new training session.
    """

    def __init__(self,

                 parent,

                 valid_input_eh,
                 invalid_input_eh,

                 disabled=False,
                 k_fold_cv_session=False):
        """
        :param parent: Parent.

        :param valid_input_eh: Method that will be called when the form is 
                               completed. 
        :param invalid_input_eh: Method that will be called when the form is 
                                 not completed after the user made a change.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.

        :param k_fold_cv_session:   - Default: False;
                                    - True if this is used for a K-fold 
                                    cross-validation session.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.TSDI_FRAME_PADX,
                          pady=const.TSDI_FRAME_PADY)

        self._invalid_input_eh = invalid_input_eh
        self._valid_input_eh = valid_input_eh

        self._k_fold_cv_session = k_fold_cv_session

        self._create_widgets()
        self._place_widgets()

        self._sess_details = SessionDetails(
            k_fold_cv_session=k_fold_cv_session
        )

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):

        self._lbl_title = tk.Label(
            self,

            text=const.TSDI_INSTRUCTION,
            font=const.TSDI_FONT,
            justify='left'
        )

        self._f_browse = BrowseF(
            parent=self,

            initial_path=const.TSDI_BF_INITIAL_DIRECTORY,
            no_selection_message=const.TSDI_BF_NO_SELECTION,
            user_instruction=const.TSDI_BF_USER_INSTRUCTION,
            browse_window_title=const.TSDI_BF_WINDOW_TITLE,

            browse_button_eh=self._data_set_selected_eh,

            supported_files=const.TSDI_FILE_EXTENSION,

            directory=False,
            disabled=False
        )

        # TODO

        """
        from graphics.output.data_set.data_set_save_details_output_f import DataSetSaveDetailsOutputF

        self._selected_data_set_details = DataSetSaveDetailsOutputF(
            ...........
        )
        """

        self._cbi_nn_model = ComboboxInputF(
            parent=self,

            user_instruction=const.TSDI_NN_MODEL_INSTRUCTION,
            user_options=const.TSDI_NN_MODEL_OPTIONS,

            selection_eh=self._neural_network_selected_eh,

            disabled=False
        )

        self._cbi_batch_size = ComboboxInputF(
            parent=self,

            user_instruction=const.TSDI_BATCH_SIZE_INSTRUCTION,
            user_options=const.TSDI_BATCH_SIZE_OPTIONS,

            selection_eh=self._examples_per_batch_eh,

            disabled=False
        )

        self._cbi_epochs_nbr = ComboboxInputF(
            parent=self,

            user_instruction=const.TSDI_EPOCHS_NBR_INSTRUCTION,
            user_options=const.TSDI_EPOCHS_NBR_OPTIONS,

            selection_eh=self._number_of_epochs_eh,

            disabled=False
        )

        self._cbi_image_size = ComboboxInputF(
            parent=self,

            user_instruction=const.TSDI_IMAGE_SIZE_INSTRUCTION,
            user_options=const.TSDI_IMAGE_SIZE_OPTIONS,

            selection_eh=self._image_size_eh,

            disabled=False
        )

        if self._k_fold_cv_session:
            self._cbi_number_of_folds = ComboboxInputF(
                parent=self,

                user_instruction=const.TSDI_K_FOLD_CV_INSTRUCTION,
                user_options=const.TSDI_K_FOLD_CV_OPTIONS,

                selection_eh=self._number_of_folds_eh,

                disabled=False
            )

    def _place_widgets(self):

        self._lbl_title.pack(side='top',
                             fill='both',
                             expand=True)

        self._f_browse.pack(side='top',
                            fill='both',
                            expand=True)

        self._cbi_nn_model.pack(side='top',
                                fill='both',
                                expand=True)
        self._cbi_batch_size.pack(side='top',
                                  fill='both',
                                  expand=True)
        self._cbi_epochs_nbr.pack(side='top',
                                  fill='both',
                                  expand=True)
        self._cbi_image_size.pack(side='top',
                                  fill='both',
                                  expand=True)

        if self._k_fold_cv_session:
            self._cbi_number_of_folds.pack(side='top',
                                           fill='both',
                                           expand=True)

    #########################################################################
    # Event handling

    def _data_set_selected_eh(
            self,

            data_set_path: str):
        """ Called when the user selects a data set."""

        self._sess_details.main_data_set_file = data_set_path

        self._check_form_completion()

    def _neural_network_selected_eh(
            self,

            neural_network):
        """ 
        - Called when the user selects a neural network model.
        """

        self._sess_details.neural_network = neural_network

        self._check_form_completion()

    def _examples_per_batch_eh(
            self,

            example_per_batch):
        """ 
        - Called when the user selects the number of examples per batch.
        """

        self._sess_details.examples_per_batch = int(example_per_batch)

        self._check_form_completion()

    def _number_of_epochs_eh(
            self,

            number_of_epochs):
        """ 
        - Called when the user selects the number of epochs.
        """

        self._sess_details.number_of_epochs = int(number_of_epochs)

        self._check_form_completion()

    def _image_size_eh(
            self,

            img_size):
        """ 
        - Called when the user selects the image size.
        """

        self._sess_details.image_size = int(img_size)

        self._check_form_completion()

    def _number_of_folds_eh(
            self,

            number_of_folds):
        """ 
        - Called when the user selects the image size.
        """

        self._sess_details.number_of_folds = int(number_of_folds)

        self._check_form_completion()

    def _check_form_completion(self):
        """
        - Checks if the input form is completed

        :return: - True if the form is completed
                 - False otherwise
        """

        if self._sess_details.session_details_input_are_valid():
            self._valid_input_eh()
        else:
            self._invalid_input_eh()

    #########################################################################
    # Public methods

    def get_input(self):

        return self._sess_details

    def enable(self):
        """ Enables all the widgets."""

        if self._k_fold_cv_session:
            self._cbi_number_of_folds.enable()

        self._lbl_title.config(state='normal')
        self._cbi_batch_size.enable()
        self._cbi_epochs_nbr.enable()
        self._cbi_image_size.enable()
        self._cbi_nn_model.enable()
        self._f_browse.enable()

    def disable(self):
        """ Disables all the widgets."""

        if self._k_fold_cv_session:
            self._cbi_number_of_folds.disable()

        self._lbl_title.config(state='disabled')
        self._cbi_batch_size.disable()
        self._cbi_epochs_nbr.disable()
        self._cbi_image_size.disable()
        self._cbi_nn_model.disable()
        self._f_browse.disable()

    #########################################################################
