import tensorflow as tf


#############################################################################

def to_tf_example(
        image_buffer,
        label):
    """
    -

    :param image_buffer: 
    :param label: 

    :return: 
    """

    image_feature = _bytes_feature(
        value=tf.compat.as_bytes(image_buffer)
    )

    label_feature = _int64_feature(
        value=label
    )

    feature = {
        'image': image_feature,
        'label': label_feature
    }

    features = tf.train.Features(
        feature=feature
    )

    example = tf.train.Example(
        features=features
    )

    return example


#############################################################################

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

#############################################################################
