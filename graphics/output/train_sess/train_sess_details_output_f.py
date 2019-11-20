from graphics.output.train_sess.train_sess_save_details_output_f import TrainSessSaveDetailsOutputF
from graphics.output.data_set.used_data_sets_output_f import UsedDataSetsOutputF
from graphics.output.data_augmentation_output_f import DataAugmentationOutputF
from graphics.output.classes_output import ClassesOutputF

from utils.data_set.data_set_classes import DataSetClasses
from utils.data_set.data_set_details import DataSetDetails
from utils.train.data_augmentation import DataAugmentation
from utils.data_set.used_data_sets import UsedDataSets
from utils.train.session_details import SessionDetails


import tkinter as tk


class TrainSessDetailsOutputF(tk.Frame):
    """
    - Use to display informations about a training session.
    """

    def __init__(self,

                 parent,

                 disabled=False):
        """
        :param parent: Parent.

        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent)

        self._create_widgets()
        self._place_widgets()

        if disabled:
            self.disable()

    #########################################################################
    # Widget creation and placement

    def _create_widgets(self):

        self._data_augmentation_output = DataAugmentationOutputF(
            parent=self,
        )

        self._classes_output = ClassesOutputF(
            parent=self,
        )

        self._session_details_output = TrainSessSaveDetailsOutputF(
            parent=self,
        )

        self._used_data_sets_output = UsedDataSetsOutputF(
            parent=self,
        )

    def _place_widgets(self):

        self._session_details_output.pack(side='top',
                                          fill='both',
                                          expand=True)

        self._data_augmentation_output.pack(side='top',
                                            fill='both',
                                            expand=True)

        self._classes_output.pack(side='top',
                                  fill='both',
                                  expand=True)

        self._used_data_sets_output.pack(side='top',
                                         fill='both',
                                         expand=True)

    #########################################################################
    # Public methods

    def update_session_details(
            self,

            data_set_details: DataSetDetails,
            session_details: SessionDetails):
        """
        - Call to update the session's details.

        :param data_set_details: DataSetDetails
        :param session_details: SessionDetails
        """

        self._session_details_output.update_save_details(
            train_sess_details=session_details)

        self.update_data_augmentation(
            data_augmentation_options=session_details.data_augmentation
        )

        self.update_classes(
            classes=data_set_details.classes
        )

        used_data_sets = UsedDataSets()
        used_data_sets.add(data_set_details)

        self.update_used_data_sets(
            used_data_sets=used_data_sets
        )

    def update_data_augmentation(
            self,

            data_augmentation_options: DataAugmentation):
        """
        - Call to update the data augmentation methods used by the session.

        :param data_augmentation_options: DataAugmentation
        """

        self._data_augmentation_output.update_status(
            data_augmentation_options)

    def update_classes(
            self,

            classes: DataSetClasses):
        """
        - Call to update the session's classes.

        :param classes: DataSetClasses
        """

        self._classes_output.update_classes(
            classes)

    def update_used_data_sets(
            self,

            used_data_sets: UsedDataSets):
        """
        - Call to update the list with the data sets used by the session 
        until now..

        :param used_data_sets: UsedDataSets
        """

        self._used_data_sets_output.update_used_data_sets(
            used_data_sets
        )

    def enable(self):
        """ Enables all the widgets."""

        self._data_augmentation_output.enable()
        self._session_details_output.enable()
        self._used_data_sets_output.enable()
        self._classes_output.enable()

    def disable(self):
        """ Disables all the widgets."""

        self._classes_output.disable()
        self._used_data_sets_output.disable()
        self._session_details_output.disable()
        self._data_augmentation_output.disable()

    #########################################################################
