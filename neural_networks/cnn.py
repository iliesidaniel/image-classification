from utils.train.session_details import SessionDetails


import constants.cnn_constants as const
import tensorflow as tf

import re


class CNN:

    def __init__(self,

                 session_details: SessionDetails,
                 interact=False):

        self._session_details = session_details
        self._interact = interact

    #########################################################################
    # Auxiliary methods

    @staticmethod
    def _activation_summary(x):

        tensor_name = re.sub(
            pattern="%s_[0-9]*/" % const.CNN_TOWER_NAME,
            string=x.op.name,
            repl=''
        )

        tf.summary.histogram(
            name=tensor_name + '/activations',
            values=x
        )

        tf.summary.scalar(
            name=tensor_name + '/sparsity',
            tensor=tf.nn.zero_fraction(x)
        )

    @staticmethod
    def _create_cpu_variable(
            name,
            shape,
            initializer):

        with tf.device('/cpu:0'):
            var = tf.get_variable(
                initializer=initializer,
                dtype=tf.float32,
                shape=shape,
                name=name
            )

        return var

    def _create_cpu_variable_with_weight_decay(
            self,
            name,
            shape,
            stddev,
            wd):

        var = self._create_cpu_variable(
            initializer=tf.truncated_normal_initializer(
                stddev=stddev,
                dtype=tf.float32
            ),
            shape=shape,
            name=name
        )

        if wd is not None:
            weight_decay = tf.multiply(
                name='weight_loss',
                x=tf.nn.l2_loss(var),
                y=wd
            )

            tf.add_to_collection(
                value=weight_decay,
                name='losses'
            )

        return var

    #########################################################################
    # Public methods

    def create_cnn_model(
            self,
            images):

        # conv1
        with tf.variable_scope('conv1') as scope:
            kernel = self._create_cpu_variable_with_weight_decay(
                name='weights',
                stddev=5e-2,
                shape=[
                    5, 5, 3, 64
                ],
                wd=0.0
            )

            conv = tf.nn.conv2d(
                input=images,
                filter=kernel,
                padding='SAME',
                strides=[
                    1, 1, 1, 1
                ]
            )

            biases = self._create_cpu_variable(
                initializer=tf.constant_initializer(0.0),
                name='biases',
                shape=[
                    64
                ]
            )

            pre_activation = tf.nn.bias_add(
                bias=biases,
                value=conv
            )

            conv1 = tf.nn.relu(
                features=pre_activation,
                name=scope.name
            )

            self._activation_summary(
                x=conv1
            )

        # pool1
        pool1 = tf.nn.max_pool(
            strides=[
                1, 2, 2, 1
            ],
            ksize=[
                1, 3, 3, 1
            ],
            padding='SAME',
            name='pool1',
            value=conv1
        )

        # norm1
        norm1 = tf.nn.lrn(
            alpha=0.001 / 9.0,
            depth_radius=4,
            name='norm1',
            input=pool1,
            beta=0.75,
            bias=1.0
        )

        # conv2
        with tf.variable_scope('conv2') as scope:
            kernel = self._create_cpu_variable_with_weight_decay(
                shape=[
                    5, 5, 64, 64
                ],
                name='weights',
                stddev=5e-2,
                wd=0.0
            )

            conv = tf.nn.conv2d(
                filter=kernel,
                padding='SAME',
                strides=[
                    1, 1, 1, 1
                ],
                input=norm1
            )

            biases = self._create_cpu_variable(
                initializer=tf.constant_initializer(0.1),
                name='biases',
                shape=[
                    64
                ]
            )

            pre_activation = tf.nn.bias_add(
                bias=biases,
                value=conv
            )

            conv2 = tf.nn.relu(
                features=pre_activation,
                name=scope.name
            )

            self._activation_summary(
                x=conv2
            )

        # norm2
        norm2 = tf.nn.lrn(
            alpha=0.001 / 9.0,
            depth_radius=4,
            name='norm2',
            input=conv2,
            beta=0.75,
            bias=1.0
        )

        # pool2
        pool2 = tf.nn.max_pool(
            strides=[
                1, 2, 2, 1
            ],
            ksize=[
                1, 3, 3, 1
            ],
            padding='SAME',
            name='pool2',
            value=norm2
        )

        # local3
        if self._interact:
            batch = 1
        else:
            batch = self._session_details.examples_per_batch

        with tf.variable_scope('local3') as scope:
            reshape = tf.reshape(
                shape=[
                    batch,
                    -1
                ],
                tensor=pool2
            )

            dim = reshape.get_shape()[1].value

            weights = self._create_cpu_variable_with_weight_decay(
                name='weights',
                stddev=0.04,
                wd=0.004,
                shape=[
                    dim,
                    384
                ]
            )

            biases = self._create_cpu_variable(
                initializer=tf.constant_initializer(0.1),
                name='biases',
                shape=[
                    384
                ]
            )

            local3 = tf.nn.relu(
                features=biases + tf.matmul(
                    a=reshape,
                    b=weights
                ),
                name=scope.name
            )

            self._activation_summary(
                x=local3
            )

        # local4
        with tf.variable_scope('local4') as scope:
            weights = self._create_cpu_variable_with_weight_decay(
                name='weights',
                stddev=0.04,
                wd=0.004,
                shape=[
                    384,
                    192
                ]
            )

            biases = self._create_cpu_variable(
                initializer=tf.constant_initializer(0.1),
                name='biases',
                shape=[
                    192
                ]
            )

            local4 = tf.nn.relu(
                features=biases + tf.matmul(
                    a=local3,
                    b=weights
                ),
                name=scope.name
            )

            self._activation_summary(
                x=local4
            )

        # linear layer(WX + b),
        with tf.variable_scope('softmax_linear') as scope:
            weights = self._create_cpu_variable_with_weight_decay(
                shape=[
                    192,
                    self._session_details.number_of_classes
                ],
                stddev=1 / 192.0,
                name='weights',
                wd=0.0
            )

            biases = self._create_cpu_variable(
                initializer=tf.constant_initializer(0.0),
                name='biases',
                shape=[
                    self._session_details.number_of_classes
                ]
            )

            softmax_linear = tf.add(
                name=scope.name,
                x=tf.matmul(
                    a=local4,
                    b=weights
                ),
                y=biases
            )

            self._activation_summary(
                x=softmax_linear
            )

        return softmax_linear

    #########################################################################
