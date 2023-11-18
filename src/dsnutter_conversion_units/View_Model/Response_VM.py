from ..helpers.Enums import GradeTypes, BackendTypes
from ..Model import Response
from .Base_VM import Base_VM
from typing import Callable
from datetime import datetime
import uuid
from ..di.Configurations import Configurations
from ..Data import Data_Responses
from .Conversion_VM import Conversion_VM
from ..helpers.functions import Functions

# controls operations on the reponse Models, and persistance


class Response_VM(Base_VM):

    def __init__(self, type: str, backend_type: BackendTypes, config: Configurations, 
                 factory: Callable[..., Response.Response], data: Data_Responses.Data_Responses) -> None:
        super(Response_VM, self).__init__(type, backend_type, config)
        self._factory = factory
        self._data = data  # singleton
        self._convert_input = None

    def all_keys(self) -> list:
        return self._data.all_keys()

    def all_keys_level2(self, key: str) -> list:
        raise NotImplementedError()

    def all_to_types(self, from_type: str) -> list:
        raise NotImplementedError()

    def all_keys_level3(self, key_outer: str, key_inner) -> list:
        raise NotImplementedError()

    def all_students(self) -> list:
        return self.all_keys()

    def get_responses(self) -> dict:
        return self._data.get_responses()

    # commenting out until we need this in the future due to linter
    # def get_responses(self, student_id: str) -> dict:
    #     return self._data.get_by_student_id(student_id)

    def get_response(self, from_type: str, to_type: str, student_id: str, timestamp: str) -> Response.Response:
        return self._data.get_response(from_type, to_type, student_id, timestamp)

    # DSN Notes: this needs better test coverage
    # DSN Notes: this is intended to add multiple items and needs changed
    def add(self, hash_key: str, hashmap: dict, persist: bool = True):
        if 'grade' not in hashmap:
            (input_value_rounded, input_value_calculated, grade) = self.grade_input_value(
                hashmap['from_type'], hashmap['to_type'], hashmap['response'], hashmap['input_value'])
            hashmap['grade'] = grade
        else:
            grade = hashmap['grade']
            input_value_calculated = None
            input_value_rounded = None

        from_type = hashmap['from_type']
        to_type = hashmap['to_type']
        student_id = hash_key
        if 'ID' not in hashmap:
            ID = None
            hashmap['ID'] = None
        if 'timestamp' not in hashmap:
            timestamp = hashmap['timestamp'] = datetime.now().strftime(Response.Response.date_format)
        else:
            timestamp = hashmap['timestamp']

        if hashmap['ID'] is None or hashmap['ID'] == '':
            ID = hashmap['ID'] = str(uuid.uuid4())
        else:
            ID = hashmap['ID']

        obj = self._factory(student_id=student_id,
                            response=hashmap['response'],
                            input_value=hashmap['input_value'],
                            from_type=from_type,
                            to_type=to_type,
                            timestamp=timestamp,
                            grade=grade,
                            ID=ID,
                            input_value_rounded=input_value_rounded,
                            input_value_calculated=input_value_calculated)
        self._data.add(self._type, {'obj': obj, 'student_id': student_id}, persist)

        return obj

    def execute_load_preexisting(self):
        items = self._data.execute_load_preexisting(self._config.responses_config_file, self._config.file_type)
        items = items[self._type]
        for student_id in items.keys():
            for inner in items[student_id]:
                # do not persist to storage since its already there
                self.add(student_id, inner, False)

    @property
    def conversion(self):
        return self._c_vm

    @conversion.setter
    def conversion(self, value: Conversion_VM):
        self._c_vm = value

    # must set conversion before executing this
    def grade_input_value(self, from_type: str, to_type: str, response: str, input_value: str) -> None:
        try:
            if self._convert_input is None:
                raise ModuleNotFoundError("Please set a conversion view model before calling Response_VM.grade_input_value")
            input_value_rounded, input_value_calculated = self._convert_input(input_value, from_type, to_type)

            if Functions.round_float_decimal_places(input_value_rounded, 1) == \
                Functions.round_float_decimal_places(response, 1):
                grade = GradeTypes.CORRECT
            else:
                grade = GradeTypes.INCORRECT
        except ValueError:
            grade = GradeTypes.INCORRECT
            input_value_rounded, input_value_calculated = None, None

        if from_type not in self._config.conversions_config[self._type]:
            grade = GradeTypes.INVALID
        elif to_type not in self._config.conversions_config[self._type][from_type]:
            grade = GradeTypes.INVALID

        return (input_value_rounded, input_value_calculated, grade)

    def save(self):
        raise NotImplementedError()

    def to_dataframe_all(self, for_display = False):
        return self._data.to_dataframe_all(for_display)

    def __str__(self) -> str:
        result = 'Response View Model: {}\n'.format(self._type)
        result = 'Response View Model: {}\n'.format(self._storage)
        return result
