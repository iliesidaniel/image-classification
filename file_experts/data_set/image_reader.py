from PIL import Image

import tensorflow as tf
import numpy as np


class ImageReader:
    """
    - Use to read an image and prepare it to be used for:
        1. Creating a new data set : decode_image_for_tf_record;
        2. manual testing a network : decode_image_for_nn.
    """

    @staticmethod
    def _read_and_process_raw_image(
            path: str,
            width: int,
            height: int
    ):
        """
        - Reads the image at path.
        - If the image is PNG it makes sure it's no longer transparent.
        - The image is scaled to fit the available space.

        :param path: Image path.
        :param width: Available width.
        :param height: Available height.

        :return: Image as tensor (tf.float32).
        """

        # ~~~~~~~~ If *.png start ~~~~~~~~
        if path.endswith('png'):
            png_image = Image.open(path).convert("RGBA")
            tmp_image_path = '/tmp/tmp.jpg'
            png_width, pny_height = png_image.size

            non_transparent = Image.new(
                'RGBA',
                (png_width, pny_height),
                (255, 255, 255)
            )
            non_transparent.paste(
                png_image,
                (0, 0, png_width, pny_height),
                png_image
            )

            non_transparent.save(r'' + tmp_image_path)
            path = tmp_image_path
        # ~~~~~~~~ If *.png end ~~~~~~~~

        image = Image.open(path)
        img_width, img_height = image.size

        if img_height == height and img_width == width:
            # If the images has the same size as the max allowed dimensions.

            new_height = height
            new_width = width
        elif img_width >= img_height:
            # If the width of the image is greater or equal with the height.

            new_width = width
            new_height = int(img_height * width / img_width)
        else:
            # If the height of the image is greater than the width.

            new_height = height
            new_width = int(img_width * height / img_height)

        uint8_image = np.asarray(image, np.uint8)
        float32_image = tf.cast(uint8_image, tf.float32)

        resized_image = tf.image.resize_images(
            [float32_image],
            (
                new_height,
                new_width
            )
        )[0]

        resized_image = tf.image.resize_image_with_crop_or_pad(
            resized_image,
            height,
            width
        )

        resized_image.set_shape([height, width, 3])

        return resized_image

    #########################################################################
    # Public methods

    @staticmethod
    def decode_image_for_tf_record(
            path: str,
            width: int,
            height: int
    ):
        """
        - The image is scaled to fit the available space.

        :param path: Image path.
        :param width: Available width.
        :param height: Available height.

        :return: Image as numpy.array (numpy.uint8).
        """

        float32_image = ImageReader._read_and_process_raw_image(
            path=path,
            width=width,
            height=height
        )

        with tf.Session() as sess:
            uint8_image = tf.cast(float32_image, tf.uint8)
            uint8_image2 = sess.run([uint8_image])

            np_uint8_image = np.asarray(uint8_image2, np.uint8)

        # return np_uint8_image.tostring()
        return np_uint8_image

    @staticmethod
    def decode_image_for_nn(
            path: str,
            width: int,
            height: int
    ):
        """
        - The image is scaled to fit the available space.

        :param path: Image path.
        :param width: Available width.
        :param height: Available height.

        :return: Image as tensor (tf.float32).
        """

        return ImageReader._read_and_process_raw_image(
            path=path,
            width=width,
            height=height
        )

    #########################################################################
