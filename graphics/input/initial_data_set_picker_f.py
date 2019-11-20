from utils.data_set.classes_correlation_between_data_sets import ClassesCorrelationBetweenDataSets
from utils.data_set.initial_data_set import InitialDataSet

from graphics.input.class_identifiers_input_f import ClassIdentifiersInputF
from graphics.widgets.qna_f import QnAF

from tkinter import filedialog
from tkinter import messagebox

import file_experts.file_expert as f_expert
import constants.input_constants as const
import tkinter as tk


class InitialDataSetPickerF(tk.Frame):
    """
    - Use to get input regarding the relations between the new data set's 
    class identifiers and the identifiers form the initial data set.
    """

    def __init__(self,

                 parent,

                 classes: [],

                 picker_id: int,

                 valid_input_eh,
                 invalid_input_eh,

                 disabled=False):
        """
        :param parent: Parent.
        
        :param classes: List with the class names.
            
        :param valid_input_eh: Method that will be called when the form is 
                               completed.
        :param invalid_input_eh: Method that will be called after each user 
                                 input if the form is not/no longer 
                                 completed.
        
        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """
        tk.Frame.__init__(self,
                          parent,
                          padx=const.IDSP_FRAME_PADX,
                          pady=const.IDSP_FRAME_PADY,
                          relief='sunken',
                          bd=5)

        self._invalid_input_eh = invalid_input_eh
        self._valid_input_eh = valid_input_eh
        self._picker_id = picker_id
        self._classes = classes

        self._valid = False

        self._var_initial_data_set = tk.IntVar()
        self._previous_selection = const.IDSP_NO_SELECTION_VAL

        self._data_set_details = InitialDataSet()

        self._create_frames()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_frames(self):
        """ Creates the frames."""

        question = self._create_question_text()

        self._qna_initial_data_set = QnAF(
            parent=self,

            frame_variable=self._var_initial_data_set,

            question_text=question,

            answers_text=[
                const.IDSP_CIFAR10_BTN_TEXT,
                const.IDSP_IMAGENET_BTN_TEXT,
                const.IDSP_FROM_IMAGES_BTN_TEXT
            ],
            answers_eh=[
                self._cifar_10_eh,
                self._imagenet_eh,
                self._from_images_eh,
            ]
        )

        self._cii_class_input = ClassIdentifiersInputF(
            parent=self,

            valid_input_eh=self._valid_cii_form_eh,
            invalid_input_eh=self._invalid_cii_form_eh,

            disabled=False
        )

        self._cii_class_input.update_classes(class_names=self._classes)

        self._lbl_instruction = tk.Label(
            self,

            padx=const.IDSP_WIDGETS_PADX,
            pady=const.IDSP_WIDGETS_PADY,

            text=const.IDSP_INSTRUCTION_TEXT,
            font=const.IDSP_FONT
        )

    def _place_widgets(self):
        """ Places the widgets."""

        self._qna_initial_data_set.pack(side='top',
                                        fill='both',
                                        expand=True)
        self._cii_class_input.pack(side='top',
                                   fill='both',
                                   expand=True)
        self._lbl_instruction.pack(side='top',
                                   fill='both',
                                   expand=True)

    #########################################################################
    # Event handling

    def _cifar_10_eh(self):
        """
        - Called when the user selects cifar 10 as the initial data set.
        """

        self._data_set_details.cifar10_train_ds = messagebox.askyesno(
            title=const.IDSP_CIFAR10_TRAIN_DS_TITLE,
            message=const.IDSP_CIFAR10_TRAIN_DS_MSG
        )

        if self._data_set_details.cifar10_train_ds:
            self._data_set_details.cifar10_test_ds = messagebox.askyesno(
                title=const.IDSP_CIFAR10_TEST_DS_TITLE,
                message=const.IDSP_CIFAR10_TEST_DS_MSG
            )
        else:
            self._data_set_details.cifar10_test_ds = True

        self._data_set_details.cifar10 = True
        self._data_set_details.imagenet = False
        self._data_set_details.images = False

        self._data_set_details.identifiers = const.IDSP_CIFAR10_IDENTIFIERS

        self._cii_class_input.update_data_set_identifier(
            self._data_set_details.identifiers)

        # Sets the previous selection value to the current button.
        self._previous_selection = const.IDSP_CIFAR10_VAL

        # Until the user selects the identifiers for each class the form is
        # invalid.
        self._invalid_cii_form_eh()
        self._lbl_instruction.forget()

    def _imagenet_eh(self):
        """
        - Called when the user selects ImageNet as the initial data set.
        
        - Not yet implemented.
        """

        # TODO

        messagebox.showinfo(
            title=const.IDSP_IMAGENET_TITLE,
            message=const.IDSP_IMAGENET_MSG
        )

        if self._previous_selection != const.IDSP_NO_SELECTION_VAL:
            self._qna_initial_data_set.select_button(
                self._previous_selection)
        else:
            self._qna_initial_data_set.deselect_button(
                const.IDSP_IMAGENET_VAL)

        """
        self._data_set_details.cifar10 = False
        self._data_set_details.imagenet = True
        self._data_set_details.images = False
        """

    def _from_images_eh(self):
        """
        - Called when the user wants to use folders with images as initial 
        data set.
        """

        self._data_set_details.data_set_location = filedialog.askdirectory(
            title=const.IDSP_FROM_IMAGES_INITIAL_DIR,
            initialdir=const.IDSP_FROM_IMAGES_TITLE
        )

        selected_path = self._data_set_details.data_set_location

        # Checks if the user has selected a directory.
        if isinstance(selected_path, str) and selected_path != '':
            # Checks if the received path is a directory.
            if f_expert.is_directory(selected_path):
                # Gets a list with all the visible subdirectories.
                self._data_set_details.identifiers = \
                    f_expert.get_directories(selected_path)

                # Updates the identifier list
                self._cii_class_input.update_data_set_identifier(
                    self._data_set_details.identifiers)

                # Sets teh previous selection value to the current button.
                self._previous_selection = const.IDSP_FROM_IMAGES_VAL

                # Saving details about the initial data set.
                self._data_set_details.cifar10 = False
                self._data_set_details.imagenet = False
                self._data_set_details.images = True

                # Until the user selects the identifiers for each class the
                # form is invalid.
                self._invalid_cii_form_eh()
                self._lbl_instruction.forget()
        else:
            # If the user did not select a directory.
            if self._previous_selection != const.IDSP_NO_SELECTION_VAL:
                # If another initial data set was selected before, that
                # button is selected again.
                self._qna_initial_data_set.select_button(
                    self._previous_selection)
            else:
                # If no initial data set was selected before, the current
                # button is deselected.
                self._qna_initial_data_set.deselect_button(
                    const.IDSP_FROM_IMAGES_VAL)

    def _valid_cii_form_eh(self):
        """
        - Called when the form is completed.
        """

        self._data_set_details.class_correlation = \
            self._cii_class_input.get_input()

        self._valid = True

        self._valid_input_eh()

        self.disable()

    def _invalid_cii_form_eh(self):
        """
        - Called when the form is not completed.
        """

        self._data_set_details.class_correlation = \
            ClassesCorrelationBetweenDataSets()

        self._valid = False

        self._invalid_input_eh()

    def _create_question_text(self):
        """
        - Creates form title.
        """

        return const.IDSP_QUESTION_TEXT + ' #' + str(self._picker_id)

    #########################################################################
    # Public methods

    def update_classes(
            self,

            classes: []):

        self._classes = classes

        self._cii_class_input.update_classes(classes)

    def get_input(self):
        """
        :return:    - List with the relations between the new data set 
                    identifier (list index) and the old data set identifier.
                     - [] if the form is not completed.
        """

        return self._data_set_details

    def update_picker_id(
            self,

            new_id):

        self._picker_id = new_id
        self._qna_initial_data_set.update_question_text(self._create_question_text())

    def form_is_valid(self):
        """
        :return:    - True if the form is valid.
                    - False otherwise.
        """

        return self._valid

    # ~~~~~~~~~~~~~~~~~~~~~Enable / disable the widget.~~~~~~~~~~~~~~~~~~~~~~

    def enable(self):
        """ Enables all the widgets."""

        if not self._valid:
            self._lbl_instruction.config(state='normal')
            self._qna_initial_data_set.enable()
            self._cii_class_input.enable()
        else:
            self.disable()

    def disable(self):
        """ Disables all the widgets."""

        self._cii_class_input.disable()
        self._qna_initial_data_set.disable()
        self._lbl_instruction.config(state='disabled')

    # ~~~~~~~~~~~~~~~~~~~~~Enable / disable Cifar10 button.~~~~~~~~~~~~~~~~~~

    def enable_cifar10(self):
        """ Enables Cifar10 button."""

        # 0 is the index of the "Cifar10" button.
        self._qna_initial_data_set.enable_button(0)

    def disable_cifar10(self):
        """ Disables Cifar10 button."""

        # 0 is the index of the "Cifar10" button.
        self._qna_initial_data_set.disable_button(0)

    # ~~~~~~~~~~~~~~~~~~~~~Enable / disable ImageNet button.~~~~~~~~~~~~~~~~~

    def enable_imagenet(self):
        """ Enables ImageNet button."""

        # 1 is the index of the "ImageNet" button.
        self._qna_initial_data_set.enable_button(1)

    def disable_imagenet(self):
        """ Disables ImageNet button."""

        # 1 is the index of the "ImageNet" button.
        self._qna_initial_data_set.disable_button(1)

    # ~~~~~~~~~~~~~~~~~~~~~Enable / disable from images button.~~~~~~~~~~~~~~

    def enable_from_images(self):
        """ Enables From images button."""

        # 2 is the index of the "From images" button.
        self._qna_initial_data_set.enable_button(2)

    def disable_from_images(self):
        """ Disables From images button."""

        # 2 is the index of the "From images" button.
        self._qna_initial_data_set.disable_button(2)

    #########################################################################
