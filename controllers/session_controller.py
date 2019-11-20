from controllers.data_set_controller import DataSetController
from utils.data_set.data_set_details import DataSetDetails

from utils.train.session_details import SessionDetails
from utils.new_file_details import NewFileDetails

from file_experts.session_rw import SessionRW


import constants.global_constants as g_const
import constants.cnn_constants as cnn_const

import file_experts.file_expert as fe

import tensorflow as tf


class SessionController:

    #########################################################################
    # Write

    @staticmethod
    def process_and_save_the_input_for_a_new_session(
            session_file_details: NewFileDetails,
            session_details: SessionDetails,
    ):

        session_details.name = session_file_details.file_name
        session_details.description = session_file_details.description
        session_details.session_current_path = \
            session_file_details.directory_path \
            + '/' \
            + session_file_details.file_name

        data_set_details = DataSetController.read_main_data_set_file(
            file_path=session_details.main_data_set_file
        )

        session_details.number_of_classes = data_set_details.classes.get_number_of_classes()
        session_details.data_set_name = data_set_details.name
        session_details.classes = data_set_details.classes

        SessionController.write_session_files(
            session_file_details=session_file_details,
            session_details=session_details
        )

        return session_details, data_set_details

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @staticmethod
    def _copy_data_set(
            session_details: SessionDetails):
        """
        - Writes the session files.

        :param session_details: SessionDetails instance.
        """

        data_set_details = DataSetController.read_main_data_set_file(
            file_path=session_details.main_data_set_file
        )

        fe.crete_directory(
            directory_path=session_details.data_set_directory
        )

        fe.crete_directory(
            directory_path=session_details.checkpoints_directory
        )

        fe.copy_file(
            file_path=session_details.main_data_set_file,
            destination_path=session_details.data_set_directory
        )

        session_details.main_data_set_file = \
            session_details.data_set_directory \
            + '/' \
            + data_set_details.name \
            + g_const.GLOBAL_DATA_SET_FILE_EXTENSION

        paths = data_set_details.data_set_files.get_data_set_file_paths()

        for data_set_file in paths:
            fe.copy_file(
                file_path=data_set_file,
                destination_path=session_details.data_set_directory
            )

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @staticmethod
    def write_session_files(
            session_file_details: NewFileDetails,
            session_details: SessionDetails):
        """
        - Writes the session files.
        
        :param session_file_details: NewFileDetails instance.
        :param session_details: SessionDetails instance.
        """

        directory_path = \
            session_file_details.directory_path \
            + '/' \
            + session_file_details.file_name

        fe.crete_directory(directory_path=directory_path)

        session_file_details.directory_path = directory_path

        session_details_file_path = \
            session_file_details.directory_path \
            + '/' \
            + session_file_details.file_name \
            + g_const.GLOBAL_SESSION_FILE_EXTENSION

        SessionRW.write_session_details_file(
            session_details_file_path=session_details_file_path,
            session_details=session_details
        )

        SessionController._copy_data_set(
            session_details=session_details
        )

    #########################################################################
    # Read

    @staticmethod
    def read_main_session_file(
            session_file_path: str):
        """
        - Reads the file that contains the session details.
        
        :param session_file_path: Path to the file that contains the session
                                  details.

        :return: 
        """

        if fe.is_file(path=session_file_path):
            session_details = SessionRW.read_main_session_file(
                session_file_path=session_file_path
            )

            session_details.session_current_path = fe.remove_last_entry_from_path(
                path=session_file_path
            )

            session_details.main_data_set_file = \
                session_details.data_set_directory \
                + '/' \
                + session_details.data_set_name \
                + g_const.GLOBAL_DATA_SET_FILE_EXTENSION

            return session_details
        else:
            raise FileNotFoundError(
                '"'
                + session_file_path
                + '" does not exists.'
            )

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @staticmethod
    def get_examples_for_train_session(
            session_details: SessionDetails):

        main_file_path = session_details.main_data_set_file

        data_set_details = DataSetController.read_main_data_set_file(
            file_path=main_file_path
        )

        if session_details.data_augmentation.crop and False:        # TODO
            label, image = DataSetController.read_data_set_files_without_image_resize(
                desired_image_size=session_details.image_size,
                data_set_details=data_set_details
            )

            image = tf.random_crop(
                value=image,
                size=[
                    session_details.image_size,
                    session_details.image_size,
                    3
                ]
            )
        else:
            label, image = DataSetController.read_data_set_files_and_resize_images(
                desired_image_size=session_details.image_size,
                data_set_details=data_set_details
            )

        if session_details.data_augmentation.flip_left_right:
            image = tf.image.random_flip_left_right(
                image=image
            )

        if session_details.data_augmentation.brightness and False:        # TODO
            image = tf.image.random_brightness(
                image=image,
                max_delta=63
            )

        if session_details.data_augmentation.contrast:
            image = tf.image.random_contrast(
                image=image,
                lower=0.2,
                upper=1.8
            )

        image.set_shape(
            [
                session_details.image_size,
                session_details.image_size,
                3
            ]
        )

        min_size = int(
            data_set_details.number_of_examples
            * cnn_const.CNN_SHUFFLE_BATCH_MIN_SIZE_COEFFICIENT
        )

        capacity = (
            cnn_const.CNN_SHUFFLE_BATCH_CAPACITY_COEFFICIENT
            * session_details.examples_per_batch
        ) + min_size

        image_batch, label_batch = tf.train.shuffle_batch(
            num_threads=cnn_const.CNN_SHUFFLE_BATCH_NUMBER_OF_THREADS,
            batch_size=session_details.examples_per_batch,
            min_after_dequeue=min_size,
            tensors=[image, label],
            capacity=capacity
        )

        return label_batch, image_batch

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @staticmethod
    def get_examples_for_test_session(
            session_details: SessionDetails,
            test_data_set_details: DataSetDetails):

        label, image = DataSetController.read_data_set_files_and_resize_images(
            desired_image_size=session_details.image_size,
            data_set_details=test_data_set_details
        )

        min_size = int(
            test_data_set_details.number_of_examples
            * cnn_const.CNN_SHUFFLE_BATCH_MIN_SIZE_COEFFICIENT
        )

        capacity = (
            cnn_const.CNN_SHUFFLE_BATCH_CAPACITY_COEFFICIENT
            * session_details.examples_per_batch
        ) + min_size

        image_batch, label_batch = tf.train.batch(
            num_threads=cnn_const.CNN_SHUFFLE_BATCH_NUMBER_OF_THREADS,
            batch_size=session_details.examples_per_batch,
            tensors=[image, label],
            capacity=capacity
        )

        return label_batch, image_batch

    #########################################################################
