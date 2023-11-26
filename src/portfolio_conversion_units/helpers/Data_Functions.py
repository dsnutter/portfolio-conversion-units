from ..helpers.Enums import BackendTypes
import json
import csv
import os.path

class Data_Functions:
    @staticmethod
    def conversions_file_to_dict(filename: str, file_type: BackendTypes) -> dict:
        try:
            if file_type == BackendTypes.CSV:
                with open(filename, newline='') as file:
                    lines = csv.DictReader(f=file, delimiter=',')
                    result = {}
                    for items in lines:
                        # DSN Notes: not totally sure this is the correct way to do this
                        if items["Type"] not in result:
                            result[items["Type"]] = {}
                        if items["From"] not in result[items["Type"]]:
                            result[items["Type"]][items["From"]] = {}
                        if items["To"] not in result[items["Type"]][items["From"]]:
                            result[items["Type"]][items["From"]][items["To"]] = {}
                        result[items["Type"]][items["From"]][items["To"]]['eq'] = items["equation"]
                        result[items["Type"]][items["From"]][items["To"]]['ID'] = items["ID"]
                file.close()
                return result
            elif file_type == BackendTypes.JSON:
                result = json.load(open(filename))
            else:
                result = None

            return result
        except FileNotFoundError:
            return {}

    @staticmethod
    def responses_file_to_dict(filename: str, file_type: BackendTypes) -> dict:
        try:
            if file_type == BackendTypes.CSV:
                with open(filename, newline='') as file:
                    lines = csv.DictReader(f=file, delimiter=',')
                    result = {}
                    for items in lines:
                        # DSN Notes: not totally sure this is the correct way to do this
                        if items["Type"] not in result:
                            result[items["Type"]] = {}
                        if items["student_id"] not in result[items["Type"]]:
                            result[items["Type"]][items["student_id"]] = []
                        result[items["Type"]][items["student_id"]].append({
                            "response": items["response"],
                            "input_value": items["input_value"],
                            "from_type": items["from_type"],
                            "to_type": items["to_type"],
                            "grade": items["grade"],
                            "timestamp": items["timestamp"],
                            "ID": items["ID"]
                        })
                file.close()
                return result
            elif file_type == BackendTypes.JSON:
                result = json.load(open(filename))
            else:
                result = None

            return result
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_conversion_dict_to_file(config: dict, filename: str, file_type: BackendTypes) -> dict:
        try:
            if file_type == BackendTypes.JSON:
                with open(filename, 'w+') as file:
                    json.dump(obj=config, fp=file, indent=4)
                file.close()
            elif file_type == BackendTypes.CSV:
                with open(filename, 'w+', newline='') as file:
                    lines = csv.DictWriter(file, ['Type', 'From', 'To', 'equation', 'ID'])
                    lines.writeheader()
                    for cname in config:
                        for from_c in config[cname]:
                            for to_c in config[cname][from_c]:
                                lines.writerow({'Type': cname, 'From': from_c, 'To': to_c,
                                               'equation': config[cname][from_c][to_c]['eq'],
                                                'ID': config[cname][from_c][to_c]['ID']})
                file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not write to: {filename}")

    @staticmethod
    def save_responses_dict_to_file(config: dict, filename: str, file_type: BackendTypes):
        try:
            if file_type == BackendTypes.JSON:
                with open(filename, 'w+') as file:
                    json.dump(obj=config, fp=file, indent=4)
                file.close()
            elif file_type == BackendTypes.CSV:
                with open(filename, 'w+', newline='') as file:
                    lines = csv.DictWriter(file, ['Type', 'student_id', 'response', 'input_value',
                                           'from_type', 'to_type', 'grade', 'timestamp', 'ID'])
                    lines.writeheader()
                    for cname in config:
                        for student_id in config[cname]:
                            for obj in config[cname][student_id]:
                                lines.writerow({'Type': cname,
                                                'student_id': student_id,
                                                'response': obj['response'],
                                                'input_value': obj['input_value'],
                                                'from_type': obj['from_type'],
                                                'to_type': obj['to_type'],
                                                'grade': obj['grade'],
                                                'timestamp': obj['timestamp'],
                                                'ID': obj['ID']})
                file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not write to: {filename}")

    @staticmethod
    def append_responses_dict_to_file(config: dict, filename: str, file_type: BackendTypes):
        try:
            if file_type == BackendTypes.JSON:
                raise NotImplementedError()
                # with open(filename, 'w+') as file:
                #     json.dump(obj=config, fp=file, indent=4)
            elif file_type == BackendTypes.CSV:
                # write head if does not exist already
                if os.path.isfile(filename) and os.path.getsize(filename) <= 0:
                    with open(filename, 'w+', newline='') as file:
                        lines = csv.DictWriter(file, ['Type', 'student_id', 'response', 'input_value',
                                            'from_type', 'to_type', 'grade', 'timestamp', 'ID'])
                        lines.writeheader()
                    file.close()
                new_lines = {}
                IDs = []
                # generate the new items
                for cname in config:
                    for student_id in config[cname]:
                        for obj in config[cname][student_id]:
                            IDs.append(str(obj['ID']))
                            new_lines[str(obj['ID'])] = {'Type': cname,
                                                         'student_id': student_id,
                                                         'response': obj['response'],
                                                         'input_value': obj['input_value'],
                                                         'from_type': obj['from_type'],
                                                         'to_type': obj['to_type'],
                                                         'grade': obj['grade'],
                                                         'timestamp': obj['timestamp'],
                                                         'ID': obj['ID']}

                with open(filename, 'a+', newline='') as file:
                    lines = csv.DictWriter(file, ['Type', 'student_id', 'response', 'input_value',
                                           'from_type', 'to_type', 'grade', 'timestamp', 'ID'])
                    # lines.writeheader()
                    for ID in IDs:
                        lines.writerow(new_lines[ID])
                file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not write to: {filename}")

    @staticmethod
    def conversions_filter_file_to_dict(filename: str, file_type: BackendTypes) -> dict:
        try:
            if file_type == BackendTypes.CSV:
                with open(filename, newline='') as file:
                    lines = csv.DictReader(f=file, delimiter=',')
                    result = {}
                    for items in lines:
                        if items["Type"] not in result:
                            result[items["Type"]] = {}
                        if items["To"] not in result[items["Type"]]:
                            result[items["Type"]][items["To"]] = {}
                        result[items["Type"]][items["To"]]['eq'] = items["equation"]
                        result[items["Type"]][items["To"]]['ID'] = items["ID"]
                        result[items["Type"]][items["To"]]['reason'] = items["Reason"]
                file.close()
                return result
            elif file_type == BackendTypes.JSON:
                result = json.load(open(filename))
            else:
                result = None

            return result
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_responses_filter_results_dict_to_file(config: dict, filename: str, file_type: BackendTypes):
        try:
            if file_type == BackendTypes.JSON:
                with open(filename, 'w+') as file:
                    json.dump(obj=config, fp=file, indent=4)
                file.close()
            elif file_type == BackendTypes.CSV:
                with open(filename, 'w+', newline='') as file:
                    lines = csv.DictWriter(file, ['Type', 'To', 'equation', 'Reason', 'ID'])
                    lines.writeheader()
                    for question_type in config:
                        for to_type in config[question_type]:
                            lines.writerow({'Type': question_type,
                                            'To': to_type,
                                            'equation': config[question_type][to_type]['eq'],
                                            'Reason': config[question_type][to_type]['reason'],
                                            'ID': config[question_type][to_type]['ID']})
                file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not write to: {filename}")
        
    @staticmethod
    def check_config_files_exist(file_conversions, file_responses, file_conversion_filters):
        if not os.path.isfile(file_conversions) or os.path.getsize(file_conversions) <= 0:
            print("There is a configuration issue with a file not existing or empty, please fix it")
            exit()
        if not os.path.isfile(file_responses):
            print("There is a configuration issue with a file not existing, please fix it")
            exit()
        if not os.path.isfile(file_conversion_filters) or os.path.getsize(file_conversion_filters) <= 0:
            print("There is a configuration issue with a file not existing or empty, please fix it")
            exit()


