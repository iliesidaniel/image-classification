import constants.global_constants as g_const


#############################################################################
#  Create data set window

CDSW_FONT = g_const.GLOBAL_FONT_M
CDSW_STATUS_BAR_FONT = g_const.GLOBAL_FONT_S_ITALIC

CDSW_TITLE = 'Create data set'

CDSW_WINDOW_PADX = 0
CDSW_WINDOW_PADY = 0

CDSW_FRAMES_PADX = 11
CDSW_FRAMES_PADY = 6

CDSW_CREATE_BUTTON_PADX = 11
CDSW_CREATE_BUTTON_PADY = 10

CDSW_ORIGINAL_IMAGES_VALUE = 1
CDSW_RANDOM_DISTORTIONS_VALUE = 2

CDSW_INIT_DATA_SET_QUESTION = 'Select the initial data set :'
CDSW_INIT_DATA_SET_ANSWER_1 = 'Cifar 10'
CDSW_INIT_DATA_SET_ANSWER_2 = 'Cifar 100'

CDSW_DATA_SET_USE_QUESTION = 'The data set will be used for :'
CDSW_DATA_SET_USE_ANSWER_1 = 'Training'
CDSW_DATA_SET_USE_ANSWER_2 = 'Evaluation'

CDSW_BF_USER_INSTRUCTION = 'Directory path'
CDSW_BF_NO_SELECTION = 'No save location selected'
CDSW_BF_WINDOW_TITLE = 'Select a directory'
CDSW_BF_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY

CDSW_IF_USER_INSTRUCTION = 'Data set name'
CDSW_IF_ALLOWED_CHARACTERS = '[a-zA-Z0-9_-]'
CDSW_IF_FILE_EXTENSION = '.train_sess/test_sess'

CDSW_CREATE_BUTTON_TEXT = 'Create data set'

CDSW_PB_NO_ACTION_FILL_PERCENT = 50
CDSW_PB_NO_ACTION_TEXT = "?? %   -   N / A"
CDSW_PB_EMPTY_COLOR = '#333333'
CDSW_PB_FILL_COLOR = '#4286f4'
CDSW_PB_TEXT_COLOR = '#e2e2e2'
CDSW_PB_HEIGHT = 45
CDSW_PB_WIDTH = 0

CDSW_STATUS_BORDER = 1
CDSW_INVALID_INPUT_STATUS = 'Please complete the creation form.'
CDSW_VALID_INPUT_STATUS = 'Thank you! Everything is set, you can now ' \
                          'create the data set by pressing the "' \
                          + CDSW_CREATE_BUTTON_TEXT + ' " button.'
CDSW_CREATING_DATA_SET_STATUS = 'Creating the new data set. Please wait.'

#############################################################################
# Cifar10 constants

CIFAR10_SAVE_LOCATION = '.cifar_10'
CIFAR10_ARCHIVE_FILE = 'cifar-10-binary.tar.gz'
CIFAR10_ARCHIVE_MD5SUM = 'c32a1d4ab5d03f1284b67883e8d87530'
CIFAR10_ARCHIVE_PATH = CIFAR10_SAVE_LOCATION \
                       + '/' \
                       + CIFAR10_ARCHIVE_FILE
CIFAR10_DOWNLOAD_LINK = 'http://www.cs.toronto.edu/~kriz/' \
                        + CIFAR10_ARCHIVE_FILE

CIFAR10_DIRECTORY_NAME = 'cifar-10-batches-bin'
CIFAR10_DIRECTORY_PATH = CIFAR10_SAVE_LOCATION \
                         + '/' \
                         + CIFAR10_DIRECTORY_NAME

# ~~~~~~~~~~~~~~~~~~~~~Cifar10 train data set files~~~~~~~~~~~~~~~~~~~~~~~~~~

CIFAR10_TRAIN_FILE_1_NAME = 'data_batch_1.bin'
CIFAR10_TRAIN_FILE_1_PATH = CIFAR10_DIRECTORY_PATH \
                            + '/' \
                            + CIFAR10_TRAIN_FILE_1_NAME
CIFAR10_TRAIN_FILE_1_SHA512 = '6e2dbbb2455496a15e0a1d621fd65e52d0b41ef4ec9' \
                              'f2edaf69f0dd31e9a5acbae64bb24b457e303e06609' \
                              '9f4d9c9bf7a22cc559c8a3379fcb5b3f0b18b68f16'

CIFAR10_TRAIN_FILE_2_NAME = 'data_batch_2.bin'
CIFAR10_TRAIN_FILE_2_PATH = CIFAR10_DIRECTORY_PATH \
                            + '/' \
                            + CIFAR10_TRAIN_FILE_2_NAME
CIFAR10_TRAIN_FILE_2_SHA512 = '41c360f984ebc8694699846d06a093e9e6d11d540eb' \
                              '275ea8875656b5119773388621aa313862ef35be028' \
                              '5f04828c0018bf7727eb1ca0a6275261d02003e7f1'

CIFAR10_TRAIN_FILE_3_NAME = 'data_batch_3.bin'
CIFAR10_TRAIN_FILE_3_PATH = CIFAR10_DIRECTORY_PATH \
                            + '/' \
                            + CIFAR10_TRAIN_FILE_3_NAME
CIFAR10_TRAIN_FILE_3_SHA512 = '8c1ecbfefe68df4af960ae77fbab8372928423cb9f2' \
                              'd724c3fbf4c07f35bfaff275c8587d35cb3c74a6993' \
                              '4fa99a294742a2d47b2eb183b6f4eba8c12b065977'

CIFAR10_TRAIN_FILE_4_NAME = 'data_batch_4.bin'
CIFAR10_TRAIN_FILE_4_PATH = CIFAR10_DIRECTORY_PATH \
                            + '/' \
                            + CIFAR10_TRAIN_FILE_4_NAME
CIFAR10_TRAIN_FILE_4_SHA512 = '49309a1d6ca0555a285e4ceb6796a12b8af42b33b12' \
                              'bfc85dae092d3be579d5161f9cae952ff6544bf9b58' \
                              'bc35294a5b16f757171df15f309b4df971bf2e10c6'

CIFAR10_TRAIN_FILE_5_NAME = 'data_batch_5.bin'
CIFAR10_TRAIN_FILE_5_PATH = CIFAR10_DIRECTORY_PATH \
                            + '/' \
                            + CIFAR10_TRAIN_FILE_5_NAME
CIFAR10_TRAIN_FILE_5_SHA512 = 'b62357317f3331182a598c298cd1c6773d33737e084' \
                              'ebc94052e9f6275a6cc72a0ed5114195b48b81f2b5d' \
                              'fc7e206782ea9f4e3bec452db88c5073a83c5df816'

CIFAR10_TRAIN_FILES_NAME = [
    CIFAR10_TRAIN_FILE_1_NAME,
    CIFAR10_TRAIN_FILE_2_NAME,
    CIFAR10_TRAIN_FILE_3_NAME,
    CIFAR10_TRAIN_FILE_4_NAME,
    CIFAR10_TRAIN_FILE_5_NAME
]

CIFAR10_TRAIN_FILES_PATH = [
    CIFAR10_TRAIN_FILE_1_PATH,
    CIFAR10_TRAIN_FILE_2_PATH,
    CIFAR10_TRAIN_FILE_3_PATH,
    CIFAR10_TRAIN_FILE_4_PATH,
    CIFAR10_TRAIN_FILE_5_PATH
]

CIFAR10_TRAIN_FILES_SHA512 = [
    CIFAR10_TRAIN_FILE_1_SHA512,
    CIFAR10_TRAIN_FILE_2_SHA512,
    CIFAR10_TRAIN_FILE_3_SHA512,
    CIFAR10_TRAIN_FILE_4_SHA512,
    CIFAR10_TRAIN_FILE_5_SHA512
]

# ~~~~~~~~~~~~~~~~~~~~~Cifar10 test data set file~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CIFAR10_TEST_FILE_NAME = 'test_batch.bin'
CIFAR10_TEST_FILE_PATH = CIFAR10_DIRECTORY_PATH \
                         + '/' \
                         + CIFAR10_TEST_FILE_NAME
CIFAR10_TEST_FILE_SHA512 = '74a9c00f7fe8357de708716d96417ee80c9edb1441ec31' \
                           '88acfc79bee907ebf7a1c08c59fdd8094fd944ae37b8d0' \
                           'e24b6319debef41901400b3a06f6a8442b81'

# ~~~~~~~~~~~~~~~~~~~~~All Cifar10 files~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CIFAR10_FILE_NAMES = CIFAR10_TRAIN_FILES_NAME
CIFAR10_FILE_NAMES.append(CIFAR10_TEST_FILE_NAME)

CIFAR10_FILE_PATHS = CIFAR10_TRAIN_FILES_PATH
CIFAR10_FILE_PATHS.append(CIFAR10_TEST_FILE_PATH)

CIFAR10_FILE_SHA512 = CIFAR10_TRAIN_FILES_SHA512
CIFAR10_FILE_SHA512.append(CIFAR10_TEST_FILE_SHA512)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CIFAR10_DOWNLOAD_NUMBER_OF_TRIES = 5

CIFAR10_EXAMPLES_NBR_TRAIN_DS = 50000
CIFAR10_EXAMPLES_NBR_TEST_DS = 10000

CIFAR10_IMAGE_HEIGHT = 32
CIFAR10_IMAGE_WIDTH = 32
CIFAR10_IMAGE_DEPTH = 3

CIFAR10_EXAMPLE_BYTES = 3073
CIFAR10_IMAGE_BYTES = 3072
CIFAR10_LABEL_BYTES = 1

CIFAR10_MIN_QUEUE_EXAMPLE_NBR_TRAIN = 8192
CIFAR10_MIN_QUEUE_EXAMPLE_NBR_TEST = 4096
CIFAR10_MIN_QUEUE_CAPACITY_TRAIN = 8832
CIFAR10_MIN_QUEUE_CAPACITY_TEST = 4736
CIFAR10_QUEUE_GENERATOR_THREADS = 8
CIFAR10_BATCH_SIZE = 100

#############################################################################
