from file_experts.data_set.cifar10_data_set_preparations import Cifar10DataSetPreparations
from file_experts.data_set.image_data_set_preparations import ImageDataSetPreparations
from file_experts.data_set.cifar10_reader import Cifar10Reader
from file_experts.data_set.image_reader import ImageReader

from utils.call_method_in_new_thread import CallMethodInNewThread

from utils.data_set.initial_data_sets import InitialDataSets
from utils.data_set.initial_data_set import InitialDataSet
from utils.data_set.data_set_details import DataSetDetails

from utils.new_file_details import NewFileDetails


import file_experts.data_set.to_tf_example as to_tf_example
import constants.create_data_set_constants as const
import constants.global_constants as g_const

import tensorflow as tf
import numpy as np
import json


cifar10_download_try_failed = False
cifar10_download_failed = False


class DataSetCreator:
    """
    - Writes all the data set files.
    """

    def __init__(
            self,

            data_set_details: DataSetDetails,
            initial_data_sets: InitialDataSets,
            creation_details: NewFileDetails,

            data_set_creation_gui):
        """
        - Creates a new data set.

        :param initial_data_sets: InitialDataSets instance.
        :param creation_details: NewFileDetails instance.
        :param data_set_details: DataSetSaveDetails instance.

        :param data_set_creation_gui: CreateDataSetGUI instance, it will be
                                      used to call the progress update
                                      methods.
        """

        self._data_set_creation_gui = data_set_creation_gui
        self._initial_data_sets = initial_data_sets
        self._data_set_details = data_set_details
        self._creation_details = creation_details

        self._number_of_files = self._data_set_details.number_of_files
        self._data_set_files = self._data_set_details.data_set_files
        self._height = self._data_set_details.image_size
        self._width = self._data_set_details.image_size

        self._file_path = self._data_set_files.get_data_set_file_paths()
        self._examples_list = []
        self.writer = []

    #########################################################################
    # File writing methods

    # ~~~~~~~~~~~~~~~~~~~~~ Main data set file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _write_main_data_set_file(self):
        """
        - Writes the main data set file.
        """

        data_set_details_file_name = \
            self._creation_details.directory_path \
            + '/' \
            + self._creation_details.file_name \
            + g_const.GLOBAL_DATA_SET_FILE_EXTENSION

        json_str = self._data_set_details.to_json()

        with open(data_set_details_file_name, 'w') as outfile:
            json.dump(
                json_str, outfile,
                sort_keys=False,
                indent=4,
                separators=(',', ': '),
                ensure_ascii=False
            )

    # ~~~~~~~~~~~~~~~~~~~~~ TFRecord files ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _write_image_data_set(self):
        """
        - Writes the image examples to TFRecord files.
        """

        distribution = ImageDataSetPreparations.image_distribution_in_files(
            number_of_files=self._number_of_files,
            examples_list=self._examples_list
        )

        one_percent = len(self._examples_list) / 100

        total_progress = 0

        for file_index in range(self._number_of_files):
            number_of_examples = len(distribution[file_index])

            self._data_set_details.number_of_examples += number_of_examples
            self._data_set_files.update_number_of_examples_in_file(
                examples_added=number_of_examples,
                file_index=file_index
            )

            for image_index in range(number_of_examples):
                image = distribution[file_index][image_index]
                total_progress += 1

                percent = int((total_progress + 1) / one_percent)

                self._data_set_creation_gui.update_image_ds_progress(
                    progress=percent
                )

                uint8_image2 = ImageReader.decode_image_for_tf_record(
                    path=image.path,

                    height=self._height,
                    width=self._width
                )
                uint8_image = uint8_image2.tostring()

                tf_example = to_tf_example.to_tf_example(
                    image_buffer=uint8_image,
                    label=int(image.identifier)
                )

                self.writer[file_index].write(tf_example.SerializeToString())

    def _write_cifar10_data_set(
            self,

            initial_data_set: InitialDataSet,
            train_ds):
        """
        - Writes the Cifar10 examples to TFRecord files.

        :param initial_data_set: InitialDataSet instance.
        :param train_ds:    - True if used to write the train data set.
                            - False if used to write the test data set.
        """

        if train_ds:
            examples = const.CIFAR10_EXAMPLES_NBR_TRAIN_DS
            read_op = Cifar10Reader.get_train_data_set_examples
        else:
            examples = const.CIFAR10_EXAMPLES_NBR_TEST_DS
            read_op = Cifar10Reader.get_test_data_set_examples

        progress_1_percent = examples / 100
        total_progress = 0

        split_length = int(examples / self._number_of_files)
        split_difference = examples % self._number_of_files

        examples_per_class = [0 for i in range(10)]

        with tf.Graph().as_default():
            labels, images = read_op()

            with tf.Session() as sess:
                coord = tf.train.Coordinator()
                threads = tf.train.start_queue_runners(sess=sess, coord=coord)

                for file_index in range(self._number_of_files):

                    number_of_example = split_length

                    if file_index < split_difference:
                        number_of_example += 1

                    self._data_set_details.number_of_examples = \
                        self._data_set_details.number_of_examples \
                        + number_of_example

                    self._data_set_files.update_number_of_examples_in_file(
                        examples_added=number_of_example,
                        file_index=file_index
                    )

                    for example_index in range(number_of_example):
                        total_progress += 1
                        self._data_set_creation_gui.update_cifar10_ds_progress(
                            progress=int(total_progress / progress_1_percent),
                            train_ds=train_ds
                        )

                        uint8_image = tf.cast(images, tf.uint8)
                        int32_label = tf.cast(labels, tf.int32)

                        label, uint8_image2 = sess.run([int32_label, uint8_image])

                        label = label[0]
                        examples_per_class[label] += 1

                        correlations = initial_data_set.class_correlation
                        label = correlations.get_new_correlation(
                            new_identifier=label
                        )

                        np_uint8_image = np.asarray(uint8_image2, np.uint8)
                        image = np_uint8_image.tostring()

                        tf_example = to_tf_example.to_tf_example(
                            image_buffer=image,
                            label=label
                        )

                        self.writer[file_index].write(tf_example.SerializeToString())

                    coord.request_stop()
                    coord.join(threads)

        for index in range(self._data_set_details.number_of_classes):
            self._data_set_details.classes.update_number_of_examples_for_class(
                examples_added=examples_per_class[index],
                identifier=index
            )

    def _write_data_set_files(self):
        """
        - Calls the method that will write the data set files.
        """

        for file_index in range(self._number_of_files):
            self.writer.append(
                tf.python_io.TFRecordWriter(
                    self._file_path[file_index]
                )
            )

        self._write_image_data_set()

        for initial_data_set in self._initial_data_sets.get_correlations():

            if initial_data_set.cifar10:
                if initial_data_set.cifar10_train_ds:
                    self._write_cifar10_data_set(
                        initial_data_set=initial_data_set,
                        train_ds=True
                    )

                if initial_data_set.cifar10_test_ds:
                    self._write_cifar10_data_set(
                        initial_data_set=initial_data_set,
                        train_ds=False
                    )

        for file_index in range(self._number_of_files):
            self.writer[file_index].close()

    #########################################################################
    # Auxiliary methods

    def _prepare_data_set_creation(self):
        """
        - Prepares the data set creation.
        """

        list_of_threads = []

        self._data_set_creation_gui.creation_preparations()

        for initial_data_set in self._initial_data_sets.get_correlations():

            if initial_data_set.images:
                image_data_set_preparations = ImageDataSetPreparations(
                    data_set_save_details=self._data_set_details,
                    initial_data_set_details=initial_data_set,

                    examples_list=self._examples_list
                )

                list_of_threads.append(image_data_set_preparations)

                image_data_set_preparations.start()

            elif initial_data_set.cifar10:
                cifar10_preparations = Cifar10DataSetPreparations(
                    progress_update_method=self._data_set_creation_gui.update_cifar10_download_progress,
                )

                list_of_threads.append(cifar10_preparations)

                cifar10_preparations.start()

            elif initial_data_set.imagenet:
                # TODO

                pass

        for thread in list_of_threads:
            thread.join()

    def _create_data_set(self):
        """
        - Calls the methods that will create the data set.
        """

        # TODO check validity.

        self._prepare_data_set_creation()

        if cifar10_download_failed:
            self._data_set_creation_gui.cifar10_download_failed_eh()
        else:
            self._write_data_set_files()
            self._write_main_data_set_file()

            self._data_set_creation_gui.creation_completed()

    #########################################################################
    # Public methods

    def create_data_set(self):
        """
        - Call this method to start the data set creation process, which
        will be executed on another thread.
        """

        CallMethodInNewThread.call_method(
            function_to_call=self._create_data_set,
        )

    #########################################################################
