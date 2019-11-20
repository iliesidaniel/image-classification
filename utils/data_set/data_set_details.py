from utils.data_set.data_set_classes import DataSetClasses
from utils.data_set.data_set_files import DataSetFiles


class DataSetDetails:

    def __init__(self,

                 path_to_files: str):
        """
        :param path_to_files: Path to the directory that contains the files.
        """

        self._name = ''
        self._description = ''

        self._image_size = -1
        self._number_of_files = -1
        self._number_of_classes = 0
        self._number_of_examples = 0

        self.classes = DataSetClasses()
        self.data_set_files = DataSetFiles(
            path_to_files=path_to_files
        )

    def __str__(self):
        rez = '\n#### Data set details ####\n'
        rez += '   \nName               :    ' + self.name
        rez += '   \nDescription        :    ' + self.description
        rez += '   \nImage size         :    ' + str(self.image_size)
        rez += '   \nNumber of files    :    ' + str(self.number_of_files)
        rez += '   \nNumber of classes  :    ' + str(self.number_of_classes)
        rez += '   \nNumber of examples :    ' + str(self.number_of_examples)
        rez += str(self.classes)
        rez += str(self.data_set_files)

        rez += '\n## Is valid : ' + str(self.is_valid()) + ' ##'

        return rez

    #########################################################################
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

    #########################################################################
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

    #########################################################################
    # image_size

    @property
    def image_size(self):
        return self._image_size

    @image_size.setter
    def image_size(
            self,
            value: int):
        if not isinstance(value, int) or value < 10:
            raise ValueError('The image size must be integer and >= 10.')

        self._image_size = value

    #########################################################################
    # number_of_files

    @property
    def number_of_files(self):
        return self._number_of_files

    @number_of_files.setter
    def number_of_files(
            self,
            value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('The number of files must be integer and above '
                             '0.')

        self._number_of_files = value

    #########################################################################
    # number_of_classes

    @property
    def number_of_classes(self):
        return self._number_of_classes

    @number_of_classes.setter
    def number_of_classes(
            self,
            value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('The number of classes must be integer and '
                             'above 0.')

        self._number_of_classes = value

    #########################################################################
    # number_of_examples

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

    #########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self.data_set_files.is_valid():
            return False

        if not self.classes.is_valid():
            return False

        if not isinstance(self.number_of_examples, int) \
                or not isinstance(self.number_of_files, int) \
                or not isinstance(self.number_of_classes, int) \
                or not isinstance(self.description, str) \
                or not isinstance(self.image_size, int) \
                or not isinstance(self.name, str):
            return False

        if self.number_of_examples < 1 \
                or self.number_of_classes < 1 \
                or self.number_of_files < 1 \
                or self.description == '' \
                or self.image_size < 10 \
                or self.name == '':
            return False

        return True

    #########################################################################

    def to_json(self):

        data_set_files = self.data_set_files.to_json()
        classes = self.classes.to_json()

        js = {
            'Name'              : self.name,
            'Description'       : self.description,
            'Number of examples': self.number_of_examples,
            'Number of classes' : self.classes.get_number_of_classes(),
            'Number of files'   : self.number_of_files,
            'Image size'        : self.image_size,

            'Classes'           : classes,
            'Data set files'    : data_set_files,
        }

        return js

    #########################################################################

    def from_json(
            self,

            js: {}):

        self.name = js['Name']
        self.description = js['Description']
        self.number_of_examples = int(js['Number of examples'])
        self.number_of_classes = int(js['Number of classes'])
        self.number_of_files = int(js['Number of files'])
        self.image_size = int(js['Image size'])

        self.classes.from_json(
            number_of_classes=self.number_of_classes,
            js=js['Classes']
        )
        self.data_set_files.from_json(
            number_of_files=self.number_of_files,
            js=js['Data set files']
        )

    #########################################################################
