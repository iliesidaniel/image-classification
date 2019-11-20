from project_exceptions.data_set_exceptions import CorruptMainDataSetFile
from utils.data_set.data_set_file import DataSetFile


import file_experts.file_expert as fe


class DataSetFiles:

    def __init__(self,

                 path_to_files):
        """
        
        :param path_to_files: Path to the directory that contains the files.
        """

        self._path_to_files = path_to_files
        self._data_set_files = []

    def __str__(self):

        rez = '\n++++ Data set files ++++\n'

        for file in self._data_set_files:
            rez += str(file)

        rez += '\n++ Is valid : ' + str(self.is_valid()) + ' ++'

        return rez

    #########################################################################
    # Public methods

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SHA512 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def update_files_sha512(self):
        """
        - Updates SHA512 for all files.
        """

        for file_index in range(len(self._data_set_files)):
            self._data_set_files[file_index].update_sha512(
                path_to_file=self._path_to_files
            )

    def check_files_sha51(self):
        """
        - Checks the SHA512 sum for all the data set files.

        :return:    - True if the saved sum is the same with the calculated
                      one.
                    - False otherwise.
        """

        for file in self._data_set_files:
            file_path = self._path_to_files + '/' + file.file_name

            if fe.file_sha512(file_name=file_path) != file.sha512:
                return False

        return True

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Data set files ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def get_data_set_files(self):
        """
        :return: DataSetFile list
        """

        return self._data_set_files

    def get_data_set_file_paths(self):
        """
        :return: The paths for all the data set files.
        """

        paths = []

        for file_index in range(len(self._data_set_files)):
            paths.append(
                self._path_to_files
                + '/'
                + self._data_set_files[file_index].file_name
            )

        return paths

    def clear(self):
        """
        - Clears the list.
        """

        self._data_set_files.clear()

    def check_file_existence(self):
        """
        - Checks if all the data set files exist.

        :return:    - True if all the files exist.
                    - False otherwise.
        """

        for file in self._data_set_files:
            file_path = self._path_to_files + '/' + file.file_name

            if not fe.is_file(path=file_path):
                return False

        return True

    def update_number_of_examples_in_file(
            self,

            file_index: int,
            examples_added: int):
        """
        :param file_index: The index of the file in which the examples were
                           added.
        :param examples_added: How many examples were added.
        """

        self._data_set_files[file_index].number_of_examples += examples_added

    def create_data_set_file_names(
            self,

            number_of_files):
        """
        
        :param number_of_files: Number of files.
        """

        self.clear()

        for file_index in range(number_of_files):
            data_set_file = DataSetFile()

            data_set_file.file_name = str(file_index) + '.txt'

            self._data_set_files.append(
                data_set_file
            )

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Valid ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not self._data_set_files:
            return False

        for file in self._data_set_files:
            if not isinstance(file, DataSetFile):
                return False
            elif not file.is_valid():
                return False

        return True

    #########################################################################

    def to_json(self):
        """ Converts object data to JSON format."""

        self.update_files_sha512()

        js = {}

        for index in range(len(self._data_set_files)):
            class_id = 'Files ' + str(index)
            class_js = self._data_set_files[index].to_json()

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

            number_of_files: int):
        """ Converts JSON format object data."""

        self.clear()

        if len(js) != number_of_files:
            raise CorruptMainDataSetFile(
                'The details about at least one of the data set files are '
                'missing.'
            )

        for index in range(number_of_files):
            class_id = 'Files ' + str(index)

            tmp = DataSetFile()
            tmp.from_json(js[class_id])

            self._data_set_files.append(tmp)

    ##########################################################################
