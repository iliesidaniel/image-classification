import constants.create_data_set_constants as const
import tensorflow as tf


class Cifar10Reader:

    @staticmethod
    def _convert_from_binary(
            example_bytes):
        """
        - Casts the label to tf.int32.
        - Reshapes the image.

        :param example_bytes: Example in bytes from the Cifar10 data set file.

        :return:    - Label : tf.int32;
                    - Image : tf.uint8 [height, width, depth].
        """

        int32_label = tf.cast(
            x=tf.strided_slice(
                input_=example_bytes,
                begin=[0],
                end=[const.CIFAR10_LABEL_BYTES],
                strides=[1]
            ),
            dtype=tf.int32
        )

        int32_label.set_shape([1])

        binary_image = tf.reshape(
            tensor=tf.strided_slice(
                input_=example_bytes,
                begin=[const.CIFAR10_LABEL_BYTES],
                end=[const.CIFAR10_EXAMPLE_BYTES],
                strides=[1]
            ),
            shape=[
                const.CIFAR10_IMAGE_DEPTH,
                const.CIFAR10_IMAGE_HEIGHT,
                const.CIFAR10_IMAGE_WIDTH
            ]
        )

        uint8_image = tf.transpose(
            a=binary_image,
            perm=[
                1, 2, 0
            ]
        )

        return int32_label, uint8_image

    @staticmethod
    def _read_example_from_binary_file(
            filename_queue):
        """
        - Reads an example from filename_queue. 

        :param filename_queue: QueueRunner

        :return:    - Label : tf.int32;
                    - Image : tf.uint8 [height, width, depth].
        """

        reader = tf.FixedLengthRecordReader(
            record_bytes=const.CIFAR10_EXAMPLE_BYTES,
            header_bytes=0,
            footer_bytes=0
        )

        _, value = reader.read(
            queue=filename_queue
        )

        example_bytes = tf.decode_raw(
            bytes=value,
            out_type=tf.uint8
        )

        label, uint8_image = Cifar10Reader._convert_from_binary(
            example_bytes=example_bytes
        )

        return label, uint8_image

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Batch methods

    @staticmethod
    def _get_example(
            file_names: []):
        """
        - Reads examples from the file_names files.

        :param file_names: List with the path of the Cifar10 files.

        :return:    - Label : tf.int32;
                    - Image : tf.uint8 [height, width, depth].
        """

        filename_queue = tf.train.string_input_producer(
            string_tensor=file_names
        )

        label, image = Cifar10Reader._read_example_from_binary_file(
            filename_queue=filename_queue
        )

        # TODO Remove start
        reshaped_image = tf.cast(image, tf.float32)

        height = 24
        width = 24

        resized_image = tf.image.resize_image_with_crop_or_pad(
            reshaped_image,
            width,
            height
        )

        float_image = tf.image.per_image_standardization(resized_image)
        float_image.set_shape([height, width, 3])

        # return label, float_image
        # TODO Remove end

        return label, image

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Public methods

    @staticmethod
    def get_train_data_set_examples():
        """
        :return:    - Label : tf.int32;
                    - Image : tf.uint8 [height, width, depth].
        """

        labels, images = Cifar10Reader._get_example(
            file_names=const.CIFAR10_TRAIN_FILES_PATH
        )

        return labels, images

    @staticmethod
    def get_test_data_set_examples():
        """
        :return:    - Label : tf.int32;
                    - Image : tf.uint8 [height, width, depth].
        """

        labels, images = Cifar10Reader._get_example(
            file_names=[const.CIFAR10_TEST_FILE_PATH]
        )

        return labels, images

    #########################################################################
