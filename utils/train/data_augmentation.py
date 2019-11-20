import constants.train_sess_constants as const


class DataAugmentation:

    def __init__(self):

        self._crop = False
        self._flip_left_right = False
        self._brightness = False
        self._contrast = False

    def __str__(self):
        rez = '\n++++ Data augmentation ++++\n'
        rez += '\nCrop            :    ' + str(self.crop)
        rez += '\nFlip left-right :    ' + str(self.flip_left_right)
        rez += '\nBrightness      :    ' + str(self.brightness)
        rez += '\nContrast        :    ' + str(self.contrast)

        return rez

    ##########################################################################
    # crop

    @property
    def crop(self):
        return self._crop

    @crop.setter
    def crop(self,
             value: bool):
        if not isinstance(value, bool):
            raise ValueError('Crop must be bool.')

        self._crop = value

    ##########################################################################
    # flip_left_right

    @property
    def flip_left_right(self):
        return self._flip_left_right

    @flip_left_right.setter
    def flip_left_right(self,
                        value: bool):
        if not isinstance(value, bool):
            raise ValueError('Flip left-right must be bool.')

        self._flip_left_right = value

    ##########################################################################
    # brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self,
                   value: bool):
        if not isinstance(value, bool):
            raise ValueError('Brightness must be bool.')

        self._brightness = value

    ##########################################################################
    # contrast

    @property
    def contrast(self):
        return self._contrast

    @contrast.setter
    def contrast(self,
                 value: bool):
        if not isinstance(value, bool):
            raise ValueError('Contrast must be bool.')

        self._contrast = value

    ##########################################################################
    # to list

    def get_options_list(self):

        options_list = [
            (
                const.DA_CROP_TEXT,
                self._crop
            ),
            (
                const.DA_FLIP_LR_TEXT,
                self._flip_left_right
            ),
            (
                const.DA_BRIGHTNESS_TEXT,
                self._brightness
            ),
            (
                const.DA_CONTRAST_TEXT,
                self._contrast
            )
        ]

        return options_list

    ##########################################################################

    def to_json(self):

        js = {
            'Crop'            : self.crop,
            'Contrast'        : self.contrast,
            'Brightness'      : self.brightness,
            'Flip left-right' : self.flip_left_right,
        }

        return js

    ##########################################################################

    def from_json(
            self,

            js: {}):

        self.flip_left_right = js['Flip left-right']
        self.brightness = js['Brightness']
        self.contrast = js['Contrast']
        self.crop = js['Crop']

    ##########################################################################
