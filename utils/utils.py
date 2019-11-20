from PIL import Image, ImageTk

import re


#############################################################################

def load_and_resize_image(
        image_path_file_name: str,
        width: int,
        height: int):
    """ Loads the image specified by image_path_file_name, the image will be
    resized to the values specified by the parameters width and height.

    :param image_path_file_name: Path and file name of the image;
    :param width: Image width;
    :param height: Image height;

    :return: Resized image
    """

    image = Image.open(image_path_file_name)
    resized = image.resize((width, height))

    return ImageTk.PhotoImage(resized)


#############################################################################

def string_is_valid(
        string_to_check: str,
        allowed_characters: str):
    """
    - Checks if a string contains only characters that are present in
      allowed_characters.
    - Regex is used for the check.

    :param string_to_check: String that will be checked;
    :param allowed_characters: Regex expression that contains the allowed
                               characters;

    :return: - True if string_to_check has only allowed characters;
             - False otherwise.
    """

    not_allowed_characters = re.sub(allowed_characters, '', string_to_check)

    return not_allowed_characters == '' and string_to_check != ''


#############################################################################

def is_int(obj):
    """
    
    :param obj: 
    :return: 
    """
    # TODO

    if obj is not None:
        if string_is_valid(obj, '[0-9]'):
            try:
                int(obj)
                return True
            except ValueError:
                return False

    return False


def is_float(obj):
    """
    
    :param obj: 
    :return: 
    """
    # TODO

    if obj is not None:
        if string_is_valid(obj, '[0-9.]'):
            try:
                float(obj)
                return True
            except ValueError:
                return False

    return False

#############################################################################
