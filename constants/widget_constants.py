import constants.global_constants as g_const


##########################################################################
#  Browse frame

BF_INSTRUCTION_FONT = g_const.GLOBAL_FONT_M
BF_BROWSE_BUTTON_FONT = BF_INSTRUCTION_FONT
BF_FILE_INFO_FONT = g_const.GLOBAL_FONT_S_ITALIC

BF_FRAME_PADX = 11
BF_FRAME_PADY = 6

BF_LABEL_FRAME_PADX = 11
BF_LABEL_FRAME_PADY = 6

BF_BUTTON_TEXT = 'Browse ...'

##########################################################################
#  Combobox input frame

CI_FONT = g_const.GLOBAL_FONT_M

CI_FRAME_PADX = 11
CI_FRAME_PADY = 6

##########################################################################
#  Checkbox item output frame

CIO_FONT = g_const.GLOBAL_FONT_M

CIO_FRAME_PADX = 11
CIO_FRAME_PADY = 6

##########################################################################
#  Guesses frame

GF_PB_HEIGHT = 45
GF_INITIAL_WIDTH = 400

GF_NUMBER_OF_GUESSES = 5

GF_NO_INPUT_PERCENTS = [50, 50, 50, 50, 50]
GF_NO_INPUT_PB_TEXT = ['?? %   -   N / A', '?? %   -   N / A',
                       '?? %   -   N / A', '?? %   -   N / A',
                       '?? %   -   N / A']

GF_FILL_COLORS = ['#4286f4', '#4275e3', '#4264d2', '#4253c1', '#4242b0']
GF_TEXT_COLORS = ['#e2e2e2', '#e2e2e2', '#e2e2e2', '#e2e2e2', '#e2e2e2']
GF_EMPTY_COLORS = ['#333333', '#333333', '#333333', '#333333', '#333333']

##########################################################################
# Image holder frame

IHF_INITIAL_IMAGE = './graphics/images/gui_images/_no_image_selected.png'

IHF_INITIAL_HEIGHT = 900
IHF_INITIAL_WIDTH = 0

IHF_IMAGE_BORDER_WIDTH = 0

##########################################################################
#  Multiline input frame

MI_FONT = g_const.GLOBAL_FONT_M

MI_FRAME_PADX = 22
MI_FRAME_PADY = 6

##########################################################################
#  Multiline output frame

MLO_FONT = g_const.GLOBAL_FONT_M

MLO_PADX = 11
MLO_PADY = 6

MLO_WIDGET_PADX = g_const.SUBFRAME_PADX
MLO_WIDGET_PADY = g_const.SUBFRAME_PADY

##########################################################################
#  Question with n possible Answers

QNA_FONT = g_const.GLOBAL_FONT_M

QNA_FRAME_PADX = 0
QNA_FRAME_PADY = 6

QNA_ANSWERS_FRAME_PADX = 11
QNA_ANSWERS_FRAME_PADY = 6

QNA_ANSWER_BUTTON_PADX = 11
QNA_ANSWER_BUTTON_PADY = 10

##########################################################################
#  Session buttons frame

SB_FONT = g_const.GLOBAL_FONT_M

SB_FRAME_PADX = 11
SB_FRAME_PADY = 6

SB_BTN_FRAME_PADX = 60
SB_BTN_FRAME_PADY = 11

SB_BUTTON_PADX = 11
SB_BUTTON_PADY = 8

SB_IMG_WIDTH = 64
SB_IMG_HEIGHT = 24

SB_START_BUTTON_TEXT = 'Start'
SB_PAUSE_BUTTON_TEXT = 'Pause'
SB_STOP_BUTTON_TEXT = 'Stop'
SB_CANCEL_BUTTON_TEXT = 'Cancel'

SB_BTN_START_IMG_PATH = './graphics/images/gui_images/_start.png'
SB_BTN_PAUSE_IMG_PATH = './graphics/images/gui_images/_pause.png'
SB_BTN_STOP_IMG_PATH = './graphics/images/gui_images/_stop.png'
SB_BTN_CANCEL_IMG_PATH = './graphics/images/gui_images/_cancel.png'

##########################################################################
#  Scrollable listbox frame

SL_FONT = g_const.GLOBAL_FONT_S

SL_PADX = 11
SL_PADY = 6

SL_OUTPUT_LISTBOX_HEIGHT = 25

##########################################################################
#  Single line output frame

SLO_FONT = g_const.GLOBAL_FONT_M

SLO_PADX = g_const.SUBFRAME_PADX / 2
SLO_PADY = g_const.SUBFRAME_PADY / 2

##########################################################################
# Verified input frame

VIF_FRAME_PADX = 11
VIF_FRAME_PADY = 6

VIF_FONT = g_const.GLOBAL_FONT_M

VIF_NBR_OF_INPUT_CHARS = 50

##########################################################################
# Validity indicator frame

VI_FONT = g_const.GLOBAL_FONT_S_ITALIC

VI_VALID_TEXT = 'Valid'
VI_INVALID_TEXT = 'Invalid'

VI_IMG_SIZE = 30

VI_SCROLL_REGION_HEIGHT = 320

VI_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
VI_SUBFRAME_PADX = 0
VI_SUBFRAME_PADY = 0
VI_SUBFRAME_BD = g_const.SUBFRAME_BD

VI_VALID_IMG_PATH = './graphics/images/gui_images/_good.png'
VI_INVALID_IMG_PATH = './graphics/images/gui_images/_bad.png'

##########################################################################
