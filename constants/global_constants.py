#############################################################################
#  Global constants -> Training and testing GUIs

GLOBAL_ALLOWED_FILE_NAME_CHARACTERS = '[a-zA-Z0-9_-]'

GLOBAL_DATA_SET_FILE_EXTENSION = '.dataset'
GLOBAL_DATA_SET_BROWSE_ENTRY = [
    (
        'Data set',
        '*' + GLOBAL_DATA_SET_FILE_EXTENSION
    )
]

GLOBAL_SESSION_FILE_EXTENSION = '.session'
GLOBAL_SESSION_BROWSE_ENTRY = [
    (
        'Session',
        '*' + GLOBAL_SESSION_FILE_EXTENSION
    )
]

GLOBAL_KF_CV_SESSION_FILE_EXTENSION = '.kfcvsession'
GLOBAL_KF_CV_SESSION_BROWSE_ENTRY = [
    (
        'K-fold cross-validation session',
        '*' + GLOBAL_KF_CV_SESSION_FILE_EXTENSION
    )
]

#############################################################################
#  Global constants -> Fonts

GLOBAL_FONT_S = ('Serif', 8)
GLOBAL_FONT_S_ITALIC = ('Serif', 8, 'italic')

GLOBAL_FONT_M = ('Serif', 10)
GLOBAL_FONT_M_ITALIC = ('Serif', 10, 'italic')

GLOBAL_FONT_L = ('Serif', 12)
GLOBAL_FONT_L_ITALIC = ('Serif', 12, 'italic')

TITLE_FONT = GLOBAL_FONT_L
SUBTITLE_FONT = GLOBAL_FONT_M_ITALIC
WIDGET_FONT = GLOBAL_FONT_M

#############################################################################
# Size

INPUT_WIDGET_LABEL_WIDTH = 31

#############################################################################
# Pad

FRAME_PADX = 24
FRAME_PADY = 12

SUBFRAME_PADX = 24
SUBFRAME_PADY = 12

BUTTON_PADX = 100
BUTTON_PADY = 12

TITLE_PADX = 300
TITLE_PADY = 40

SUBTITLE_PADX = 300
SUBTITLE_PADY = 12

#############################################################################
# Border

FRAME_BD = 5
SUBFRAME_BD = 3
BUTTON_BD = 3

#############################################################################
# Relief

FRAME_RELIEF = 'raised'
SUBFRAME_RELIEF = 'sunken'

#############################################################################
# Image size

IMAGE_SIZE_MIN = 24
IMAGE_SIZE_MAX = 256
IMAGE_SIZE_INCREASE_STEP = 4

#############################################################################
# Default values

DEFAULT_BROWSE_DIRECTORY = '/home/senna/bachelor-project-dev-files'

#############################################################################
