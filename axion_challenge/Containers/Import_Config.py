import json
from model.Conversion import Conversion
from typing import List

class Import_Config:
    
    def __init__(self, filename):
        self._filename = filename

    def to_json(self):
        to_build = json.load(open(self._filename))

        return to_build

        # list = []
        # for outerkey, dict in to_build.iter_items():
        #     for innerkey, value in dict.iter_items():
        #         print(outerkey, innerkey, value)
        #         fn = value
        #         item = Conversion(outerkey)
        #         item.define_conversion(innerkey, fn)