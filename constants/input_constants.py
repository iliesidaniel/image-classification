import constants.global_constants as g_const


#############################################################################
#  Class identifiers input frame

CII_TITLE_FONT = g_const.SUBTITLE_FONT
CII_TITLE_TEXT = 'Class name <-> Identifier'
CII_TITLE_PADX = g_const.SUBTITLE_PADX
CII_TITLE_PADY = g_const.SUBTITLE_PADY

CII_FRAME_RELIEF = g_const.FRAME_RELIEF
CII_FRAME_PADX = g_const.FRAME_PADX
CII_FRAME_PADY = g_const.FRAME_PADY
CII_FRAME_BD = g_const.FRAME_BD

CII_WIDGETS_RELIEF = g_const.SUBFRAME_RELIEF
CII_WIDGETS_PADX = g_const.SUBFRAME_PADX
CII_WIDGETS_PADY = g_const.SUBFRAME_PADX
CII_WIDGETS_BD = g_const.SUBFRAME_BD

CII_ERROR_TITLE = 'Critical error!'
CII_ERROR_MSG = 'Sorry, something went wrong during class identifiers ' \
                'input.\n\n' \
                'The application is closing.'

#############################################################################
#  Class name input frame

CNI_FONT = g_const.GLOBAL_FONT_M

CNI_TITLE_FONT = g_const.SUBTITLE_FONT
CNI_TITLE_TEXT = 'Identifier <-> Class name'
CNI_TITLE_PADX = g_const.SUBTITLE_PADX
CNI_TITLE_PADY = g_const.SUBTITLE_PADY

CNI_FRAME_PADX = g_const.FRAME_PADX
CNI_FRAME_PADY = g_const.FRAME_PADY

CNI_MAIN_FRAME_PADX = 0
CNI_MAIN_FRAME_PADY = 0

CNI_WIDGETS_PADX = g_const.SUBFRAME_PADX
CNI_WIDGETS_PADY = g_const.SUBFRAME_PADY

CNI_BUTTONS_PADX = g_const.BUTTON_PADX
CNI_BUTTONS_PADY = g_const.BUTTON_PADY
CNI_BUTTON_BD = g_const.BUTTON_BD

CNI_ADD_BTN_TEXT = 'Add new class'
CNI_DELETE_BTN_TEXT = 'Delete the last class'

CNI_ALLOWED_CHARACTER = '[a-zA-Z0-9_-]'

#############################################################################
#  File name input frame

FNI_S_FONT = g_const.GLOBAL_FONT_S_ITALIC
FNI_L_FONT = g_const.GLOBAL_FONT_M

FNI_FRAME_PADX = g_const.FRAME_PADX
FNI_FRAME_PADY = g_const.FRAME_PADY

FNI_WIDGETS_PADX = g_const.SUBFRAME_PADX
FNI_WIDGETS_PADY = g_const.SUBFRAME_PADY

FNI_USER_INSTRUCTION = 'Name'
FNI_ALLOWED_CHARACTERS = '[a-zA-Z0-9_-]'

_FNI_ALLOWED_MSG_START = 'Allowed characters :  '
_FNI_ALLOWED_MSG_END = ''

FNI_ALLOWED_MSG = _FNI_ALLOWED_MSG_START \
                  + FNI_ALLOWED_CHARACTERS \
                  + _FNI_ALLOWED_MSG_END

#############################################################################
#  Initial data set picker frame

IDSP_FONT = g_const.GLOBAL_FONT_M

IDSP_FRAME_PADX = g_const.FRAME_PADX
IDSP_FRAME_PADY = g_const.FRAME_PADY

IDSP_WIDGETS_PADX = g_const.SUBFRAME_PADX
IDSP_WIDGETS_PADY = g_const.SUBFRAME_PADY

IDSP_QUESTION_TEXT = 'Select data set'

IDSP_NO_SELECTION_VAL = -1
IDSP_CIFAR10_VAL = 0
IDSP_IMAGENET_VAL = 1
IDSP_FROM_IMAGES_VAL = 2

IDSP_CIFAR10_BTN_TEXT = 'Cifar 10'
IDSP_IMAGENET_BTN_TEXT = 'ImageNet'
IDSP_FROM_IMAGES_BTN_TEXT = 'From images ...'

IDSP_INSTRUCTION_TEXT = 'Please select an initial data set.'

IDSP_CIFAR10_TRAIN_DS_TITLE = 'Train data set',
IDSP_CIFAR10_TRAIN_DS_MSG = "Do you want to use the training data set?"

IDSP_CIFAR10_TEST_DS_TITLE = 'Test data set',
IDSP_CIFAR10_TEST_DS_MSG = "Do you want to use the evaluation data set?"

IDSP_IMAGENET_TITLE = 'ImageNet',
IDSP_IMAGENET_MSG = "Sorry.\n\nFeature not implemented."

IDSP_FROM_IMAGES_INITIAL_DIR = '.'
IDSP_FROM_IMAGES_TITLE = 'Select data set directory',

IDSP_CIFAR10_IDENTIFIERS = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

#############################################################################
#  Initial data sets picker frame

IDSSP_FONT = g_const.GLOBAL_FONT_M

IDSSP_TITLE_FONT = g_const.SUBTITLE_FONT
IDSSP_TITLE_TEXT = 'Select initial data set(s)'
IDSSP_TITLE_PADX = g_const.SUBTITLE_PADX
IDSSP_TITLE_PADY = g_const.SUBTITLE_PADY

IDSSP_FRAME_PADX = g_const.FRAME_PADX
IDSSP_FRAME_PADY = g_const.FRAME_PADY

IDSSP_WIDGETS_PADX = g_const.SUBFRAME_PADX
IDSSP_WIDGETS_PADY = g_const.SUBFRAME_PADY

IDSSP_BUTTON_PADX = g_const.BUTTON_PADX
IDSSP_BUTTON_PADY = g_const.BUTTON_PADY
IDSSP_BUTTON_BD = g_const.BUTTON_BD

IDSSP_ADD_BTN_TEXT = 'Add new data set'
IDSSP_CB_INSTRUCTION_TEXT = 'Select the index of the data set you want to ' \
                            'delete.'
IDSSP_DELETE_BTN_TEXT = 'Delete'

#############################################################################
#  Number input frame and Number in range input frame

NINRI_FONT = g_const.GLOBAL_FONT_M

NINRI_FRAME_PADX = g_const.FRAME_PADX
NINRI_FRAME_PADY = g_const.FRAME_PADY

#############################################################################
#  String input frame

SI_FONT = g_const.GLOBAL_FONT_M

SI_FRAME_PADX = g_const.FRAME_PADX
SI_FRAME_PADY = g_const.FRAME_PADY

SI_ALLOWED_CHARACTERS = '[a-zA-Z0-9_-]'
SI_ALLOWED_CHARACTERS_SPACE = '[a-zA-Z0-9 _-]'

#############################################################################
#  Save details frame

SDI_TITLE_FONT = g_const.SUBTITLE_FONT
SDI_TITLE_TEXT = 'Save details'
SDI_TITLE_PADX = g_const.SUBTITLE_PADX
SDI_TITLE_PADY = g_const.SUBTITLE_PADY

SDI_WIDGETS_RELIEF = g_const.SUBFRAME_RELIEF
SDI_WIDGETS_PADX = g_const.SUBFRAME_PADX
SDI_WIDGETS_PADY = g_const.SUBFRAME_PADX
SDI_WIDGETS_BD = g_const.SUBFRAME_BD

SDI_FRAME_PADX = g_const.FRAME_PADX
SDI_FRAME_PADY = g_const.FRAME_PADY

SDI_BF_USER_INSTRUCTION = 'Directory path'
SDI_BF_NO_SELECTION = 'No save location selected'
SDI_BF_WINDOW_TITLE = 'Select save location'
SDI_BF_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY

SDI_FNI_DESCRIPTION_TEXT = 'Description'

#############################################################################
