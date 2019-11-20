import file_experts.file_expert as fe


class NewFileDetails:

    def __init__(self):

        self._directory_path = ''
        self._file_name = ''
        self._description = ''

    def __str__(self):

        rez = '\n---- New file details ----\n'
        rez += '\nDirectory path :    ' + self.directory_path
        rez += '\nName           :    ' + self.file_name
        rez += '\nDescription    :    ' + self.description
        rez += '\n-- Is valid : ' + str(self.is_valid()) + ' --'

        return rez

    ##########################################################################
    # directory_path

    @property
    def directory_path(self):
        return self._directory_path

    @directory_path.setter
    def directory_path(
            self,
            value: str):
        self._directory_path = value

    ##########################################################################
    # file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self,
                  value: str):
        self._file_name = value

    ##########################################################################
    # description

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,
                    value: str):
        self._description = value

    ##########################################################################

    def is_valid(self):
        """
        - Checks if valid

        :return: - True if valid
                 - False otherwise
        """

        if not isinstance(self.directory_path, str) \
                or not isinstance(self.description, str) \
                or not isinstance(self.file_name, str):
            return False

        if self.directory_path == '' \
                or self.description == '' \
                or self.file_name == '':
            return False

        file_path = self.directory_path + '/' + self.file_name

        if not fe.is_directory(self.directory_path) \
                or not fe.is_file(file_path):
            return False

        return True

    ##########################################################################
