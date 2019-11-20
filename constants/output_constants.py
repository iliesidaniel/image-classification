import constants.train_sess_constants as tr_const
import constants.test_sess_constants as te_const
import constants.global_constants as g_const


#############################################################################
#  Classes output frame

CMO_HEADING_FONT = g_const.GLOBAL_FONT_M
CMO_TABLE_FONT = g_const.GLOBAL_FONT_S
CMO_TABLE_HEIGHT = 10

CMO_TITLE_FONT = g_const.SUBTITLE_FONT
CMO_TITLE_TEXT = 'Confusion matrix'
CMO_TITLE_PADX = g_const.SUBTITLE_PADX
CMO_TITLE_PADY = g_const.SUBTITLE_PADY

CMO_FRAME_RELIEF = g_const.FRAME_RELIEF
CMO_FRAME_PADX = g_const.FRAME_PADX
CMO_FRAME_PADY = g_const.FRAME_PADY
CMO_FRAME_BD = g_const.FRAME_BD

CMO_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
CMO_SUBFRAME_BD = g_const.SUBFRAME_BD

#############################################################################
#  Classes output frame

CO_HEADING_FONT = g_const.GLOBAL_FONT_M
CO_TABLE_FONT = g_const.GLOBAL_FONT_S

CO_TITLE_FONT = g_const.SUBTITLE_FONT
CO_TITLE_TEXT = 'Classes'
CO_TITLE_PADX = g_const.SUBTITLE_PADX
CO_TITLE_PADY = g_const.SUBTITLE_PADY

CO_SUBTITLE_IDENTIFIER_TEXT = 'Identifier'
CO_SUBTITLE_CLASS_TEXT = 'Class name'
CO_SUBTITLE_FONT = g_const.SUBTITLE_FONT

CO_FRAME_RELIEF = g_const.FRAME_RELIEF
CO_FRAME_PADX = g_const.FRAME_PADX
CO_FRAME_PADY = g_const.FRAME_PADY
CO_FRAME_BD = g_const.FRAME_BD

CO_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
CO_SUBFRAME_PADX = g_const.SUBFRAME_PADX
CO_SUBFRAME_PADY = g_const.SUBFRAME_PADY
CO_SUBFRAME_BD = g_const.SUBFRAME_BD

CO_TABLE_HEIGHT = CMO_TABLE_HEIGHT
CO_TABLE_COLUMNS = [
    'Identifier',
    'Class name',
    'Number of examples'
]

#############################################################################
#  Data augmentation output frame

DAO_TITLE_FONT = g_const.SUBTITLE_FONT
DAO_TITLE_TEXT = 'Data augmentation'
DAO_TITLE_PADX = g_const.SUBTITLE_PADX
DAO_TITLE_PADY = g_const.SUBTITLE_PADY

DAO_FRAME_RELIEF = g_const.FRAME_RELIEF
DAO_FRAME_PADX = g_const.FRAME_PADX
DAO_FRAME_PADY = g_const.FRAME_PADY
DAO_FRAME_BD = g_const.FRAME_BD

DAO_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
DAO_SUBFRAME_PADX = g_const.SUBFRAME_PADX
DAO_SUBFRAME_PADY = g_const.SUBFRAME_PADY
DAO_SUBFRAME_BD = g_const.SUBFRAME_BD

#############################################################################
#  Data set details output frame

DSDO_TITLE_TEXT = 'Data set save details'

DSDO_EXAMPLES_NBR_TEXT = 'Number of examples'
DSDO_EXAMPLES_NBR_INITIAL_TEXT = ''

DSDO_CLASSES_NBR_TEXT = 'Number of classes'
DSDO_CLASSES_NBR_INITIAL_TEXT = ''

DSDO_IMAGE_SIZE_TEXT = 'Image size'
DSDO_IMAGE_SIZE_INITIAL_TEXT = ''

DSDO_ERROR_TITLE = 'Fatal error!'
DSDO_ERROR_MSG = 'Sorry.\n\nSomething went wrong while showing the data' \
                 ' set\'s save details.\n\nThe application is closing.'

#############################################################################
#  Save details output frame

SD_FONT = g_const.WIDGET_FONT

SD_TITLE_FONT = g_const.SUBTITLE_FONT
SD_TITLE_TEXT = 'Save details'
SD_TITLE_PADX = g_const.SUBTITLE_PADX
SD_TITLE_PADY = g_const.SUBTITLE_PADY

SD_FRAME_RELIEF = g_const.FRAME_RELIEF
SD_FRAME_PADX = g_const.FRAME_PADX
SD_FRAME_PADY = g_const.FRAME_PADY
SD_FRAME_BD = g_const.FRAME_BD

SD_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
SD_SUBFRAME_PADX = g_const.SUBFRAME_PADX
SD_SUBFRAME_PADY = g_const.SUBFRAME_PADY
SD_SUBFRAME_BD = g_const.SUBFRAME_BD

SD_NAME_TEXT = 'Name'
SD_INITIAL_NAME_TEXT = ''
SD_DESCRIPTION_WIDTH = 28
SD_DESCRIPTION_TEXT = 'Description'

#############################################################################
# Test session charts frame

TESC_TITLE_FONT = g_const.SUBTITLE_FONT
TESC_TITLE_TEXT = 'Charts'
TESC_TITLE_PADX = g_const.SUBTITLE_PADX
TESC_TITLE_PADY = g_const.SUBTITLE_PADY

TESC_FRAME_RELIEF = g_const.FRAME_RELIEF
TESC_FRAME_PADX = g_const.FRAME_PADX
TESC_FRAME_PADY = g_const.FRAME_PADY
TESC_FRAME_BD = g_const.FRAME_BD

TESC_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
TESC_SUBFRAME_PADX = g_const.SUBFRAME_PADX
TESC_SUBFRAME_PADY = g_const.SUBFRAME_PADY
TESC_SUBFRAME_BD = g_const.SUBFRAME_BD

TESC_CHARTS_TEXT = 'Select the chart you want to see'
TESC_CHARTS_OPTIONS = te_const.TER_METHODS_LIST

#############################################################################
# Test sess output frame

TESO_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
TESO_SUBFRAME_PADX = g_const.SUBFRAME_PADX
TESO_SUBFRAME_PADY = g_const.SUBFRAME_PADY
TESO_SUBFRAME_BD = g_const.SUBFRAME_BD

TESO_PB_WIDTH = 100
TESO_PB_HEIGHT = 45

TESO_PB_FILL_COLORS = '#4286f4'
TESO_PB_TEXT_COLORS = '#e2e2e2'
TESO_PB_EMPTY_COLORS = '#333333'

TESO_PB_NO_INPUT_PERCENT = 50
TESO_PB_NO_INPUT_TEXT = '?? %   -   N / A'

#############################################################################
# Train sess output frame

TRSO_HEADING_FONT = g_const.GLOBAL_FONT_M
TRSO_TABLE_FONT = g_const.GLOBAL_FONT_S

TRSO_TABLE_HEIGHT = 30

TRSO_TABLE_COLUMNS = [
    'Step',
    'Loss',
    'Examples / second',
    'Seconds / batch',
]

#############################################################################
# Test session overall results output frame

TSOR_FONT = g_const.WIDGET_FONT

TSOR_TITLE_FONT = g_const.SUBTITLE_FONT
TSOR_TITLE_TEXT = 'Test session overall results'
TSOR_TITLE_PADX = g_const.SUBTITLE_PADX
TSOR_TITLE_PADY = g_const.SUBTITLE_PADY

TSOR_SUBTITLE_EVAL_METHOD_TEXT = 'Measure methods'
TSOR_SUBTITLE_RESULT_TEXT = 'Results'
TSOR_SUBTITLE_FONT = g_const.SUBTITLE_FONT

TSOR_FRAME_RELIEF = g_const.FRAME_RELIEF
TSOR_FRAME_PADX = g_const.FRAME_PADX
TSOR_FRAME_PADY = g_const.FRAME_PADY
TSOR_FRAME_BD = g_const.FRAME_BD

TSOR_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
TSOR_SUBFRAME_PADX = g_const.SUBFRAME_PADX
TSOR_SUBFRAME_PADY = g_const.SUBFRAME_PADY
TSOR_SUBFRAME_BD = g_const.SUBFRAME_BD

TSOR_PRECISION_TEXT = te_const.TER_PRECISION_TEXT
TSOR_PRECISION_INITIAL_TEXT = ''

TSOR_RECALL_TEXT = te_const.TER_RECALL_TEXT
TSOR_RECALL_INITIAL_TEXT = ''

TSOR_F_MEASURE_TEXT = te_const.TER_F_MEASURE_TEXT
TSOR_F_MEASURE_INITIAL_TEXT = ''

#############################################################################
# Train sess save details output frame

TSSD_TITLE_TEXT = 'Train session save details'

TSSD_NN_MODEL_TEXT = tr_const.TSDI_NN_MODEL_INSTRUCTION
TSSD_NN_MODEL_INITIAL_TEXT = ''
TSSD_BATCH_SIZE_TEXT = tr_const.TSDI_BATCH_SIZE_INSTRUCTION
TSSD_BATCH_SIZE_INITIAL_TEXT = ''
TSSD_EPOCHS_NBR_TEXT = tr_const.TSDI_EPOCHS_NBR_INSTRUCTION
TSSD_EPOCHS_NBR_INITIAL_TEXT = ''
TSSD_IMAGE_SIZE_TEXT = tr_const.TSDI_IMAGE_SIZE_INSTRUCTION
TSSD_IMAGE_SIZE_INITIAL_TEXT = ''

TSSD_ERROR_TITLE = 'Fatal error!'
TSSD_ERROR_MSG = 'Sorry.\n\nSomething went wrong while showing the train' \
                 ' session\'s save details.\n\nThe application is closing.'

#############################################################################
#  Used data set output frame

USDO_TITLE_TEXT = 'Data set #'

USDO_IMAGE_SIZE_TEXT = 'Image size'
USDO_IMAGE_SIZE_INITIAL_TEXT = ''

USDO_NUMBER_OF_FILES_TEXT = 'Number of files'
USDO_NUMBER_OF_FILES_INITIAL_TEXT = ''

USDO_NUMBER_OF_EXAMPLES_TEXT = 'Number of examples'
USDO_NUMBER_OF_EXAMPLES_INITIAL_TEXT = ''

USDO_ERROR_TITLE = 'Fatal error!'
USDO_ERROR_MSG = 'Sorry.\n\nSomething went wrong while showing the used' \
                 ' data set details.\n\nThe application is closing.'

#############################################################################
#  Used data sets output frame

UDSSO_FONT = g_const.WIDGET_FONT

UDSSO_TITLE_FONT = g_const.SUBTITLE_FONT
UDSSO_TITLE_TEXT = 'Data sets used'
UDSSO_TITLE_PADX = g_const.SUBTITLE_PADX
UDSSO_TITLE_PADY = g_const.SUBTITLE_PADY

UDSSO_FRAME_RELIEF = g_const.FRAME_RELIEF
UDSSO_FRAME_PADX = g_const.FRAME_PADX
UDSSO_FRAME_PADY = g_const.FRAME_PADY
UDSSO_FRAME_BD = g_const.FRAME_BD

UDSSO_SUBFRAME_RELIEF = g_const.SUBFRAME_RELIEF
UDSSO_SUBFRAME_PADX = g_const.SUBFRAME_PADX
UDSSO_SUBFRAME_PADY = g_const.SUBFRAME_PADY
UDSSO_SUBFRAME_BD = g_const.SUBFRAME_BD

#############################################################################
