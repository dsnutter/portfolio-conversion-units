from ..helpers.Enums import BackendTypes
from ..helpers.Data_Functions import Data_Functions

#
# for importing configurations from datastores for di
#


class Configurations():
    def __init__(self, file_type: BackendTypes,
                 filename_conversions: str,
                 filename_responses: str,
                 filename_conversions_filter: str) -> None:
        self._conversions_config_file = filename_conversions
        self._responses_config_file = filename_responses
        self._conversions_filter_config_file = filename_conversions_filter
        self._file_type = file_type

        if filename_conversions is not None:
            self._conversions_config = Data_Functions.conversions_file_to_dict(filename_conversions, file_type)
        else:
            self._conversions_config = {}
        if filename_conversions_filter is not None:
            self._conversions_filter_config = \
                Data_Functions.conversions_filter_file_to_dict(filename_conversions_filter, file_type)
        else:
            self._conversions_filter_config = {}
        if filename_responses is not None:
            self._responses_config = Data_Functions.responses_file_to_dict(filename_responses, file_type)
        else:
            self._responses_config = {}

    @property
    def file_type(self):
        return self._file_type

    @property
    def conversions_config_file(self):
        return self._conversions_config_file

    @conversions_config_file.setter
    def conversions_config_file(self, value):
        self._conversions_config_file = value

    @property
    def conversions_filter_config_file(self):
        return self._conversions_filter_config_file

    @conversions_filter_config_file.setter
    def conversions_filter_config_file(self, value):
        self._conversions_filter_config_file = value

    @property
    def responses_config_file(self):
        return self._responses_config_file

    @responses_config_file.setter
    def responses_config_file(self, value):
        self._responses_config_file = value

    @property
    def conversions_config(self):
        return self._conversions_config

    @conversions_config.setter
    def conversions_config(self, value):
        self._conversions_config = value

    @property
    def conversions_filter_config(self):
        return self._conversions_filter_config

    @conversions_filter_config.setter
    def conversions_filter_config(self, value):
        self._conversions_filter_config = value

    @property
    def responses_config(self):
        return self._responses_config

    @responses_config.setter
    def responses_config(self, value):
        self._responses_config = value

    @property
    def types(self):
        # types = ['temperature', 'volume']
        types = list(self._conversions_config.keys())

        return types

    def __str__(self) -> str:
        result = 'Configurations:'
        result += 'Conversions Config File: {}\n'.format(self._conversions_config_file)
        result += 'Responses Config File: {}\n'.format(self._responses_config_file)
        return result
