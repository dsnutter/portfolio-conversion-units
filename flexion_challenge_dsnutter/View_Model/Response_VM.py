from ..helpers.Enums import GradeTypes, BackendTypes
from ..Model import Response
from .Base_VM import Base_VM
from typing import Callable, List
from datetime import datetime
import uuid

# controls operations on the reponse Models, and persistance
class Response_VM(Base_VM):

    def __init__(self, type: str, backend_type: BackendTypes, responses_config: dict, conversions_config: dict, factory: Callable[..., Response.Response], load_preexisting: bool = False) -> None:
        super(Response_VM, self).__init__(type, backend_type, responses_config, conversions_config, load_preexisting)
        self._config = self._responses_config
        self._factory = factory
        self._storage = {}

    def all_keys(self) -> list:
        # self.generate_preexisting_responses()
        return list(self._storage.keys())

    def all_keys_level2(self, key: str) -> list:
        raise NotImplementedError()

    def all_to_types(self, from_type: str) -> list:
        raise NotImplementedError()
    
    def all_keys_level3(self, key_outer: str, key_inner) -> list:
        raise NotImplementedError()

    def all_students(self) -> list:
        return self.all_keys()

    def get_responses(self, student_id: str) -> dict:
        # self.generate_preexisting_responses()
        return self._storage[student_id]

    def get_response(self, from_type: str, to_type: str, student_id: str, timestamp: str) -> Response.Response:
        # self.generate_preexisting_responses()

        # result = next(filter(lambda arr: any(datetime.strptime(item.timestamp, format) == datetime.strptime(timestamp, format))), self._storage[from_type][to_type][student_id]), None)
        result = []
        for item in self._storage[student_id]:
            if datetime.strptime(item.timestamp, Response.Response.date_format) == datetime.strptime(timestamp, Response.Response.date_format) and from_type == item.from_type and to_type == item.to_type:
                result.append(item)
        return result

    # def filter_response_by_exact_student_id(self, arr: list, timestamp: str):
    #     date_format = '%Y-%m-%d %I:%M %p'
    #     return any(datetime.strptime(item.timestamp, format) == datetime.strptime(timestamp, format) for item in arr)

    # def filter_response_by_exact_primary_key(self, arr: list, timestamp: str):
    #     date_format = '%Y-%m-%d %I:%M %p'
    #     return any(datetime.strptime(item.timestamp, format) == datetime.strptime(timestamp, format) for item in arr)

    """
    # DSN Notes: this needs better test coverage
    def add_single(self, student_id: str, response: str, answer: str, from_type: str, to_type: str, timestamp: str, override_grade: str = None, ID: str = None):
        # self.generate_preexisting_responses()
        if override_grade is not None:
            grade = override_grade
        else:
            grade = self.grade_answer(from_type, to_type, response, answer)

        if from_type not in self._storage:
            self._storage[from_type] = {}
        if to_type not in self._storage[from_type]:
            self._storage[from_type][to_type] = {}
        if student_id not in self._storage[from_type][to_type]:
            self._storage[from_type][to_type][student_id] = []
        if ID is None or ID == '':
            ID = uuid.uuid4()

        self._storage[from_type][to_type][student_id].append(self._factory(student_id=student_id, 
                                                                                    response=response, 
                                                                                    answer=answer, 
                                                                                    from_type=from_type, 
                                                                                    to_type=to_type, 
                                                                                    timestamp=timestamp, 
                                                                                    grade=grade, 
                                                                                    ID=ID))
    """                                                                         
    # DSN Notes: this needs better test coverage
    # DSN Notes: this is intended to add multiple items and needs changed
    def add(self, hash_key: str, hashmap: dict):
        if 'grade' not in hashmap:
            grade = self.grade_answer(hashmap['from_type'], hashmap['to_type'], hashmap['response'], hashmap['answer'])
        else:
            grade = hashmap['grade']

        from_type = hashmap['from_type']
        to_type = hashmap['to_type']
        student_id = hash_key
        if 'ID' not in hashmap:
            ID = None
            hashmap['ID'] = None
        if 'timestamp' not in hashmap:
            timestamp = datetime.now().strftime(Response.Response.date_format)
        else:
            timestamp = hashmap['timestamp']

        if student_id not in self._storage:
            self._storage[student_id] = []
        if hashmap['ID'] is None or hashmap['ID'] == '':
            ID = uuid.uuid4()

        obj = self._factory(student_id=student_id, 
                                    response=hashmap['response'], 
                                    answer=hashmap['answer'], 
                                    from_type=from_type, 
                                    to_type=to_type, 
                                    timestamp=timestamp, 
                                    grade=grade, 
                                    ID=ID)
        self._storage[student_id].append(obj)
        print(obj)


    def execute_load_preexisting(self):
        if self._load_preexisting and self._storage == {}:
            self._load_preexisting = False
            items = self._config
            for student_id in items.keys():
                for inner in items[student_id]:
                    # self.add_single(student_id, inner['response'], inner['answer'], inner['from_type'], inner['to_type'], inner['timestamp'], inner['grade'], inner['ID'])
                    self.add(student_id, inner)

    def grade_answer(self, from_type: str, to_type: str, response: str, answer: str) -> None:
        try:
            if round(float(response), 1) == round(float(answer), 1):
                grade = GradeTypes.CORRECT
            else:
                grade = GradeTypes.INCORRECT
        except ValueError:
            grade = GradeTypes.INCORRECT

        if from_type not in self._conversions_config:
            grade = GradeTypes.INVALID
        elif to_type not in self._conversions_config[from_type]:
            grade = GradeTypes.INVALID

        return grade

    def save(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        result = 'Response Controller: {}\n'.format(self._response_type)
        result = 'Response Controller: {}\n'.format(self._storage)
        return result

