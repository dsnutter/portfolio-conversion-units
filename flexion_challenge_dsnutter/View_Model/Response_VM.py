from ..helpers.Enums import GradeTypes
from ..Model import Response
from .Base_VM import Base_VM
from typing import Callable, List
from datetime import datetime
import uuid

# controls operations on the reponse Models, and persistance
class Response_VM(Base_VM):

    def __init__(self, response_type: str, config: dict, factory: Callable[..., Response.Response], load_preexisting: bool = False) -> None:
        self._response_type = response_type
        if response_type in config:
            self._config = config[response_type]
        else:
            self._config = {}
        self._response_factory = factory
        self._storage = {}
        self._load_preexisting = load_preexisting
        
    @property
    def all_from_types(self) -> List:
        # self.generate_preexisting_responses()
        return self._storage.keys()

    def all_to_types(self, from_type: str) -> List:
        if from_type not in self._storage:
            return []
        # self.generate_preexisting_responses()
        return self._storage[from_type].keys()

    def all_students(self, from_type: str, to_type: str) -> list:
        if from_type not in self._storage or to_type not in self._storage[from_type]:
            return []
        # self.generate_preexisting_responses()
        return self._storage[from_type][to_type].keys()

    def get_responses(self, from_type: str, to_type: str, student_id: str) -> dict:
        # self.generate_preexisting_responses()
        return self._storage[from_type][to_type][student_id]

    def get_response(self, from_type: str, to_type: str, student_id: str, timestamp: str) -> Response.Response:
        # self.generate_preexisting_responses()

        # result = next(filter(lambda arr: any(datetime.strptime(item.timestamp, format) == datetime.strptime(timestamp, format))), self._storage[from_type][to_type][student_id]), None)
        result: Response
        for item in self._storage[from_type][to_type][student_id]:
            if datetime.strptime(item.timestamp, Response.Response.date_format) == datetime.strptime(timestamp, Response.Response.date_format):
                result = item
                break
        return result

    # def filter_response_by_exact_student_id(self, arr: list, timestamp: str):
    #     date_format = '%Y-%m-%d %I:%M %p'
    #     return any(datetime.strptime(item.timestamp, format) == datetime.strptime(timestamp, format) for item in arr)

    # def filter_response_by_exact_primary_key(self, arr: list, timestamp: str):
    #     date_format = '%Y-%m-%d %I:%M %p'
    #     return any(datetime.strptime(item.timestamp, format) == datetime.strptime(timestamp, format) for item in arr)

    # DSN Notes: this needs better test coverage
    def add_response(self, student_id: str, response: str, answer: str, from_type: str, to_type: str, timestamp: str, override_grade: str = None, ID: str = None):
        # self.generate_preexisting_responses()
        if override_grade is not None:
            grade = override_grade
        else:
            grade = Response_VM.grade_answer(response, answer)

        if from_type not in self._storage:
            self._storage[from_type] = {}
        if to_type not in self._storage[from_type]:
            self._storage[from_type][to_type] = {}
        if student_id not in self._storage[from_type][to_type]:
            self._storage[from_type][to_type][student_id] = []
        if ID is None or ID == '':
            ID = uuid.uuid4()

        self._storage[from_type][to_type][student_id].append(self._response_factory(student_id=student_id, 
                                                                                    response=response, 
                                                                                    answer=answer, 
                                                                                    from_type=from_type, 
                                                                                    to_type=to_type, 
                                                                                    timestamp=timestamp, 
                                                                                    grade=grade, 
                                                                                    ID=ID))
                                                                                
    # DSN Notes: this needs better test coverage
    def add_reponse(self, hashmap: dict):
        if 'grade' not in hashmap:
            grade = Response_VM.grade_answer(hashmap['response'], hashmap['answer'])
        else:
            grade = hashmap['grade']

        from_type = hashmap['from_type']
        to_type = hashmap['to_type']
        student_id = hashmap['student_id']
        if 'ID' not in hashmap:
            ID = None
            hashmap['ID'] = None
        if 'timestamp' not in hashmap:
            timestamp = datetime.now().strftime(Response.Response.date_format)
        else:
            timestamp = hashmap['timestamp']

        if from_type not in self._storage:
            self._storage[from_type] = {}
        if to_type not in self._storage[from_type]:
            self._storage[from_type][to_type] = {}
        if student_id not in self._storage[from_type][to_type]:
            self._storage[from_type][to_type][student_id] = []
        if hashmap['ID'] is None or hashmap['ID'] == '':
            ID = uuid.uuid4()

        self._storage[from_type][to_type][student_id].append(self._response_factory(student_id=student_id, 
                                                                                    response=hashmap['response'], 
                                                                                    answer=hashmap['answer'], 
                                                                                    from_type=from_type, 
                                                                                    to_type=to_type, 
                                                                                    timestamp=timestamp, 
                                                                                    grade=grade, 
                                                                                    ID=ID))


    def generate_preexisting_responses(self):
        if self._load_preexisting and self._storage == {}:
            self._load_preexisting = False
            items = self._config
            for student_id in items.keys():
                for inner in items[student_id]:
                    self.add_response(student_id, inner['response'], inner['answer'], inner['from_type'], inner['to_type'], inner['timestamp'], inner['grade'], inner['ID'])

    @staticmethod
    def grade_answer(response: str, answer: str) -> None:
        try:
            if round(float(response), 1) == round(float(answer), 1):
                grade = GradeTypes.CORRECT
            else:
                grade = GradeTypes.INCORRECT
        except ValueError:
            grade = GradeTypes.INCORRECT
        return grade

    def __str__(self) -> str:
        result = 'Response Controller: {}\n'.format(self._response_type)
        result = 'Response Controller: {}\n'.format(self._storage)
        return result

