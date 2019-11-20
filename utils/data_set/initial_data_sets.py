from utils.data_set.initial_data_set import InitialDataSet
from copy import deepcopy


class InitialDataSets:

    def __init__(self):

        self._initial_data_sets = []

    def __str__(self):

        rez = '\n^^^^ Initial data sets ^^^^\n'

        for initial_data_set in self._initial_data_sets:
            rez += '\n **************************************************************** \n'
            rez += str(initial_data_set)

        rez += '\n^^ Is valid : ' + str(self.is_valid()) + ' ^^'

        return rez

    #########################################################################
    # Public methods

    def add(self,
            new_data_set: InitialDataSet):
        """
        - Adds a new entry to the list if the new_data_set parameter is an
        instance of the InitialDataSet class and also valid, otherwise will
        raise ValueError.

        :param new_data_set: InitialDataSet instance.
        """

        if isinstance(new_data_set, InitialDataSet) \
                and new_data_set.is_valid():
            self._initial_data_sets.append(new_data_set)
        else:
            raise ValueError('new_data_set parameter must be an instance of '
                             'InitialDataSet and also it must be valid.')

    def get_correlations(self):
        """
        :return: InitialDataSet list
        """

        return deepcopy(self._initial_data_sets)

    def clear(self):
        """
        - Clears the list.
        """

        self._initial_data_sets.clear()

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self._initial_data_sets:
            return False

        cifar10_train_ds = False
        cifar10_test_ds = False

        for initial_data_set in self._initial_data_sets:
            if not isinstance(initial_data_set, InitialDataSet):
                return False
            elif not initial_data_set.is_valid():
                return False
            elif initial_data_set.cifar10:
                # Checks if Cifar10 train ds was selected multiple times.
                if initial_data_set.cifar10_train_ds:
                    if cifar10_train_ds:
                        return False

                    cifar10_train_ds = True

                # Checks if Cifar10 test ds was selected multiple times.
                if initial_data_set.cifar10_test_ds:
                    if cifar10_test_ds:
                        return False

                    cifar10_test_ds = True

        return True

    #########################################################################
