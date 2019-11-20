from pathlib import Path

import utils.utils as utils
import hashlib
import shutil
import os


def _is_file_name_available(
        path: str,
        file_name: str,
        file_extension: str):
    """ 
    - Returns True if there is no file with the specified details, False 
    otherwise.
    """

    path_str = path + '/' + file_name + file_extension
    my_file = Path(path_str)

    return not my_file.is_file()


def is_file_name_valid(
        allowed_characters: str,
        directory_path: str,
        file_name: str,
        file_extension: str):
    """ 
    - Checks if the file name is valid.
    - A file name is valid if it contains only the allowed characters, the 
    save location exists and does not contain a file with the same name and
    extension.

    :return:    - True if the file name is valid;
                - False otherwise.
    """

    if isinstance(file_name, str) and isinstance(directory_path, str) \
            and directory_path != '' and directory_path is not None \
            and file_name != '' and file_name is not None:

        name_available = _is_file_name_available(
            path=directory_path,
            file_name=file_name,
            file_extension=file_extension
        )

        str_is_valid = utils.string_is_valid(
            file_name,
            allowed_characters
        )

        return str_is_valid and name_available

    return False


def _is_directory_name_available(
        path: str,
        directory_name: str):
    """
    - Returns True if there is no directory with the specified details, False
    otherwise.
    """

    path_str = path + '/' + directory_name
    my_file = Path(path_str)

    return not my_file.is_dir()


def is_directory_name_valid(
        allowed_characters: str,
        directory_path: str,
        directory_name: str):
    """
    - Checks if the directory name is valid.
    - A directory name is valid if it contains only the allowed characters,
    the save location exists and does not contain a directory with the same
    name and extension.

    :return:    - True if the directory name is valid;
                - False otherwise.
    """

    if isinstance(directory_name, str) and isinstance(directory_path, str) \
            and directory_path != '' and directory_path is not None \
            and directory_name != '' and directory_name is not None:

        name_available = _is_directory_name_available(
            path=directory_path,
            directory_name=directory_name
        )

        str_is_valid = utils.string_is_valid(
            directory_name,
            allowed_characters
        )

        return str_is_valid and name_available

    return False


def is_directory(
        path: str):
    """
    - Checks if a directory exists.

    :param path: Directory path.

    :return:    - True if the directory exists;
                - False otherwise.
    """

    return os.path.isdir(path)


def is_file(
        path: str):
    """
    - Checks if a file exists.

    :param path: Directory path.

    :return:    - True if the file exists;
                - False otherwise.
    """

    return os.path.isfile(path)


def delete_file(
        path: str):
    """
    - Deletes a file.

    :param path: File path.
    """

    if is_file(path=path):
        os.remove(path)


def _get_directory_content(
        directory_path: str,
        allowed_dot: bool,
        validation_method):
    """
    :param directory_path: Directory path. 
    :param validation_method: Validation method.
    :param allowed_dot: If True the list will contain dot files/directories. 

    :return: List with the files/directories contained by the directory with
             the path directory_path. 
    """

    subdirectories = os.listdir(directory_path)

    length = len(subdirectories)
    index = 0

    while index < length:
        path = directory_path + '/' + subdirectories[index]

        if not allowed_dot and subdirectories[index][0] == '.' \
                or not validation_method(path=path):

            del subdirectories[index]
            length = length - 1
        else:
            index = index + 1

    return subdirectories


def get_files(
        directory_path: str,
        allowed_dot=False):
    """
    :param directory_path: Directory path. 
    :param allowed_dot: If True the list will contain dot files. 

    :return: List with the files contained by the directory with the path
             directory_path. 
    """

    return _get_directory_content(validation_method=is_file,
                                  directory_path=directory_path,
                                  allowed_dot=allowed_dot)


def get_directories(
        directory_path: str,
        allowed_dot=False):
    """
    :param directory_path: Directory path. 
    :param allowed_dot: If True the list will contain dot directories. 

    :return: List with the directories contained by the directory with the 
             path directory_path. 
    """

    return _get_directory_content(validation_method=is_directory,
                                  directory_path=directory_path,
                                  allowed_dot=allowed_dot)


def crete_directory(
        directory_path: str):
    """
    - Creates a new directory if it does not exist already.

    :param directory_path: New directory path.

    :return:    - True if the directory was created
                - False if the directory already exists.
    """

    if not is_directory(directory_path):
        os.makedirs(directory_path)

        return True
    else:
        return False


def write_string_to_file(
        file_content: str,
        file_path: str):
    """
    - Creates a new file with the path file_path that contains file_content.

    :param file_content: File content as string.
    :param file_path: File path.
    """

    # TODO

    pass


def read_file_as_string(
        file_path: str):
    """
    - Reads the file file_path and returns the content as a string.

    :param file_path: File path.

    :return: File content.
    """

    # TODO

    pass


def file_sha512(
        file_name: str):
    """
    :param file_name: File name.

    :return: sha3_512 of the file.
    """

    _hash = hashlib.sha512()

    with open(file_name, 'rb') as file:
        chunk = 0

        while chunk != b'':
            chunk = file.read(1024)
            _hash.update(chunk)

    return _hash.hexdigest()


def file_md5sum(
        file_name: str):
    """
    :param file_name: File name.

    :return: md5sum of the file.
    """

    _hash = hashlib.md5()

    with open(file_name, 'rb') as file:
        chunk = 0

        while chunk != b'':
            chunk = file.read(1024)
            _hash.update(chunk)

    return _hash.hexdigest()


def remove_last_entry_from_path(
        path: str):
    """
    - Use this to remove the last entry from a path.

    :param path: Initial path.

    :return: New path with the last entry removed.
    """

    splitted = path.split('/')
    new_path = ''

    for index in range(len(splitted) - 1):
        new_path += '/' + splitted[index]

    return new_path


def copy_file(
        file_path: str,
        destination_path: str):
    """
    - Copies file_path to destination.

    :param file_path: Path of the file to copy.
    :param destination_path: Destination path.
    """

    if isinstance(destination_path, str) and isinstance(file_path, str) \
            and is_file(file_path) and is_directory(destination_path):
        shutil.copy(file_path, destination_path)
    else:
        raise ValueError(
            '\n* ' + str(file_path) + ' must be a file.'
            + '\n* ' + str(destination_path) + ' must be a directory.'
        )
