import json, csv
from .Base_Controller import Base_Controller
from ..helpers.Enums import FileTypes

#
# for importing configurations for conversions and old responses
#  that have been saved as JSON. This layer will allow replacement with
#  some type of data store/db in the future if we want it
#
class Import_Export_Config_Controller(Base_Controller):
    def __init__(self, file_type: FileTypes, filename_conversions: str, filename_responses: str) -> None:
        self._conversions_config_file = filename_conversions
        self._responses_config_file = filename_responses
        self._file_type = file_type

        self._conversions_config = Import_Export_Config_Controller.conversions_file_to_dict(filename_conversions, file_type)
        self._responses_config = Import_Export_Config_Controller.responses_file_to_dict(filename_responses, file_type)

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
    def responses_config_file(self):
        return self._conversions_config_file

    @responses_config_file.setter
    def responses_config_file(self, value):
        self._conversions_config_file = value

    @property
    def conversions_config(self):
        return self._conversions_config

    @property
    def responses_config(self):
        return self._conversions_config

    @staticmethod
    def conversions_file_to_dict(filename: str, file_type: FileTypes) -> dict:
        if file_type == FileTypes.CSV:
            with open(filename, newline='') as file:
                lines = csv.DictReader(f=file, delimiter=',')
                result = {}
                for items in lines:
                    # DSN Notes: not totally sure this is the correct way to do this
                    if result == {}:
                        result[items["TypeConversion"]] = {}
                    if result[items["TypeConversion"]] == {}:
                        result[items["TypeConversion"]][items["From"]] = {}
                    if result[items["TypeConversion"]][items["From"]] == {}:
                        result[items["TypeConversion"]][items["From"]][items["To"]] = ""
                    result[items["TypeConversion"]][items["From"]][items["To"]] = items["equation"]
                return result
        elif file_type == FileTypes.JSON:
            result = json.load(open(filename))
        else:
            result = None

        return result

    @staticmethod
    def responses_file_to_dict(sfilename: str, file_type: FileTypes) -> dict:
        pass

    def save_conversion_dict_to_file(self, filename: str, file_type: FileTypes) -> dict:
        if file_type == FileTypes.JSON:
            with open(filename, 'w') as file:
                json.dump(self._conversions_config, file)
        elif file_type == FileTypes.CSV:
            with open(filename, 'w') as file:
                lines = csv.DictWriter(file, [ 'TypeConversion', 'From', 'To', 'equation' ])
                lines.writeheader()
                for cname in self._conversions_config:
                    for from_c in self._conversions_config[cname]:
                        for to_c in self._conversions_config[cname][from_c]:
                            lines.writerow({ 'TypeConversion': cname, 'From': from_c, 'To': to_c, 'equation': self._conversions_config[cname][from_c][to_c] })

    def save_responses_config(self, filename: str, file_type: FileTypes):
        pass

    def __str__(self) -> str:
        result = 'Import/Export Controller'
        result += 'Conversions Config File: {}\n'.format(self._conversions_config_file)
        result += 'Repsonses Config File: {}\n'.format(self._responses_config_file)
        return result

