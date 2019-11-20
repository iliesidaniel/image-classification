from utils.data_set.classes_correlation_between_data_sets import ClassesCorrelationBetweenDataSets

import file_experts.file_expert as fe


class InitialDataSet:

    def __init__(self):

        self._cifar10 = False
        self._imagenet = False
        self._images = False

        self._cifar10_train_ds = False
        self._cifar10_test_ds = False

        self._data_set_location = ''

        self.class_correlation = ClassesCorrelationBetweenDataSets()

    def __str__(self):

        rez = '\n**** Initial data set ****\n'
        rez += '\nCifar 10    :    ' + str(self.cifar10)
        rez += '\nImageNet    :    ' + str(self.imagenet)
        rez += '\nFrom images :    ' + str(self.images)

        rez += '\n\nCifar 10 data sets :'
        rez += '\n    Train data set :    ' + str(self.cifar10_train_ds)
        rez += '\n    Test data set  :    ' + str(self.cifar10_test_ds)

        rez += '\n\nData set location : '
        rez += '\n    Path :    ' + self.data_set_location

        rez += '\n** New data set identifier <-> Initial data set identifier **'\
               + str(self.class_correlation)

        rez += '\n\n** Is valid : ' + str(self.is_valid()) + ' **'

        return rez

    ##########################################################################
    # cifar10

    @property
    def cifar10(self):
        return self._cifar10

    @cifar10.setter
    def cifar10(self,
                value: bool):
        if not isinstance(value, bool):
            raise ValueError('Cifar10 must be bool.')

        self._cifar10 = value

    ##########################################################################
    # imagenet

    @property
    def imagenet(self):
        return self._imagenet

    @imagenet.setter
    def imagenet(self,
                 value: bool):
        if not isinstance(value, bool):
            raise ValueError('ImageNet must be bool.')

        self._imagenet = value

    ##########################################################################
    # images

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self,
               value: bool):
        if not isinstance(value, bool):
            raise ValueError('Images must be bool.')

        self._images = value

    ##########################################################################
    # cifar10_train_ds

    @property
    def cifar10_train_ds(self):
        return self._cifar10_train_ds

    @cifar10_train_ds.setter
    def cifar10_train_ds(self,
                         value: bool):
        if not isinstance(value, bool):
            raise ValueError('Cifar10 train data set must be bool.')

        self._cifar10_train_ds = value

    ##########################################################################
    # cifar10_test_ds

    @property
    def cifar10_test_ds(self):
        return self._cifar10_test_ds

    @cifar10_test_ds.setter
    def cifar10_test_ds(self,
                        value: bool):
        if not isinstance(value, bool):
            raise ValueError('Cifar10 test data set must be bool.')

        self._cifar10_test_ds = value

    ##########################################################################
    # data_set_location

    @property
    def data_set_location(self):
        return self._data_set_location

    @data_set_location.setter
    def data_set_location(self,
                          value: str):
        if self._images and not fe.is_directory(value) \
                or not isinstance(value, str):
            raise ValueError('Data set location must be a string and also a '
                             'valid path.')

        self._data_set_location = value

    ##########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if self.cifar10 and not self.imagenet and not self.images \
                or not self.cifar10 and self.imagenet and not self.images \
                or not self.cifar10 and not self.imagenet and self.images:

            if self.cifar10:
                if not self.cifar10_train_ds and not self.cifar10_test_ds:
                    return False

            if self.images:
                if not fe.is_directory(self.data_set_location):
                    return False

            if not self.class_correlation.is_valid():
                return False

            return True
        else:
            return False

    ##########################################################################
