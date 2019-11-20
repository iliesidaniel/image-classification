from project_exceptions.session_exceptions import CorruptMainSessionFile
from utils.train.session_details import SessionDetails

from json import JSONDecodeError


import json


class SessionRW:
    """
    - Reads and writes the file that contains the session  details.
    """

    #########################################################################
    # File writing methods

    @staticmethod
    def write_session_details_file(
            session_details_file_path: str,
            session_details: SessionDetails):
        """
        - Writes the file that contains the session details.

        :param session_details_file_path: NewFileDetails instance.
        :param session_details: SessionDetails instance.
        """

        json_str = session_details.to_json()

        with open(session_details_file_path, 'w') as outfile:
            json.dump(
                json_str, outfile,
                sort_keys=False,
                indent=4,
                separators=(',', ': '),
                ensure_ascii=False
            )

    @staticmethod
    def read_main_session_file(
            session_file_path: str):
        """
        - Reads the file that contains the session details.

        :param session_file_path: 
        """

        try:
            with open(session_file_path) as data_file:
                data_loaded = json.load(data_file)

                session_details = SessionDetails()

                session_details.from_json(data_loaded)

                return session_details
        except (KeyError, JSONDecodeError) as exception:
            raise CorruptMainSessionFile(
                'The file "' + str(session_file_path) + '" is corrupt.'
            ) from exception

    #########################################################################
