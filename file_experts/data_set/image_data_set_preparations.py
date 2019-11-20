from utils.data_set.initial_data_set_example import InitialDataSetExample
from utils.data_set.data_set_details import DataSetDetails
from utils.data_set.initial_data_set import InitialDataSet


import file_experts.file_expert as fe
import threading
import random


class ImageDataSetPreparations(threading.Thread):

    def __init__(
            self,

            initial_data_set_details: InitialDataSet,
            data_set_save_details: DataSetDetails,

            examples_list: []):
        """
        -

        :param initial_data_set_details: 
        :param data_set_save_details: 
        :param examples_list: 
        """

        super(ImageDataSetPreparations, self).__init__()

        self._initial_data_set_details = initial_data_set_details
        self._save_details = data_set_save_details

        self._examples_list = examples_list

    #########################################################################
    # Auxiliary methods

    def _find_class_examples(
            self,

            class_identifier: str,
            class_path: str):
        """
        - Adds all the examples for the class class_identifier to 
        _examples_list and sets the identifier to class_identifier.

        :param class_identifier: Class identifier.
        :param class_path: Path to the directory containing the images for
                           the class with the identifier class_identifier.

        :return: The number of images for the class class_identifier.
        """

        examples_path = fe.get_files(class_path)

        for example_path in examples_path:
            example = InitialDataSetExample()

            example.identifier = class_identifier
            example.path = class_path + '/' + example_path

            self._examples_list.append(example)

        return len(examples_path)

    def _determine_classes(self):
        """
        - Determined the path for all the images in the data set.
        """

        data_set_directory = self._initial_data_set_details.data_set_location
        correlations = self._initial_data_set_details.class_correlation
        classes = fe.get_directories(directory_path=data_set_directory)

        for class_identifier in classes:
            new_class_identifier = correlations.get_new_correlation(
                new_identifier=class_identifier
            )
            class_path = data_set_directory + '/' + class_identifier

            number_of_examples = self._find_class_examples(
                class_identifier=new_class_identifier,
                class_path=class_path
            )

            self._save_details.classes.update_number_of_examples_for_class(
                examples_added=number_of_examples,
                identifier=new_class_identifier
            )

    #########################################################################
    # Public methods

    def run(self):
        self._determine_classes()

    @staticmethod
    def image_distribution_in_files(
            number_of_files: int,
            examples_list: []):
        """
        - Shuffles the images and distributes them equal in number_of_files
        lists.

        :param number_of_files: The number of files in which the new data
                                set will be saved.
        :param examples_list:   The InitialDataSetExample list that holds
                                the details of all the images.

        :return: - List of size number_of_files, each entry in the list
                 holds a list with InitialDataSetExample that will be
                 stored in a file.
        """

        random.seed(9280534)
        # random.seed(572281)
        random.shuffle(examples_list)

        split_length = int(len(examples_list) / number_of_files)
        split_difference = len(examples_list) % number_of_files
        split_start = 0

        image_distribution = []

        for file_number in range(number_of_files):
            split_end = split_start + split_length

            if file_number < split_difference:
                split_end += 1

            image_distribution.append(
                examples_list[split_start:split_end]
            )

            split_start = split_end

        return image_distribution

    #########################################################################
