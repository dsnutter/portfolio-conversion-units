import json, csv
from ..helpers.Enums import FileTypes

#
# for importing configurations from datastores for di
#
class Configurations():
    def __init__(self, file_type: FileTypes, filename_conversions: str, filename_responses: str) -> None:
        self._conversions_config_file = filename_conversions
        self._responses_config_file = filename_responses
        self._file_type = file_type

        if filename_conversions is not None:
            self._conversions_config = Configurations.conversions_file_to_dict(filename_conversions, file_type)
        if filename_responses is not None:
            self._responses_config = Configurations.responses_file_to_dict(filename_responses, file_type)

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
        return self._responses_config_file

    @responses_config_file.setter
    def responses_config_file(self, value):
        self._responses_config_file = value

    @property
    def conversions_config(self):
        return self._conversions_config

    @property
    def responses_config(self):
        return self._responses_config

    @staticmethod
    def conversions_file_to_dict(filename: str, file_type: FileTypes) -> dict:
        if file_type == FileTypes.CSV:
            with open(filename, newline='') as file:
                lines = csv.DictReader(f=file, delimiter=',')
                result = {}
                for items in lines:
                    # DSN Notes: not totally sure this is the correct way to do this
                    if items["TypeConversion"] not in result == {}:
                        result[items["TypeConversion"]] = {}
                    if items["From"] not in result[items["TypeConversion"]]:
                        result[items["TypeConversion"]][items["From"]] = {}
                    if items["To"] not in result[items["TypeConversion"]][items["From"]]:
                        result[items["TypeConversion"]][items["From"]][items["To"]] = {}
                    result[items["TypeConversion"]][items["From"]][items["To"]]['eq'] = items["equation"]
                    result[items["TypeConversion"]][items["From"]][items["To"]]['ID'] = items["ID"]
                return result
        elif file_type == FileTypes.JSON:
            result = json.load(open(filename))
        else:
            result = None

        return result

    @staticmethod
    def responses_file_to_dict(filename: str, file_type: FileTypes) -> dict:
        if file_type == FileTypes.CSV:
            with open(filename, newline='') as file:
                lines = csv.DictReader(f=file, delimiter=',')
                result = {}
                for items in lines:
                    # DSN Notes: not totally sure this is the correct way to do this
                    if items["TypeResponses"] not in result:
                        result[items["TypeResponses"]] = {}
                    if items["student_id"] not in result[items["TypeResponses"]]:
                        result[items["TypeResponses"]][items["student_id"]] = []                    
                    result[items["TypeResponses"]][items["student_id"]].append({
                        "response": items["response"],
                        "answer": items["answer"],
                        "from_type": items["from_type"],
                        "to_type": items["to_type"],
                        "grade": items["grade"],
                        "timestamp": items["timestamp"],
                        "ID": items["ID"]
                    })
                return result
        elif file_type == FileTypes.JSON:
            result = json.load(open(filename))
        else:
            result = None

        return result

    @staticmethod
    def save_conversion_dict_to_file(config: dict, filename: str, file_type: FileTypes) -> dict:
        if file_type == FileTypes.JSON:
            with open(filename, 'w+') as file:
                json.dump(obj=config, fp=file, indent=4)
        elif file_type == FileTypes.CSV:
            with open(filename, 'w+', newline='') as file:
                lines = csv.DictWriter(file, [ 'TypeConversion', 'From', 'To', 'equation', 'ID' ])
                lines.writeheader()
                for cname in config:
                    for from_c in config[cname]:
                        for to_c in config[cname][from_c]:
                            lines.writerow({ 'TypeConversion': cname, 'From': from_c, 'To': to_c, 'equation': config[cname][from_c][to_c]['eq'], 'ID': config[cname][from_c][to_c]['ID'] })

    @staticmethod
    def save_responses_dict_to_file(config: dict, filename: str, file_type: FileTypes):
        if file_type == FileTypes.JSON:
            with open(filename, 'w+') as file:
                json.dump(obj=config, fp=file, indent=4)
        elif file_type == FileTypes.CSV:
            with open(filename, 'w+') as file:
                lines = csv.DictWriter(file, [ 'TypeResponses','student_id','response','answer','from_type','to_type','grade','timestamp', 'ID' ])
                lines.writeheader()
                for cname in config:
                    for student_id in config[cname]:
                        for obj in config[cname][student_id]:
                            lines.writerow({ 'TypeResponses': cname, 
                                                'student_id': student_id, 
                                                'response': obj['response'], 
                                                'answer': obj['answer'], 
                                                'from_type': obj['from_type'],
                                                'to_type': obj['to_type'], 
                                                'grade': obj['grade'], 
                                                'timestamp': obj['timestamp'],
                                                'ID': obj['ID']  })

    def __str__(self) -> str:
        result = 'Import/Export Controller'
        result += 'Conversions Config File: {}\n'.format(self._conversions_config_file)
        result += 'Repsonses Config File: {}\n'.format(self._responses_config_file)
        return result

