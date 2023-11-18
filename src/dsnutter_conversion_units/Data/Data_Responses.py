from .Data_Abstract import Data_Abstract
from ..Model import Response
from ..helpers.Enums import BackendTypes
from ..helpers.Data_Functions import Data_Functions
import pandas as pd


class Data_Responses(Data_Abstract):

    def __init__(self) -> None:
        super().__init__()
        self._storage = {}

    def add(self, type: str, hashmap: dict, persist: bool = True):
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

    # future: wanted to make sure we can get responses into pandas so we can maybe analyze later
    #  for now, just used for markdown printing in the console
    def to_dataframe_all(self, for_display = False):
        thash = {}
        if for_display:
            keys = Response.Response.keys_for_display()
        else:
            keys = Response.Response.keys()
        for key in keys:
            thash[key] = []
        dfs = pd.DataFrame.from_dict(thash)
        # print(dfs)
        for student_id in self._storage:
            for obj in self._storage[student_id]:
                df = obj.to_dataframe(for_display)

                # reset pandas index numbers in both, so new ones are generated on concat
                df.reset_index(drop=True, inplace=True)
                dfs.reset_index(drop=True, inplace=True)

                # combine single response df with the many response objects
                dfs = pd.concat([dfs, df])
        # print(dfs)
        return dfs
