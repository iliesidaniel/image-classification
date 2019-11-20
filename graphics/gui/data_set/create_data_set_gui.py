from graphics.input.initial_data_sets_picker_f import InitialDataSetsPickerF
from graphics.input.data_set_details_input import DataSetDetailsInput
from graphics.widgets.scrollable_canvas_c import ScrollableCanvasC
from graphics.input.class_names_input_f import ClassNamesInputF
from graphics.widgets.progress_bar_c import ProgressBarC

from project_exceptions.data_set_exceptions import CorruptMainDataSetFile

from controllers.data_set_controller import DataSetController

from utils.data_set.data_set_classes import DataSetClasses
from utils.data_set.data_set_class import DataSetClass

from tkinter import messagebox


import constants.create_data_set_constants as ds_const
import constants.gui_constants as const

import file_experts.file_expert as file_expert

import tkinter as tk
import sys
import os


class CreateDataSetGUI(tk.Frame):
    """
    - Use to get input for a new data set.
    """

    def __init__(self,

                 parent,

                 enable_main_window_buttons,
                 disable_main_window_buttons):

        tk.Frame.__init__(self,
                          parent)

        self._enable_main_window_buttons = enable_main_window_buttons
        self._disable_main_window_buttons = disable_main_window_buttons

        self._valid_initial_data_sets = False
        self._valid_class_name_input = False
        self._valid_save_details = False

        self._creation = True

        self._create_frames()
        self._place_frames()

        self._creation = False

    def _create_frames(self):

        self._sc_scrollable = ScrollableCanvasC(
            parent=self,
        )

        self._f_create_btn = tk.Frame(
            self._sc_scrollable.f_main_frame,

            padx=const.CDSG_SUBFRAME_PADX,
            pady=60
        )

        self._f_progress_bar = tk.Frame(
            self._sc_scrollable.f_main_frame,

            padx=const.CDSG_SUBFRAME_PADX,
            pady=const.CDSG_SUBFRAME_PADY
        )

        self._lbl_title = tk.Label(
            self._sc_scrollable.f_main_frame,

            font=const.CDSG_TITLE_FONT,
            text=const.CDSG_TITLE_TEXT,

            relief=const.CDSG_TITLE_RELIEF,
            padx=const.CDSG_TITLE_PADX,
            pady=const.CDSG_TITLE_PADY,
            bd=const.CDSG_TITLE_BD
        )

        # InitialDataSetsPickerF
        self._initial_data_sets_input = InitialDataSetsPickerF(
            parent=self._sc_scrollable.f_main_frame,

            classes=[],

            valid_input_eh=self._valid_initial_data_sets_eh,
            invalid_input_eh=self._invalid_initial_data_sets_eh,

            disabled=True
        )

        # ClassNamesInputF
        self._class_names_input = ClassNamesInputF(
            parent=self._sc_scrollable.f_main_frame,

            valid_input_eh=self._valid_class_names_eh,
            invalid_input_eh=self._invalid_class_names_eh,

            disabled=True
        )

        # SaveDetailsInputF
        self._save_details_input = DataSetDetailsInput(
            parent=self._sc_scrollable.f_main_frame,

            file_extension=const.CDSG_FILE_EXTENSION,

            valid_input_eh=self._valid_save_details_eh,
            invalid_input_eh=self._invalid_save_details_eh,

            disabled=False
        )

        # Data set create button
        self._btn_create = tk.Button(
            self._f_create_btn,

            text=const.CDSG_CREATE_BTN_TEXT,
            font=const.CDSG_TITLE_FONT,

            command=self._create_data_set,
            # state='disabled',

            padx=const.CDSG_CREATE_BTN_PADX * 2,
            pady=const.CDSG_CREATE_BTN_PADY,
            bd=const.CDSG_CREATE_BTN_BD
        )

        # ProgressBarC
        self._progress_bar = ProgressBarC(
            self._f_progress_bar,

            width=const.CDSG_PB_WIDTH,
            height=const.CDSG_PB_HEIGHT,

            text=const.CDSG_PB_NO_INPUT_TEXT,
            fill_percent=const.CDSG_PB_NO_INPUT_PERCENT,

            fill_color=const.CDSG_PB_FILL_COLORS,
            empty_color=const.CDSG_PB_EMPTY_COLORS,
            text_color=const.CDSG_PB_TEXT_COLORS
        )

    def _place_frames(self):

        self._sc_scrollable.pack(side='top',
                                 fill='both',
                                 expand=True)

        self._lbl_title.pack(side='top',
                             fill='x',
                             expand=True)

        self._save_details_input.pack(side='top',
                                      fill='both',
                                      expand=True)

        self._class_names_input.pack(side='top',
                                     fill='both',
                                     expand=True)

        self._initial_data_sets_input.pack(side='top',
                                           fill='both',
                                           expand=True)

        self._btn_create.pack(side='top')

        self._progress_bar.pack(side='top',
                                fill='both',
                                expand=True)

        self._f_create_btn.pack(side='top',
                                fill='both',
                                expand=True)

        self._f_progress_bar.pack(side='top',
                                  fill='both',
                                  expand=True)

    #########################################################################
    # Event handlers

    # ~~~~~~~~~~~~~~~~~~~~~Save details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _valid_save_details_eh(
            self,

            save_details):
        """
        - Called when the save details form is valid.
        """

        self._valid_save_details = True

        print('~~~~~~~~~~~~~~~')
        print(str(save_details))
        print('~~~~~~~~~~~~~~~')

        # TODO

        self._check_form_validity()

    def _invalid_save_details_eh(self):
        """
        - Called when the save details form is invalid.
        """

        self._valid_save_details = False

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Class name input~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _valid_class_names_eh(self):
        """
        - Called when the class name form is valid.
        """

        self._valid_class_name_input = True

        class_names = self._class_names_input.get_input()

        self._initial_data_sets_input.update_classes(
            classes=class_names)

        self._check_form_validity()

    def _invalid_class_names_eh(self):
        """
        - Called when the class name form is invalid.
        """

        self._valid_class_name_input = False

        class_names = []

        self._initial_data_sets_input.update_classes(
            classes=class_names)

        self._check_form_validity()

    # ~~~~~~~~~~~~~~~~~~~~~Initial data set(s)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _valid_initial_data_sets_eh(self):
        """
        - Called when the initial data sets form is valid.
        """

        self._valid_initial_data_sets = True

        self._check_form_validity()

    def _invalid_initial_data_sets_eh(self):
        """
        - Called when the initial data sets form is invalid.
        """

        self._valid_initial_data_sets = False

        self._check_form_validity()

    #########################################################################
    # Auxiliary methods

    def _check_form_validity(self):
        """
        - Enables and disables widgets depending on the user input.
        """

        if self._valid_save_details:
            self._class_names_input.enable()

            if self._valid_class_name_input:
                self._initial_data_sets_input.enable()

                if self._valid_initial_data_sets:
                    self._btn_create.config(state='normal')
                else:
                    self._btn_create.config(state='disabled')
            else:
                self._btn_create.config(state='disabled')
                self._initial_data_sets_input.disable()
        elif not self._creation:
            self._btn_create.config(state='disabled')
            self._initial_data_sets_input.disable()
            self._class_names_input.disable()

    def _create_data_set(self):
        """
        - Starts the data set creation.
        """

        try:
            self._btn_create.config(state='disabled')
            self._initial_data_sets_input.disable()
            self._save_details_input.disable()
            self._class_names_input.disable()

            classes_list = self._class_names_input.get_input()

            classes = DataSetClasses()

            for index in range(len(classes_list)):
                tmp = DataSetClass()

                tmp.identifier = index
                tmp.class_name = classes_list[index]
                tmp.number_of_examples = 0

                classes.add(tmp)

            DataSetController.create_new_data_set(
                creation_details=self._save_details_input.get_new_file_details(),
                initial_data_sets=self._initial_data_sets_input.get_input(),
                data_set_creation_gui=self,
                data_set_classes=classes,
                image_size=self._save_details_input.get_image_size(),
                number_of_files=self._save_details_input.get_number_of_files()
            )

            self._disable_main_window_buttons()

        except FileNotFoundError:
            messagebox.showerror(
                title='Data set file not found!',
                message='The data set you selected does not exist.'
                        '\n\nPlease select another data set.'
            )
        except CorruptMainDataSetFile:
            messagebox.showerror(
                title='Data set file is corrupt!',
                message='The data set you selected is corrupt.'
                        '\n\nPlease select another data set.'
            )

    #########################################################################
    # Public methods

    def _update_progress(
            self,

            progress_text: str,
            progress_value: int):
        """
        - Updates the progress bar.
        """

        if not isinstance(progress_value, int) \
                or progress_value < 0:
            raise ValueError('Value provided '
                             + str(progress_value)
                             + '. It must be an integer >=0 and <=100.')

        if progress_value > 100:
            progress_value = 100

        print(progress_text)

        self._progress_bar.update_progress(
            percent=progress_value,
            text=progress_text
        )

    def creation_preparations(self):
        """
        - Use this to inform the user that the program is preparing the data
        set creation.
        """

        text = 'Preparing the data set creation.'

        self._update_progress(
            progress_value=0,
            progress_text=text
        )

    def update_cifar10_download_progress(
            self,

            progress: int):
        """
        - Updates the progress bar with the current download percentage.
        """

        if progress != 100:
            text = 'Downloading Cifar10  -  ' \
                   + str(progress) \
                   + '% completed'
        else:
            text = 'Cifar10 download completed!'

        self._update_progress(
            progress_value=progress,
            progress_text=text
        )

    def update_image_ds_progress(
            self,

            progress: int):
        """
        - Updates the progress bar with the percentage of the images
        converted to TFRecords.
        """

        if progress != 100:
            text = 'Writing data set files  -  from images  -  ' \
                   + str(progress) \
                   + '% completed'
        else:
            text = 'All images written in data set files.'

        self._update_progress(
            progress_value=progress,
            progress_text=text
        )

    def update_cifar10_ds_progress(
            self,

            progress: int,
            train_ds: bool):
        """
        - Updates the progress bar with the percentage of the Cifar 10
        converted to TFRecords.
        """

        if progress != 100:
            text = 'Writing data set files  -  from Cifar10 '

            if train_ds:
                text += 'train'
            else:
                text += 'test'

            text += ' data set -  ' + str(progress) + '% completed'
        else:
            text = 'All examples from Cifar10 written in data set files.'

        self._update_progress(
            progress_value=progress,
            progress_text=text
        )

    def creation_completed(self):
        """
        - Call when the data set creation is completed.
        """

        self._update_progress(
            progress_value=100,
            progress_text='Data set is created!'
        )

        self._enable_main_window_buttons()

    def cifar10_download_failed_eh(self):
        """
        - Called when the cifar10 download failed.
        """

        self._update_progress(
            progress_value=const.CDSG_PB_NO_INPUT_PERCENT,
            progress_text='Data set is created!'
        )

        data_set_location = os.path.realpath(sys.argv[0])
        data_set_location = file_expert.remove_last_entry_from_path(
            path=data_set_location
        )

        data_set_location += ds_const.CIFAR10_SAVE_LOCATION + '/'
        files_location = data_set_location + ds_const.CIFAR10_DIRECTORY_NAME

        option1 = '\n\n    1. Check your Internet connection and try again.'
        option2 = '\n\n    2. If you have the Cifar 10 archive (' \
                  + ds_const.CIFAR10_ARCHIVE_FILE \
                  + ') place it to "' \
                  + data_set_location \
                  + '".'
        option3 = '\n\n    3. If you have the Cifar 10 files, place them ' \
                  'in "' \
                  + files_location \
                  + '", and make sure they have the following names and ' \
                    'extensions:'

        for file_name in ds_const.CIFAR10_FILE_NAMES:
            option3 += '\n       * ' + file_name

        messagebox.showerror(
            title='Cifar10 download failed!',
            message='Failed to download the Cifar 10 data set.\n'
                    '\n\nPossible options to solve this:'
                    + option1
                    + option2
                    + option3
        )

    #########################################################################
