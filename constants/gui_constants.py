import constants.train_sess_constants as tr_const
import constants.global_constants as g_const


#############################################################################
# Training session GUI

#############################################################################
# Manual test session GUI

#############################################################################
# Automated test session GUI

ATS_FONT = g_const.GLOBAL_FONT_M

ATS_SUBFRAME_PADX = g_const.SUBFRAME_PADX
ATS_SUBFRAME_PADY = 60

ATS_TSB_NO_SELECTION = 'No training session selected'
ATS_TSB_USER_INSTRUCTION = 'Select a training session'
ATS_TSB_WINDOW_TITLE = 'Select a training session'
ATS_TSB_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY
ATS_TSB_SUPPORTED_FILES = g_const.GLOBAL_SESSION_BROWSE_ENTRY

ATS_EPOCHS_NBR_TEXT = tr_const.TSDI_EPOCHS_NBR_INSTRUCTION
ATS_EPOCHS_NBR_OPTIONS = tr_const.TSDI_EPOCHS_NBR_OPTIONS

ATS_DSB_NO_SELECTION = 'No data set selected.'
ATS_DSB_USER_INSTRUCTION = 'Select a data set'
ATS_DSB_INVALID_MESSAGE = 'The data set selected can not be used by this' \
                          ' session.'
ATS_DSB_WINDOW_TITLE = 'Select a data set'
ATS_DSB_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY
ATS_DSB_SUPPORTED_FILES = g_const.GLOBAL_DATA_SET_BROWSE_ENTRY

ATS_START_BTN_PADX = g_const.BUTTON_PADX
ATS_START_BTN_PADY = g_const.BUTTON_PADY
ATS_START_BTN_BD = g_const.BUTTON_BD
ATS_BTN_TEXT = 'Start test session'

#############################################################################
# K-fold cross validation session GUI

#############################################################################
# K-fold cross validation existent session GUI

KFCVESG_K_TEXT = 'Select the train-test session you want to see'

#############################################################################
# K-fold cross validation new session GUI

#############################################################################
# K-fold cross validation session GUI buttons frame

KFCVGB_FONT = g_const.GLOBAL_FONT_M

KFCVGB_PADX = 11
KFCVGB_PADY = 6

KFCVGB_BTN_FRAME_PADX = 0
KFCVGB_BTN_FRAME_PADY = 0

KFCVGB_BTN_PADX = 0
KFCVGB_BTN_PADY = 12

KFCVGB_NEW_SESS_BTN = "New K-fold cross-validation session"
KFCVGB_EXISTENT_SESS_BTN = 'Existent K-fold cross-validation session'

KFCVGB_IMG_WIDTH = 100
KFCVGB_IMG_HEIGHT = 32

KFCVGB_NEW_SESS_IMG_PATH = \
    './graphics/images/gui_images/_new_train_sess.png'
KFCVGB_EXISTENT_SESS_IMG_PATH = \
    './graphics/images/gui_images/_existent_train_sess.png'

#############################################################################
#  Create data set GUI

CDSG_TITLE_FONT = g_const.TITLE_FONT
CDSG_TITLE_TEXT = 'Create a new data set'
CDSG_TITLE_RELIEF = g_const.FRAME_RELIEF
CDSG_TITLE_PADX = g_const.TITLE_PADX
CDSG_TITLE_PADY = g_const.TITLE_PADY
CDSG_TITLE_BD = g_const.SUBFRAME_BD

CDSG_FRAME_RELIEF = g_const.FRAME_RELIEF
CDSG_FRAME_PADX = g_const.FRAME_PADX
CDSG_FRAME_PADY = g_const.FRAME_PADY
CDSG_FRAME_BD = g_const.FRAME_BD

CDSG_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
CDSG_SUBFRAME_PADX = g_const.SUBFRAME_PADX
CDSG_SUBFRAME_PADY = g_const.SUBFRAME_PADY
CDSG_SUBFRAME_BD = g_const.SUBFRAME_BD

CDSG_CREATE_BTN_TEXT = 'Create data set'
CDSG_CREATE_BTN_PADX = g_const.BUTTON_PADX
CDSG_CREATE_BTN_PADY = g_const.BUTTON_PADY
CDSG_CREATE_BTN_BD = g_const.BUTTON_BD

CDSG_FILE_EXTENSION = g_const.GLOBAL_DATA_SET_FILE_EXTENSION

CDSG_PB_WIDTH = 100
CDSG_PB_HEIGHT = 45

CDSG_PB_FILL_COLORS = '#4286f4'
CDSG_PB_TEXT_COLORS = '#e2e2e2'
CDSG_PB_EMPTY_COLORS = '#333333'

CDSG_PB_NO_INPUT_PERCENT = 50
CDSG_PB_NO_INPUT_TEXT = 'Please complete the form'

#############################################################################
# Train GUI buttons frame

TGB_FONT = g_const.GLOBAL_FONT_M

TGB_PADX = 11
TGB_PADY = 6

TGB_BTN_FRAME_PADX = 0
TGB_BTN_FRAME_PADY = 0

TGB_BTN_PADX = 0
TGB_BTN_PADY = 12

TGB_NEW_SESS_BTN = "New training session"
TGB_EXISTENT_SESS_BTN = 'Existent training session'

TGB_IMG_WIDTH = 100
TGB_IMG_HEIGHT = 32

TGB_NEW_SESS_IMG_PATH = \
    './graphics/images/gui_images/_new_train_sess.png'
TGB_EXISTENT_SESS_IMG_PATH = \
    './graphics/images/gui_images/_existent_train_sess.png'

#############################################################################
# Training session GUI

#############################################################################
# New training session GUI

NTSG_EXTENSION = g_const.GLOBAL_SESSION_FILE_EXTENSION

#############################################################################
# Existent training session GUI

ETS_FRAME_PADX = g_const.FRAME_PADX
ETS_FRAME_PADY = g_const.FRAME_PADY

ETS_TSB_NO_SELECTION = 'No training session selected'
ETS_TSB_USER_INSTRUCTION = 'Select a training session'
ETS_TSB_WINDOW_TITLE = 'Select a training session'
ETS_TSB_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY
ETS_TSB_SUPPORTED_FILES = g_const.GLOBAL_SESSION_BROWSE_ENTRY

ETS_EPOCHS_NBR_TEXT = tr_const.TSDI_EPOCHS_NBR_INSTRUCTION
ETS_EPOCHS_NBR_OPTIONS = tr_const.TSDI_EPOCHS_NBR_OPTIONS

ETS_DSB_NO_SELECTION = 'No data set selected.'
ETS_DSB_USER_INSTRUCTION = 'Select a data set'
ETS_DSB_INVALID_MESSAGE = 'The data set selected can not be used by this' \
                          ' session.'
ETS_DSB_WINDOW_TITLE = 'Select a data set'
ETS_DSB_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY
ETS_DSB_SUPPORTED_FILES = g_const.GLOBAL_DATA_SET_BROWSE_ENTRY

#############################################################################
