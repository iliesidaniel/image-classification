from project_exceptions.data_set_exceptions import CorruptMainDataSetFile
from utils.data_set.data_set_details import DataSetDetails

from json import JSONDecodeError


import file_experts.file_expert as fe

import tensorflow as tf
import json


class DataSetReader:

    #########################################################################
    # Public methods

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ TFRecords ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @staticmethod
    def read_tfrecords(
            paths: [],

            data_set_image_size: int):
        """
        - Returns labels and images from the TFRecords files.

        :param data_set_image_size: Image size in the data set.
        :param paths: List with the paths to the TFRecords files.

        :return: labels, images
        """

        filename_queue = tf.train.string_input_producer(paths)

        reader = tf.TFRecordReader()

        _, serialized_example = reader.read(filename_queue)

        features = tf.parse_single_example(
            serialized_example,

            features={
                'image': tf.FixedLenFeature([], tf.string),
                'label': tf.FixedLenFeature([], tf.int64)
            }
        )

        image = tf.decode_raw(
            features['image'],
            tf.uint8
        )

        label = tf.cast(
            features['label'],
            tf.int32
        )

        image = tf.cast(image, tf.float32)

        image = tf.reshape(
            image,
            [
                data_set_image_size,
                data_set_image_size,
                3
            ]
        )

        image.set_shape(
            [
                data_set_image_size,
                data_set_image_size,
                3
            ]
        )

        return label, image

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ Main data set file ~~~~~~~~~~~~~~~~~~~~~~~~~

    @staticmethod
    def read_tfrecords_and_resize(
            paths: [],

            data_set_image_size: int,

            new_image_size: int):
        """
        - Returns labels and images from the TFRecords files.

        :param paths: List with the paths to the TFRecords files.
        :param data_set_image_size: Image size in the data set.
        :param new_image_size: The size to which to resize the image.

        :return: labels, images
        """

        label, image = DataSetReader.read_tfrecords(
            data_set_image_size=data_set_image_size,
            paths=paths
        )

        resized_image = tf.image.resize_image_with_crop_or_pad(
            image,
            new_image_size,
            new_image_size
        )

        image = tf.image.per_image_standardization(resized_image)
        image.set_shape([new_image_size, new_image_size, 3])

        return label, image

    @staticmethod
    def read_main_data_set_file(
            path: str):
        """
        - Reads the main data set file.

        :param path: Path to the main data set file.

        :return: DataSetSaveDetails instance.
        """

        try:
            with open(path) as data_file:
                data_loaded = json.load(data_file)

            data_set_path = fe.remove_last_entry_from_path(path)

            data_set_details_from_file = DataSetDetails(
                path_to_files=data_set_path
            )

            data_set_details_from_file.from_json(data_loaded)

            return data_set_details_from_file
        except (KeyError, JSONDecodeError) as exception:
            raise CorruptMainDataSetFile(
                'The main data set file is corrupt.'
            ) from exception


#############################################################################
