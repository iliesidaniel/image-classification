from utils.data_set.data_set_details import DataSetDetails
from utils.train.session_details import SessionDetails


import constants.create_data_set_constants as const
import file_experts.file_expert as fe


class DataSetValidator:

    @staticmethod
    def check_if_extract_is_needed():
        """
        :return:    - True if the extract is required.
                    - False otherwise.
        """

        cifar10_directory_exists = fe.is_directory(
            path=const.CIFAR10_DIRECTORY_PATH
        )

        if not cifar10_directory_exists \
                or not DataSetValidator.cifar10_files_exist_and_are_valid() \
                and cifar10_directory_exists:
            return True

        return False

    #########################################################################

    @staticmethod
    def check_if_download_is_needed():
        """
        :return:    - True if the download is required.
                    - False otherwise.
        """

        if fe.is_file(const.CIFAR10_ARCHIVE_PATH):
            # If the Cifar10 archive exists.

            file_md5sum = fe.file_md5sum(const.CIFAR10_ARCHIVE_PATH)

            if not const.CIFAR10_ARCHIVE_MD5SUM == file_md5sum:
                # If the Cifar10 archive is corrupted.
                fe.delete_file(const.CIFAR10_ARCHIVE_PATH)

                return True
        else:
            # If the Cifar10 archive does not exist.

            return True

        return False

    #########################################################################

    @staticmethod
    def cifar10_files_exist_and_are_valid():
        """
        - Checks if the Cifar10 files are valid.

        :return:    - True if the train and test data set file are valid.
                    - False otherwise.
        """

        for i in range(len(const.CIFAR10_FILE_SHA512)):
            if not fe.is_file(const.CIFAR10_FILE_PATHS[i]):
                return False

            file_sha512 = fe.file_sha512(const.CIFAR10_FILE_PATHS[i])
            correct_sha512 = const.CIFAR10_FILE_SHA512[i]

            if correct_sha512 != file_sha512:
                return False

        return True

    #########################################################################

    @staticmethod
    def data_set_and_session_are_compatible(
            data_set_details: DataSetDetails,
            session_details: SessionDetails):
        """
        - Check is a data set is compatible with a session.

        :param data_set_details: DataSetDetails
        :param session_details: SessionDetails

        :return:    - True if the data set and the session are compatible.
                    - False otherwise.
        """

        if data_set_details.number_of_classes \
                == session_details.number_of_classes:
            return True

        return False

    #########################################################################
