from utils.train.data_augmentation import DataAugmentation


import constants.train_sess_constants as const
import file_experts.file_expert as fe


class SessionDetails:

    def __init__(
            self,

            k_fold_cv_session=False):

        self._k_fold_cv_session = k_fold_cv_session

        self._name = ''
        self._description = ''
        self._data_set_name = ''

        self._session_current_path = ''
        self._main_data_set_file = ''

        self._neural_network = ''
        self._examples_per_batch = -1
        self._number_of_classes = -1
        self._number_of_epochs = -1
        self._number_of_folds = -1
        self._image_size = -1

        self.data_augmentation = DataAugmentation()

    def __str__(self):

        rez = '\n\n**** Session details ****'
        rez += '\n\tName                    :    ' + self.name
        rez += '\n\tDescription             :    ' + self.description
        rez += '\n\t- Current session path  :    ' + self.session_current_path
        rez += '\n\t- Data set directory    :    ' + self.data_set_directory
        rez += '\n\t- Main data set file    :    ' + self.main_data_set_file
        rez += '\n\tNN model used           :    ' + self.neural_network
        rez += '\n\tData set name           :    ' + self.data_set_name
        rez += '\n\tExamples / batch        :    ' + str(self.examples_per_batch)
        rez += '\n\tNumber of classes       :    ' + str(self.number_of_classes)
        rez += '\n\tNumber of epochs        :    ' + str(self.number_of_epochs)
        rez += '\n\tNumber of folds         :    ' + str(self.number_of_folds)
        rez += '\n\tImage size              :    ' + str(self.image_size)
        rez += str(self.data_augmentation)
        rez += '\n+****Is valid : ' + str(self.is_valid()) + ' ****'

        return rez

    ##########################################################################
    # name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,
             value: str):
        if not isinstance(value, str) or value == '':
            raise ValueError('Name must be string and not empty.')

        self._name = value

    ##########################################################################
    # description

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,
                    value: str):
        if not isinstance(value, str) or value == '':
            raise ValueError('Description must be string and not empty.')

        self._description = value

    ##########################################################################
    # neural_networks

    @property
    def neural_network(self):
        return self._neural_network

    @neural_network.setter
    def neural_network(self,
                       value: str):
        if value not in const.TSDI_NN_MODEL_OPTIONS \
                or not isinstance(value, str):
            raise ValueError(
                'Neural network must be string and the value must be one of '
                + 'the following :    '
                + str(const.TSDI_NN_MODEL_OPTIONS)
                + '.\n But got :    '
                + str(value)
                + '.\n'
            )

        self._neural_network = value

    ##########################################################################
    # session_current_path

    @property
    def session_current_path(self):
        return self._session_current_path

    @session_current_path.setter
    def session_current_path(self,
                             value: str):

        if not isinstance(value, str):
            raise ValueError(
                'The current location for the session files must be a string'
                ' and also a valid directory path.\n But got: ' + str(value)
            )

        self._session_current_path = value

    ##########################################################################
    # main_data_set_file

    @property
    def main_data_set_file(self):
        return self._main_data_set_file

    @main_data_set_file.setter
    def main_data_set_file(
            self,
            value: str):

        if not isinstance(value, str) \
                or not fe.is_file(value):
            raise ValueError('Data set location must be a string and also a '
                             'valid file path.\n But got: ' + str(value))

        self._main_data_set_file = value

    ##########################################################################
    # data_set_name

    @property
    def data_set_name(self):
        return self._data_set_name

    @data_set_name.setter
    def data_set_name(self,
                      value: str):

        if not isinstance(value, str):
            raise ValueError('Data set location must be a string.')

        self._data_set_name = value

    ##########################################################################
    # data_set_directory

    @property
    def data_set_directory(self):
        return self.session_current_path \
               + '/' \
               + self.data_set_name

    ##########################################################################
    # checkpoints_directory

    @property
    def checkpoints_directory(self):
        return self.session_current_path \
               + '/checkpoints'

    ##########################################################################
    # examples_per_batch

    @property
    def examples_per_batch(self):
        return self._examples_per_batch

    @examples_per_batch.setter
    def examples_per_batch(self,
                           value: int):
        if value not in const.TSDI_BATCH_SIZE_OPTIONS \
                or not isinstance(value, int):
            raise ValueError(
                'The number of examples / batch must be int and the value '
                + 'must be one of the following :    '
                + str(const.TSDI_BATCH_SIZE_OPTIONS)
                + '.\n But got :    '
                + str(value)
                + '.\n'
            )

        self._examples_per_batch = value

    ##########################################################################
    # number_of_classes

    @property
    def number_of_classes(self):
        return self._number_of_classes

    @number_of_classes.setter
    def number_of_classes(self,
                          value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('The number of classes must be int and the '
                             'value must be above 0.')

        self._number_of_classes = value

    ##########################################################################
    # number_of_epochs

    @property
    def number_of_epochs(self):
        return self._number_of_epochs

    @number_of_epochs.setter
    def number_of_epochs(self,
                         value: int):
        if not isinstance(value, int) \
                or value not in const.TSDI_EPOCHS_NBR_OPTIONS:
            raise ValueError(
                'The number of epochs must be int and the value must be one '
                + 'of the following :    '
                + str(const.TSDI_EPOCHS_NBR_OPTIONS)
                + '.\n But got :    '
                + str(value)
                + '.\n'
            )

        self._number_of_epochs = value

    ##########################################################################
    # number_of_folds

    @property
    def number_of_folds(self):
        return self._number_of_folds

    @number_of_folds.setter
    def number_of_folds(self,
                        value: int):
        if not isinstance(value, int) \
                or value not in const.TSDI_K_FOLD_CV_OPTIONS:
            raise ValueError(
                'The number of folds must be int and the value must be one '
                + 'of the following :    '
                + str(const.TSDI_K_FOLD_CV_OPTIONS)
                + '.\n But got :    '
                + str(value)
                + '.\n'
            )

        self._number_of_folds = value

    ##########################################################################
    # image_size

    @property
    def image_size(self):
        return self._image_size

    @image_size.setter
    def image_size(self,
                   value: int):
        if value not in const.TSDI_IMAGE_SIZE_OPTIONS \
                or not isinstance(value, int):
            raise ValueError(
                'The image size of folds must be int and the value must be'
                + ' one of the following :    '
                + str(const.TSDI_IMAGE_SIZE_OPTIONS)
                + '.\n But got :    '
                + str(value)
                + '.\n'
            )

        self._image_size = value

    ##########################################################################

    def session_details_input_are_valid(self):
        """
        - Checks if all the input properties are valid.

        :return: - True if all the input properties are valid.
                 - False otherwise.
        """

        if self._k_fold_cv_session:
            if not isinstance(self.number_of_folds, int) \
                    or self.number_of_folds not in const.TSDI_K_FOLD_CV_OPTIONS:
                return False

        if not isinstance(self._data_set_name, str) \
                or not isinstance(self.examples_per_batch, int) \
                or not isinstance(self.number_of_epochs, int) \
                or not isinstance(self.neural_network, str) \
                or not isinstance(self.image_size, int):
            return False

        if self.examples_per_batch not in const.TSDI_BATCH_SIZE_OPTIONS \
                or self.number_of_epochs not in const.TSDI_EPOCHS_NBR_OPTIONS \
                or self.neural_network not in const.TSDI_NN_MODEL_OPTIONS \
                or self.image_size not in const.TSDI_IMAGE_SIZE_OPTIONS \
                or not fe.is_file(self.main_data_set_file):
            return False

        return True

    ##########################################################################

    def is_valid(self):
        """
        - Checks if all the properties are valid.

        :return: - True if all the properties are valid.
                 - False otherwise.
        """

        if self._k_fold_cv_session:
            if not isinstance(self.number_of_folds, int) \
                    or self.number_of_folds not in const.TSDI_K_FOLD_CV_OPTIONS:
                return False

        if not isinstance(self.examples_per_batch, int) \
                or not isinstance(self.number_of_classes, int) \
                or not isinstance(self.number_of_epochs, int) \
                or not isinstance(self.neural_network, str) \
                or not isinstance(self.description, str) \
                or not isinstance(self.image_size, int) \
                or not isinstance(self.name, str):
            return False

        if self.examples_per_batch not in const.TSDI_BATCH_SIZE_OPTIONS \
                or self.number_of_epochs not in const.TSDI_EPOCHS_NBR_OPTIONS \
                or self.neural_network not in const.TSDI_NN_MODEL_OPTIONS \
                or self.image_size not in const.TSDI_IMAGE_SIZE_OPTIONS \
                or self.number_of_classes < 0 \
                or self.description == '' \
                or self.name == '':
            return False

        return True

    ##########################################################################

    def to_json(self):

        data_augmentation = self.data_augmentation.to_json()

        print(self)

        js = {
            'Name'              : self.name,
            'Description'       : self.description,
            'NN model used'     : self.neural_network,
            'Number of classes' : self.number_of_classes,
            'Examples / batch'  : self.examples_per_batch,
            'Number of epochs'  : self.number_of_epochs,
            # 'Number of folds'   : self.number_of_folds, For now not needed.
            'Image size'        : self.image_size,
            'Data set name'     : self.data_set_name,

            'Data augmentation' : data_augmentation,
        }

        return js

    ##########################################################################

    def from_json(
            self,

            js: {}):

        self.name = js['Name']
        self.description = js['Description']
        self.neural_network = js['NN model used']
        self.examples_per_batch = js['Examples / batch']
        self.number_of_classes = js['Number of classes']
        self.number_of_epochs = js['Number of epochs']
        # self.number_of_folds = js['Number of folds']    For now not needed.
        self.image_size = js['Image size']
        self.data_set_name = js['Data set name']

        self.data_augmentation.from_json(
            js=js['Data augmentation']
        )

    ##########################################################################
