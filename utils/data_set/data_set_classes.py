from project_exceptions.data_set_exceptions import CorruptMainDataSetFile
from utils.data_set.data_set_class import DataSetClass


class DataSetClasses:

    def __init__(self):

        self._data_set_classes = []

    def __str__(self):

        rez = '\n++++ Data set classes ++++\n'

        for data_set_entry in self._data_set_classes:
            rez += str(data_set_entry)

        rez += '\n++ Is valid : ' + str(self.is_valid()) + ' ++'

        return rez

    #########################################################################
    # Public methods

    def add(self,
            new_class: DataSetClass):
        """
        - Adds a new entry to the list if the new_class parameter is an 
        instance of the DataSetClass class and also valid.
        
        :param new_class: DataSetClass instance.
        """

        if isinstance(new_class, DataSetClass) and new_class.is_valid():
            self._data_set_classes.append(new_class)
        else:
            raise ValueError('new_class parameter must be an instance of the'
                             ' DataSetClass class and also it must be valid')

    def update_number_of_examples_for_class(
            self,
            identifier: int,
            examples_added: int):
        """
        - Updates the number of examples that are stored in the data set for
        the class identified by identifier.

        :param identifier: Class identifier.
        :param examples_added: How many examples were added.
        """

        for data_set_class in self._data_set_classes:
            if data_set_class.identifier == identifier:
                data_set_class.number_of_examples += examples_added

    def get_number_of_classes(self):
        """
        :return: Returns the number of classes in the data set.
        """

        return len(self._data_set_classes)

    def get_data_set_classes(self):
        """
        :return: DataSetClass list
        """

        return self._data_set_classes

    def clear(self):
        """
        - Clears the list.
        """

        self._data_set_classes.clear()

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self._data_set_classes:
            return False

        for data_set_entry in self._data_set_classes:
            if not isinstance(data_set_entry, DataSetClass):
                return False
            elif not data_set_entry.is_valid():
                return False

        return True
    ##########################################################################

    def to_json(self):
        """ Converts object data to JSON format."""

        js = {}

        for index in range(len(self._data_set_classes)):
            class_id = 'Class ' + str(index)
            class_js = self._data_set_classes[index].to_json()

            js.update(
                {
                    class_id
                    :
                    class_js
                }
            )

        return js

    ##########################################################################

    def from_json(
            self,

            js: {},

            number_of_classes: int):
        """ Converts JSON format object data."""

        self.clear()

        if len(js) != number_of_classes:
            raise CorruptMainDataSetFile(
                'The details about at least one of the data set classes are '
                'missing.'
            )

        for index in range(number_of_classes):
            class_id = 'Class ' + str(index)

            tmp = DataSetClass()
            tmp.from_json(js[class_id])

            self._data_set_classes.append(tmp)

    ##########################################################################
