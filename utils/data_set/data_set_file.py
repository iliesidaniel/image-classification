import file_experts.file_expert as fe


class DataSetFile:

    def __init__(self):

        self._file_name = ''
        self._sha512 = ''
        self._number_of_examples = 0

    def __str__(self):

        rez = '\n---- Data set file ----\n'
        rez += '\nFile name          :    ' + self.file_name
        rez += '\nSHA512             :    ' + self.sha512
        rez += '\nNumber of examples :    ' + str(self.number_of_examples)
        rez += '\n-- Is valid : ' + str(self.is_valid()) + ' --'

        return rez

    ##########################################################################
    # file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(
            self,
            value: str):
        if not isinstance(value, str) or value == '':
            raise ValueError('File name must be string and not empty.')

        self._file_name = value

    ##########################################################################
    # sha512

    @property
    def sha512(self):
        return self._sha512

    @sha512.setter
    def sha512(
            self,
            value: str):
        if not isinstance(value, str) or value == '':
            raise ValueError('SHA512 must be string and not empty.')

        self._sha512 = value

    def update_sha512(
            self,

            path_to_file: str):
        """
        - Updates the file's SHA512.
        
        :param path_to_file: Path to the directory that contains the file.
        """

        file_name = path_to_file + '/' + self.file_name

        if fe.is_file(file_name):
            self._sha512 = fe.file_sha512(
                file_name
            )
        else:
            raise ValueError(self.file_name + ' does not exist.')

        print('\n====\n' + file_name + '\n' + str(self))

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
                or not isinstance(self.file_name, str) \
                or not isinstance(self.sha512, str):
            return False

        if self.number_of_examples < 0 \
                or self.file_name == '' \
                or self.sha512 == '':
            return False

        return True

    ##########################################################################

    def to_json(self):

        js = {
            'File name'          : self.file_name,
            'SHA512'             : self.sha512,
            'Number of examples' : self.number_of_examples,
        }

        return js

    ##########################################################################

    def from_json(
            self,

            js: {}):

        self.file_name = js['File name']
        self.sha512 = js['SHA512']
        self.number_of_examples = int(js['Number of examples'])

    ##########################################################################
