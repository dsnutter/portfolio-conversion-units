from typing import Callable
from .Conversion import Conversion
import json
from enum import Enum
from typing import List

# is DI singleton
class Conversions_Many:

    def __init__(self, conversion_type: str, config: json, conversion_factory: Callable[..., Conversion]) -> None:
        # print('type of many conversion: {}\n'.format(conversion_type))
        # print('configuration JSON: {}\n'.format(config))

        self._storage = {}
        self._conversion_factory = conversion_factory
        self._config = config[conversion_type]
        self._conversion_type = conversion_type

        for from_type in self._config:
            if from_type not in self._storage:
                self._storage[from_type] = {}
            for to_type in self._config[from_type]:
                # DSN Notes: eq will be converted to py meth lambda function
                # fnEq = lambda x: meth(eq)
                # will not use eval() here due to security reasons of being able to shell out to host os
                #   and delete files for instance
                eq = self._config[from_type][to_type]
                obj = self._conversion_factory(from_type, to_type, eq)
                self._storage[from_type][to_type] = obj

    @property
    def all(self):
        return self._storage

    @property
    def all_from_types(self):
        return self._storage.keys()

    def all_to_types(self, from_type) -> List:
        list = []
        # print(self._storage)
        for item in self._storage[from_type]:
            list.append(item)
            # print(item)
        return list

    def conversion(self, from_type, to_type):
        return self._storage[from_type][to_type]
