from file_experts.data_set.data_set_validator import DataSetValidator
from file_experts.data_set import data_set_creator

from time import sleep


import constants.create_data_set_constants as const
import file_experts.file_expert as fe
import urllib.request
import threading
import tarfile


class Cifar10DataSetPreparations(threading.Thread):
    """
    - Makes sure the Cifar 10 data set files are present and intact.
    - If required it can download the Cifar 10 data set and / or extract
    the data set.
    """

    def __init__(
            self,

            progress_update_method):
        """
        :param progress_update_method: GUI method that updates the download
                                       progress.
        """

        super(Cifar10DataSetPreparations, self).__init__()

        self._progress_update_method = progress_update_method

    #########################################################################
    # Helper methods

    def _make_sure_the_required_files_exist(self):
        """
        - Makes sure that the Cifar10 files exist and are valid.
        """

        if not fe.is_directory(const.CIFAR10_SAVE_LOCATION):
            fe.crete_directory(const.CIFAR10_SAVE_LOCATION)
            if self._download_cifar10():
                self._extract_cifar10()
        else:
            if DataSetValidator.check_if_extract_is_needed():
                if DataSetValidator.check_if_download_is_needed():
                    if not self._download_cifar10():
                        return

                self._extract_cifar10()

    def _download_cifar10(self):
        """
        - Downloads Cifar10 binary version.
        """

        number_of_tries = 0

        while number_of_tries < const.CIFAR10_DOWNLOAD_NUMBER_OF_TRIES:
            try:
                urllib.request.urlretrieve(
                    const.CIFAR10_DOWNLOAD_LINK,
                    const.CIFAR10_ARCHIVE_PATH,
                    self._update_download_progress
                )

                return True
            except Exception as _:
                data_set_creator.cifar10_download_try_failed = True
                sleep(60)

            number_of_tries += 1

        data_set_creator.cifar10_download_failed = True
        return False

    def _update_download_progress(
            self,
            count,
            block_size,
            total_size):
        """ 
        - Calls the download progress update method, passing the percent of
        the progress.
        """

        self._progress_update_method(
            int(count * block_size / float(total_size) * 100)
        )

    @staticmethod
    def _extract_cifar10():
        """
        - Extracts the Cifar 10 data set archive.
        """

        with tarfile.open(const.CIFAR10_ARCHIVE_PATH, 'r:gz') as archive:
            archive.extractall(const.CIFAR10_SAVE_LOCATION)

    #########################################################################
    # Public methods

    def run(self):
        """
        - Call this method to start the Cifar 10 data set preparations.
        """

        self._make_sure_the_required_files_exist()

    #########################################################################
