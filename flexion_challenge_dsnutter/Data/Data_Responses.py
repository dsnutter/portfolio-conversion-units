from .Data_Abstract import Data_Abstract
from ..Model import Response
from ..helpers.Enums import BackendTypes
from ..helpers.Data_Functions import Data_Functions

class Data_Responses(Data_Abstract):

    def add(self, type:str, hashmap: dict, persist: bool = True):
        raise NotImplementedError()
    
    def get(self, ID: str):
        raise NotImplementedError()

    def update(self, hashmap: dict):
        raise NotImplementedError()

    def delete(self, hashmap: dict):
        raise NotImplementedError()
    
    def get_by_student_id(self, student_id: str):
        raise NotImplementedError()
    
    def get_response(self, from_type: str, to_type: str, student_id: str, timestamp: str) -> Response.Response:
        raise NotImplementedError()

    def all_keys(self):
        raise NotImplementedError()
    
    def get_responses(self) -> dict:
        raise NotImplementedError()
    
    def execute_load_preexisting(self, filename: str, file_type: BackendTypes):
        return Data_Functions.responses_file_to_dict(filename, file_type)



