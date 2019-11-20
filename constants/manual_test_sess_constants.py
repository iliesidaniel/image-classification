import constants.global_constants as g_const


#############################################################################
#  Interact window

IW_FONT = g_const.GLOBAL_FONT_M
IW_FONT_I = g_const.GLOBAL_FONT_M_ITALIC

IW_WINDOW_PADX = 11
IW_WINDOW_PADY = 11

IW_FRAMES_PADX = 11
IW_FRAMES_PADY = 11

#############################################################################
#  Browse CNN

BC_USER_INSTRUCTION = 'Select session :'
BC_NO_SELECTION_MESSAGE = 'No session selected!'
BC_BROWSE_WINDOW_TITLE = 'Select a session'
BC_INITIAL_DIRECTORY = g_const.DEFAULT_BROWSE_DIRECTORY

#############################################################################
#  Browse image frame

BI_USER_INSTRUCTION = 'Select an image :'
BI_NO_SELECTION_MESSAGE = 'No image selected!'
BI_BROWSE_WINDOW_TITLE = 'Select an image'
BI_SUPPORTED_FILES = [('Images', '*.jpeg *.jpg *.png')]
BI_INITIAL_DIRECTORY = './graphics/images/interact_images'

#############################################################################
# Image holder frame

IHF_INITIAL_IMAGE = './graphics/images/gui_images/_no_image_selected.png'

IHF_INITIAL_HEIGHT = 900
IHF_INITIAL_WIDTH = 0

IHF_IMAGE_BORDER_WIDTH = 0

#############################################################################
#  Progress bar

PB_FILL_COLORS = ['#4286f4', '#4275e3', '#4264d2', '#4253c1', '#4242b0']
PB_EMPTY_COLORS = ['#333', '#333', '#333', '#333', '#333']
PB_TEXT_COLORS = ['#e2e2e2', '#e2e2e2', '#e2e2e2', '#e2e2e2', '#e2e2e2']

#############################################################################
#  Guesses frame

GF_LABELS = [
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

GF_NO_INPUT_PB_TEXT = ['?? %   -   N / A', '?? %   -   N / A',
                       '?? %   -   N / A', '?? %   -   N / A',
                       '?? %   -   N / A']
GF_NO_INPUT_PERCENTS = [50, 50, 50, 50, 50]
GF_NUMBER_OF_GUESSES = 5
GF_INITIAL_WIDTH = 400
GF_PB_HEIGHT = 45

#############################################################################
# Run frame

RF_BUTTON_TEXT = 'Run'
RF_PADX = 0
RF_PADY = 50

#############################################################################
# Time frame

TF_FIXED_LABEL_TEXT = 'Time :'
TF_NO_INTERACTION_TIME = 'N / A'
TF_PADX = 0
TF_PADY = 10

#############################################################################
