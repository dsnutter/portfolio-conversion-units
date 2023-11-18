from .Data_Responses import Data_Responses
from ..helpers.Enums import BasicTypes, BackendTypes
from ..helpers.Data_Functions import Data_Functions
from datetime import datetime
from ..Model import Response


class Data_Responses_CSV(Data_Responses):

    def __init__(self, type: BasicTypes, filename: str) -> None:
        super().__init__()
        self._type = type
        self._backend_type = BackendTypes.CSV
        self._filename = filename

    def add(self, type: str, hashmap: dict, persist: bool = True):
        if hashmap['student_id'] not in self._storage:
            self._storage[hashmap['student_id']] = []
        self._storage[hashmap['student_id']].append(hashmap['obj'])
        if persist:
            Data_Functions.append_responses_dict_to_file({type: hashmap['obj'].to_dict()}, self._filename, self._backend_type)

    def get_by_student_id(self, student_id: str):
        return self._storage[student_id]

    def get_response(self, from_type: str, to_type: str, student_id: str, timestamp: str) -> Response.Response:
        result = []
        for item in self._storage[student_id]:
            if datetime.strptime(item.timestamp, Response.Response.date_format) == \
                    datetime.strptime(timestamp, Response.Response.date_format) \
                    and from_type == item.from_type and to_type == item.to_type:
                result.append(item)
        return result

    def all_keys(self):
        return list(self._storage.keys())

    def get_responses(self) -> dict:
        return self._storage
