

class DataSetClass:

    def __init__(self):

        self._class_name = ''
        self._identifier = -1
        self._number_of_examples = 0

    def __str__(self):

        rez = '\n---- Data set class ----\n'
        rez += '\nClass name         :    ' + self.class_name
        rez += '\nIdentifier         :    ' + str(self.identifier)
        rez += '\nNumber of examples :    ' + str(self.number_of_examples)
        rez += '\n-- Is valid : ' + str(self.is_valid()) + ' --'

        return rez

    ##########################################################################
    # class_name

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(
            self,
            value: str):
        if not isinstance(value, str) or value == '':
            raise ValueError('Class name must be string and not empty.')

        self._class_name = value

    ##########################################################################
    # identifier

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(
            self,
            value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Identifier must be integer and >= 0.')

        self._identifier = value

    ##########################################################################
    # examples_per_batch

    @property
    def number_of_examples(self):
        return self._number_of_examples

    @number_of_examples.setter
    def number_of_examples(
            self,
            value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('The number of examples must be integer and '
                             'above 0.')

        self._number_of_examples = value

    ##########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not isinstance(self.number_of_examples, int) \
                or not isinstance(self.identifier, int) \
                or not isinstance(self.class_name, str):
            return False

        if self.number_of_examples < 0 \
                or self.identifier < 0 \
                or self.class_name == '':
            return False

        return True

    ##########################################################################

    def to_json(self):

        js = {
            'Class name'         : self.class_name,
            'Identifier'         : self.identifier,
            'Number of examples' : self.number_of_examples,
        }

        return js

    ##########################################################################

    def from_json(
            self,

            js: {}):

        self.class_name = js['Class name']
        self.identifier = js['Identifier']
        self.number_of_examples = int(js['Number of examples'])

    ##########################################################################
