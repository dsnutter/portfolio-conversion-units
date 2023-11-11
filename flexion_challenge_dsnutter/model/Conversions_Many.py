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

        for fromType in self._config:
            if fromType not in self._storage:
                self._storage[fromType] = {}
            for toType in self._config[fromType]:
                # DSN Notes: eq will be converted to py meth lambda function
                # fnEq = lambda x: meth(eq)
                # will not use eval() here due to security reasons of being able to shell out to host os
                #   and delete files for instance
                eq = self._config[fromType][toType]
                obj = self._conversion_factory(fromType, toType, eq)
                self._storage[fromType][toType] = obj

    def get_all(self):
        return self._storage

    def get_all_from_types(self):
        return self._storage.keys()

    def get_all_to_types(self, fromType) -> List:
        list = []
        # print(self._storage)
        for item in self._storage[fromType]:
            list.append(item)
            # print(item)
        return list
