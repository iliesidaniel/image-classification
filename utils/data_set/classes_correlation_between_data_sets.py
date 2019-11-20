from utils.data_set.class_correlation_between_data_sets import ClassCorrelationBetweenDataSets
from copy import deepcopy


class ClassesCorrelationBetweenDataSets:

    def __init__(self):

        self._correlations = []

    def __str__(self):

        rez = '\n++++ Classes correlation between data sets ++++\n'

        for correlation in self._correlations:
            rez += str(correlation)

        rez += '\n++ Is valid : ' + str(self.is_valid()) + ' ++'

        return rez

    #########################################################################
    # Public methods

    def add(self,
            new_correlation: ClassCorrelationBetweenDataSets):
        """
        - Adds a new entry to the list if the new_correlation parameter is an
        instance of the ClassCorrelationBetweenDataSets class and also valid,
        otherwise will raise ValueError.

        :param new_correlation: ClassCorrelationBetweenDataSets instance.
        """

        if isinstance(new_correlation, ClassCorrelationBetweenDataSets) \
                and new_correlation.is_valid():
            self._correlations.append(new_correlation)
        else:
            raise ValueError('new_correlation parameter must be an instance '
                             'of ClassCorrelationBetweenDataSets and also it'
                             ' must be valid.')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~Get correlated identifier~~~~~~~~~~~~~~~~~~~~

    def get_new_correlation(
            self,

            new_identifier: int):
        """
        :param new_identifier: Class identifier in the new data set.

        :return: Correlated identifier.
        """

        for correlation in self._correlations:
            if str(correlation.identifier_in_old_data_set) == str(new_identifier):
                return correlation.identifier_in_new_data_set

        # raise TODO

    def get_old_correlation(
            self,

            old_identifier: int):
        """
        :param old_identifier: Class identifier in the initial data set.

        :return: Correlated identifier.
        """

        for correlation in self._correlations:
            if correlation.identifier_in_new_data_set == old_identifier:
                return correlation.identifier_in_old_data_set

        # raise TODO

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~Get correlated identifiers~~~~~~~~~~~~~~~~~~~

    def get_correlations(self):
        """
        :return: ClassCorrelationBetweenDataSets list
        """

        return deepcopy(self._correlations)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def clear(self):
        """
        - Clears the list.
        """

        self._correlations.clear()

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self._correlations:
            return False

        for correlation in self._correlations:
            if not isinstance(correlation, ClassCorrelationBetweenDataSets) \
                    or not correlation.is_valid():
                return False

        return True

    #########################################################################
