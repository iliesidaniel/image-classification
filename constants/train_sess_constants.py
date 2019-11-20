import constants.global_constants as g_const


#############################################################################
#  Save details frame

TSDI_FONT = g_const.GLOBAL_FONT_M

TSDI_FRAME_PADX = 11
TSDI_FRAME_PADY = 11

TSDI_INSTRUCTION = 'Session details'

TSDI_FILE_EXTENSION = g_const.GLOBAL_DATA_SET_BROWSE_ENTRY
TSDI_BF_NO_SELECTION = 'No save data set selected'
TSDI_BF_USER_INSTRUCTION = 'Select the data set'
TSDI_BF_WINDOW_TITLE = 'Select a data set'
TSDI_BF_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY

TSDI_NN_MODEL_INSTRUCTION = 'Neural network'
TSDI_NN_MODEL_OPTIONS = ['TensorFlow example']

TSDI_BATCH_SIZE_INSTRUCTION = 'Examples per batch'
TSDI_BATCH_SIZE_OPTIONS = [32, 64, 128, 256]

TSDI_EPOCHS_NBR_INSTRUCTION = 'Number of epochs'
TSDI_EPOCHS_NBR_OPTIONS = [32, 64, 128, 256, 512, 1024]

TSDI_IMAGE_SIZE_INSTRUCTION = 'Image size'
TSDI_IMAGE_SIZE_OPTIONS = [
    x for x in range(
        g_const.IMAGE_SIZE_MIN,
        g_const.IMAGE_SIZE_MAX + 1,
        g_const.IMAGE_SIZE_INCREASE_STEP
    )
]

TSDI_K_FOLD_CV_INSTRUCTION = 'Number of folds'
TSDI_K_FOLD_CV_OPTIONS = [2, 3, 4, 5, 6, 7, 8, 9, 10]

#############################################################################
#  Data augmentation

DA_FONT = g_const.GLOBAL_FONT_M

DA_FRAME_PADX = 0
DA_FRAME_PADY = 6

DA_MODIFIERS_PADX = 11
DA_MODIFIERS_PADY = 6

DA_RAND_DISTORTIONS_PADX = 11
DA_RAND_DISTORTIONS_PADY = 6

DA_USER_INFO = 'Data augmentation'

DA_CROP_TEXT = 'Crop'
DA_FLIP_LR_TEXT = 'Flip left-right'
DA_BRIGHTNESS_TEXT = 'Brightness'
DA_CONTRAST_TEXT = 'Contrast'

#############################################################################
