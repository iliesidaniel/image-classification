#############################################################################
# Constants describing the training process.

CNN_MOVING_AVERAGE_DECAY = 0.9999
CNN_NUM_EPOCHS_PER_DECAY = 350.0
CNN_LEARNING_RATE_DECAY_FACTOR = 0.1
CNN_INITIAL_LEARNING_RATE = 0.1
CNN_TOWER_NAME = 'tower'

CNN_STATUS_UPDATE_INTERVAL = 10

CNN_SHUFFLE_BATCH_NUMBER_OF_THREADS = 8
CNN_SHUFFLE_BATCH_CAPACITY_COEFFICIENT = 5
CNN_SHUFFLE_BATCH_MIN_SIZE_COEFFICIENT = .5

CNN_CHECKPOINT_SAVE_INTERVAL = 60   # seconds

#############################################################################
