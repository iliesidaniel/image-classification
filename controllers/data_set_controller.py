from project_exceptions.data_set_exceptions import CorruptDataSetFiles, DataSetImagesTooSmall

from file_experts.data_set.data_set_creator import DataSetCreator
from file_experts.data_set.data_set_reader import DataSetReader

from utils.data_set.initial_data_sets import InitialDataSets
from utils.data_set.data_set_details import DataSetDetails
from utils.data_set.data_set_classes import DataSetClasses
from utils.new_file_details import NewFileDetails


import file_experts.file_expert as fe


class DataSetController:
    """
    - Use this to write and read data sets.
    """

    #########################################################################
    # Write

    @staticmethod
    def create_new_data_set(
            initial_data_sets: InitialDataSets,
            creation_details: NewFileDetails,
            data_set_classes: DataSetClasses,

            data_set_creation_gui,

            number_of_files: int,
            image_size: int):
        """
        - Creates a new data set.

        :param initial_data_sets: InitialDataSets instance.
        :param creation_details: NewFileDetails instance.
        :param data_set_classes: DataSetClasses instance.

        :param data_set_creation_gui: CreateDataSetGUI instance, it will be
                                      used to call the progress update
                                      methods.

        :param number_of_files: The number of files into which the data set
                                will be saved.
        :param image_size: The image size in the new data set.
        """

        directory_path = \
            creation_details.directory_path \
            + '/' \
            + creation_details.file_name

        fe.crete_directory(directory_path=directory_path)

        creation_details.directory_path = directory_path

        save_details = DataSetDetails(
            path_to_files=creation_details.directory_path
        )

        save_details.number_of_classes = data_set_classes.get_number_of_classes()
        save_details.description = creation_details.description
        save_details.number_of_files = number_of_files
        save_details.name = creation_details.file_name
        save_details.classes = data_set_classes
        save_details.image_size = image_size
        save_details.number_of_examples = 0

        save_details.data_set_files.create_data_set_file_names(
            number_of_files=save_details.number_of_files
        )

        data_set_creator = DataSetCreator(
            data_set_creation_gui=data_set_creation_gui,
            initial_data_sets=initial_data_sets,
            creation_details=creation_details,
            data_set_details=save_details,
        )

        data_set_creator.create_data_set()

    #########################################################################
    # Read

    @staticmethod
    def read_main_data_set_file(
            file_path: str):
        """
        - Reads the main file of a data set.
        - Raises:
                    * FileNotFoundError
                    * CorruptMainDataSetFile

        :param file_path: Path to a main data set file.

        :return: DataSetDetails instance.
        """

        if fe.is_file(path=file_path):
            data_set_details = DataSetReader.read_main_data_set_file(
                path=file_path
            )

            return data_set_details
        else:
            raise FileNotFoundError(
                '"'
                + file_path
                + '" does not exists.'
            )

    @staticmethod
    def read_data_set_files_without_image_resize(
            data_set_details: DataSetDetails,
            desired_image_size: int):
        """
        - Reads the data set files (TFRecords).
        - Raises:
                    * FileNotFoundError
                    * CorruptDataSetFiles
                    * DataSetImagesTooSmall

        :param data_set_details: Data set details.
        :param desired_image_size: - The desired image size.
                                   - If the desired size is greater than the
                                   size of the images in the data set
                                   DataSetImagesTooSmall will be raised.

        :return: label, image
        """

        DataSetController._data_set_files_read_checks(
            desired_image_size=desired_image_size,
            data_set_details=data_set_details
        )

        paths = data_set_details.data_set_files.get_data_set_file_paths()

        return DataSetReader.read_tfrecords(
            data_set_image_size=data_set_details.image_size,
            paths=paths
        )

    @staticmethod
    def read_data_set_files_and_resize_images(
            data_set_details: DataSetDetails,
            desired_image_size: int):
        """
        - Reads the data set files (TFRecords).
        - Raises:
                    * FileNotFoundError
                    * CorruptDataSetFiles
                    * DataSetImagesTooSmall

        :param data_set_details: Data set details.
        :param desired_image_size: - The desired image size.
                                   - If the desired size is greater than the
                                   size of the images in the data set
                                   DataSetImagesTooSmall will be raised.

        :return: label, image
        """

        DataSetController._data_set_files_read_checks(
            desired_image_size=desired_image_size,
            data_set_details=data_set_details
        )

        paths = data_set_details.data_set_files.get_data_set_file_paths()

        if desired_image_size == data_set_details.image_size:
            return DataSetReader.read_tfrecords(
                data_set_image_size=data_set_details.image_size,
                paths=paths
            )
        else:
            return DataSetReader.read_tfrecords_and_resize(
                data_set_image_size=data_set_details.image_size,
                new_image_size=desired_image_size,
                paths=paths
            )

    #########################################################################
    # Helper methods

    @staticmethod
    def _data_set_files_read_checks(
            data_set_details: DataSetDetails,
            desired_image_size: int):
        """
        - Reads the data set files (TFRecords).
        - Raises:
                    * FileNotFoundError
                    * CorruptDataSetFiles
                    * DataSetImagesTooSmall

        :param data_set_details: Data set details.
        :param desired_image_size: - The desired image size.
                                   - If the desired size is greater than the
                                   size of the images in the data set
                                   DataSetImagesTooSmall will be raised.
        """

        data_set_files = data_set_details.data_set_files

        if not data_set_files.check_file_existence():
            raise FileNotFoundError(
                'At least one of the data set files does not exist.'
            )

        if not data_set_files.check_files_sha51():
            raise CorruptDataSetFiles(
                'At least one of the data set files is corrupt.'
            )

        if desired_image_size > data_set_details.image_size:
            raise DataSetImagesTooSmall(
                'Incompatible data set, the size of the images in the data '
                'set is smaller than the desired size.'
            )

    #########################################################################
