from utils.data_set.classes_correlation_between_data_sets import ClassesCorrelationBetweenDataSets
from utils.data_set.class_correlation_between_data_sets import ClassCorrelationBetweenDataSets
from utils.call_method_in_new_thread import CallMethodInNewThread
from utils.data_set.initial_data_sets import InitialDataSets
from utils.data_set.initial_data_set import InitialDataSet
from utils.data_set.data_set_classes import DataSetClasses
from utils.data_set.data_set_class import DataSetClass
from utils.new_file_details import NewFileDetails

from file_experts.data_set.data_set_reader import DataSetReader

from controllers.data_set_controller import DataSetController

from graphics.widgets.image_holder import ImageHolder

from datetime import datetime
from copy import deepcopy


import file_experts.file_expert as fe

import tensorflow as tf
import tkinter as tk


#############################################################################


def _create_image(
        image,
        image_name,
        sess):
    """
    :param image        : Image
    :param image_name   : Image name
    :param sess         : tf.Session
    """

    enc = tf.image.encode_jpeg(image)
    tf_img_name = tf.constant(image_name)
    img_write = tf.write_file(tf_img_name, enc)
    sess.run(img_write)


#############################################################################


def test_read_method(
        paths: [],

        data_set_image_size: int):
    """
    - Use this method to test read_tfrecords method and DataSetCreator,
    by checking the images and their names in TensorBoard.

    - Images are labeled as follows:
[image label in data set]_[the number of the file]_[image index in file].

    :param data_set_image_size: Image size in the data set.
    :param paths: List with the paths to the TFRecords files.
    """

    if __name__ == "__main__" and second_write:
        examples_to_read = _examples_to_read
    else:
        examples_to_read = 10

    number_of_files = len(paths)

    with tf.Graph().as_default():
        for file_index in range(number_of_files):
            labels, image = DataSetReader.read_tfrecords(
                data_set_image_size=data_set_image_size,
                paths=[paths[file_index]]
            )

            with tf.Session() as sess:
                coord = tf.train.Coordinator()
                threads = tf.train.start_queue_runners(
                    sess=sess,
                    coord=coord
                )

                summary_path = '/tmp/logs/file' + str(file_index)
                writer = tf.summary.FileWriter(summary_path)

                for example_index in range(examples_to_read):
                    label, img = sess.run([labels, image])

                    if __name__ == "__main__":
                        lbl.config(
                            text=label
                        )

                        image_name = '/home/senna/read/a/' \
                                     + str(label) + '_' \
                                     + str(file_index) + '_' \
                                     + str(example_index) + '.jpg'
                        _create_image(
                            image=img,
                            image_name=image_name,
                            sess=sess
                        )
                        image_holder1.update_image(
                            image_path_and_file_name=image_name
                        )

                    tf_var_img = tf.Variable(img, 'image_variable')
                    init_op = tf.global_variables_initializer()
                    sess.run(init_op)

                    image_name = 'image_' \
                                 + str(label) + '_' \
                                 + str(file_index) + '_' \
                                 + str(example_index)

                    print('Reading :  ' + image_name)

                    summary_op = tf.summary.image(
                        image_name,
                        [tf_var_img],
                        max_outputs=100
                    )

                    summary = sess.run(summary_op)
                    writer.add_summary(summary)

                    if __name__ == "__main__" and second_write:
                        image_name = '/home/senna/read/b/' \
                                     + str(label) + '_' \
                                     + str(file_index) + '_' \
                                     + str(example_index) + '.jpg'
                        _create_image(
                            image=img,
                            image_name=image_name,
                            sess=sess
                        )

                        image_holder2.update_image(
                            image_path_and_file_name=image_name
                        )

                writer.close()

                coord.request_stop()
                coord.join(threads)

            print(str(file_index) + ' was read.')

    print('Read & write finished.')


#############################################################################


def mock_data_set_creation(
        gui_instance,
        image_size):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~Data set details~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    creation_details = NewFileDetails()

    time_str = "{:%d_%b_%Y___%H_%M_%S}".format(datetime.now())

    creation_details._directory_path = '/home/senna/temp2537490563548906807645'
    creation_details._file_name = 'Try____' + time_str
    creation_details._file_name = 'first_data_set'
    creation_details._description = 'bkxXm8LPDi mLVkgzBZ6w myIN7Do4Tx ' \
                                    '5dBFHAwEYs jfT4gebti8 h2M5JgP9GH ' \
                                    'DPSwzaUhLe ONWkadKQNR C9mmfE9asU ' \
                                    'CMF3qN113H'

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~Data set classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    data_set_classes = DataSetClasses()

    classes = [
        'Airplane',
        'Automobile',
        'Bird',
        'Cat',
        'Deer',
        'Dog',
        'Frog',
        'Horse',
        'Ship',
        'Truck'
    ]

    for index in range(len(classes)):
        tmp = DataSetClass()

        tmp._class_name = classes[index]
        tmp._identifier = index
        tmp._number_of_examples = 0

        data_set_classes.add(tmp)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~Initial data sets~~~~~~~~~~~~~~~~~~~~~~~~~~~

    initial_data_sets = InitialDataSets()

    correlation_1 = ClassesCorrelationBetweenDataSets()
    correlation_2 = ClassesCorrelationBetweenDataSets()

    for index in range(len(classes)):
        tmp1 = ClassCorrelationBetweenDataSets()
        tmp2 = ClassCorrelationBetweenDataSets()

        tmp1.identifier_in_new_data_set = index
        tmp1.identifier_in_old_data_set = classes[index]

        tmp2.identifier_in_new_data_set = index
        tmp2.identifier_in_old_data_set = str(index)

        correlation_1.add(tmp1)
        correlation_2.add(tmp2)

    # ___________________________Initial data set____________________________

    initial_data_set_1 = InitialDataSet()
    initial_data_set_1._images = True
    initial_data_set_1._data_set_location = '/home/senna/qwert'
    initial_data_set_1.class_correlation = correlation_1

    # ___________________________Initial data set____________________________

    initial_data_set_2 = InitialDataSet()
    initial_data_set_2._cifar10 = True
    initial_data_set_2._cifar10_train_ds = False
    initial_data_set_2._cifar10_test_ds = True
    initial_data_set_2.class_correlation = correlation_2

    # _______________________________________________________________________

    initial_data_sets.add(initial_data_set_1)
    initial_data_sets.add(initial_data_set_2)

    for i in range(0):
        initial_data_sets.add(deepcopy(initial_data_set_1))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    DataSetController.create_new_data_set(
        initial_data_sets=initial_data_sets,
        creation_details=creation_details,
        data_set_classes=data_set_classes,
        data_set_creation_gui=gui_instance,
        image_size=image_size,
        number_of_files=10
    )


#############################################################################


if __name__ == "__main__":

    main_file = '/home/senna/temp2537490563548906807645/first_data_set.txt'

    _data_set_details = DataSetReader.read_main_data_set_file(
        path=main_file
    )

    sha_512 = fe.file_sha512(main_file)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n\n\nSHA = ' + sha_512 + '\n\n\n')
    print('**==**==**==**==**==**==**==****==**==**==**==**==**==**==**')
    print('**==**==**==**==**==**==**==****==**==**==**==**==**==**==**')
    print(str(_data_set_details))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    _examples_to_read = 10
    second_write = False
    file_path = []

    for _file_index in range(10):
        file_path.append(
            '/home/senna/temp2537490563548906807645/'
            + str(_file_index)
            + '.txt'
        )

    root = tk.Tk()

    frame = tk.Frame(
        root
    )

    image_holder1 = ImageHolder(
        image_path_and_file_name='/home/senna/img.jpg',
        parent=frame
    )
    image_holder2 = ImageHolder(
        image_path_and_file_name='/home/senna/img.jpg',
        parent=frame
    )

    lbl = tk.Label(
        root,
        text=''
    )

    image_holder1.pack(side='left',
                       fill='both',
                       expand=True)
    image_holder2.pack(side='right',
                       fill='both',
                       expand=True)

    frame.pack(side='top',
               fill='both',
               expand=True)

    lbl.pack(side='bottom',
             fill='both',
             expand=True)

    root.title('TFRecords test')

    CallMethodInNewThread.call_method(
        function_to_call=test_read_method,
        data_set_image_size=_data_set_details.image_size,
        paths=file_path
    )

    RWidth = root.winfo_screenwidth()
    RHeight = root.winfo_screenheight()
    root.geometry('%dx%d' % (RWidth, RHeight))

    root.update()

    root.minsize(1700, 900)

    root.mainloop()


#############################################################################
