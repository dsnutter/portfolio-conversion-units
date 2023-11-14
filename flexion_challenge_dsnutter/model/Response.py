from ..helpers.Enums import GradeTypes
from .Base_Model import Base_Model
from .Conversion import Conversion

class Response(Base_Model):

    date_format = '%Y-%m-%d %I:%M %p'

    """
    def __init__(self, hashmap: dict) -> None:
        self._response = hashmap['response']
        self._student_id = hashmap['student_id'].upper()
        self._answer = hashmap['answer']
        self._from_type = hashmap['from_type']
        self._to_type = hashmap['to_type']
        self._grade = hashmap['grade']
        self._timestamp = hashmap['timestamp']
        self._id = hashmap['ID']
    """
    
    def __init__(self, student_id: str, response: str, answer: str, from_type: str, to_type: str, timestamp: str, grade: GradeTypes, ID: str) -> None:
        self._response = response   
        self._student_id = student_id.upper()
        self._answer = answer
        self._from_type = from_type
        self._to_type = to_type
        self._grade = grade
        self._timestamp = timestamp
        self._id = ID

    @property
    def grade(self) -> GradeTypes:
        return self._grade

    @grade.setter
    def grade(self, value: GradeTypes) -> None:
        self._grade = value

    @property
    def response(self) -> str:
        return self._response

    @response.setter
    def response(self, value: str) -> None:
        self._response = value

    @property
    def answer(self) -> str:
        return self._answer

    @answer.setter
    def answer(self, value: str) -> None:
        self._answer = value

    @property
    def from_type(self) -> str:
        return self._from_type

    @from_type.setter
    def from_type(self, value: str) -> None:
        self._from_type = value

    @property
    def to_type(self) -> str:
        return self._to_type

    @to_type.setter
    def to_type(self, value: str) -> None:
        self._to_type = value

    @property
    def timestamp(self) -> str:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: str) -> None:
        self._timestamp = value

    @property
    def student_id(self) -> str:
        return self._student_id

    @student_id.setter
    def student_id(self, value: str) -> None:
        self._student_id = value.upper()

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    # if needed later
    # @property
    # def timestamp_as_ticks(self) ->:
    #     return self._timestamp

    def __str__(self) -> str:
        result = 'Response: {}\n'.format(self._response)
        result += 'Grade: {}\n'.format(self._grade)
        return result

    def __dict__(self) -> dict:
        hashmap = {
            self._student_id : [
                {
                    "response": self._response,
                    "answer": self._answer,
                    "from_type": self._from_type,
                    "to_type": self._to_type,
                    "grade": self._grade,
                    "timestamp": self._timestamp,
                    "ID": self._id
                }
            ]
        }
        return hashmap

