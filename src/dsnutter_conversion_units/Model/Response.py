from ..helpers.Enums import GradeTypes
from .Base_Model import Base_Model
import pandas as pd


class Response(Base_Model):

    date_format = '%Y-%m-%d %I:%M %p'

    """
    def __init__(self, hashmap: dict) -> None:
        self._response = hashmap['response']
        self._student_id = hashmap['student_id'].upper()
        self._input_value = hashmap['input_value']
        self._from_type = hashmap['from_type']
        self._to_type = hashmap['to_type']
        self._grade = hashmap['grade']
        self._timestamp = hashmap['timestamp']
        self._id = hashmap['ID']
    """

    def __init__(self, student_id: str, response: str, input_value: str, from_type: str,
                 to_type: str, timestamp: str, grade: GradeTypes, ID: str,
                 input_value_rounded: float = None, input_value_calculated: float = None) -> None:
        self._response = response
        self._student_id = student_id.upper()
        self._input_value = input_value
        self._from_type = from_type
        self._to_type = to_type
        self._grade = grade
        self._timestamp = timestamp
        self._id = ID
        self._input_value_rounded = input_value_rounded
        self._input_value_calculated = input_value_calculated

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
    def input_value(self) -> str:
        return self._input_value

    @input_value.setter
    def input_value(self, value: str) -> None:
        self._input_value = value

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

    @property
    def input_value_rounded(self) -> float:
        return self._input_value_rounded

    @property
    def input_value_calculated(self) -> float:
        return self._input_value_calculated

    # if needed later
    # @property
    # def timestamp_as_ticks(self) ->:
    #     return self._timestamp

    def __str__(self) -> str:
        return str(self.to_dict())

    def keys():
        return ["student_id", "response", "input_value", "from_type", "to_type", "grade", "timestamp", "ID"]

    def to_dict(self) -> dict:
        hashmap = {
            self._student_id: [
                {
                    "student_id": self._student_id,
                    "response": self._response,
                    "input_value": self._input_value,
                    "from_type": self._from_type,
                    "to_type": self._to_type,
                    "grade": self._grade,
                    "timestamp": self._timestamp,
                    "ID": self._id
                }
            ]
        }
        return hashmap

    def to_dataframe(self) -> pd.DataFrame:
        hashmap = self.to_dict()
        index = 0
        cols = Response.keys()

        response = {}
        for col in cols:
            response[col] = [hashmap[self._student_id][index][col]]
        # print(response)

        df = pd.DataFrame.from_records(response)
        # print(df)

        return df
