import uuid
from ..helpers.Enums import BackendTypes
from .Base_VM import Base_VM
from typing import Callable
from ..Model.Conversion import Conversion
from ..di.Configurations import Configurations
from ..helpers.functions import Functions
from decimal import Decimal

# controls operationss on the conversion Models, and persistance


class Conversion_VM(Base_VM):

    def __init__(self, question_type: str, backend_type: BackendTypes, config: Configurations,
                 factory: Callable[..., Conversion]) -> None:
        super(Conversion_VM, self).__init__(question_type, backend_type, config)

        self._factory = factory
        self._storage = self._config.conversions_config[question_type]
        self._response_factory = factory

    # future: persist exising items in memory to storage
    def save(self):
        raise NotImplementedError()

    def all_keys(self) -> list:
        return list(self._storage.keys())

    def all_to_types(self, from_types: str) -> list:
        if from_types not in self._storage:
            return []
        return list(self._storage[from_types].keys())

    @property
    def all_from_types(self) -> list:
        return self.all_keys()

    # returns result to two decimal places, so it can be rounded later
    def convert_input(self, input: float, from_type, to_type) -> Decimal:
        try:
            conversion_single = self.get_conversion_single(from_type, to_type)
            result_from_calc = str(conversion_single.equation_lambda(float(input)))
            # we want to round to two decimal places, then round to one due to the float/decimal
            #   precision 3.14159............... when converted to float
            #   i.e. it could be 1.4999999999999999 stored instead of the 1.5 intended
            #   we will round it to one later, not now
            result = Functions.round_float_decimal_places(str(result_from_calc), 2)
        except SyntaxError as se:
            raise SyntaxError(f'Cannot execute lambda function defined for conversion from {from_type} to {to_type}: {se}')
        except Exception as e:
            raise ValueError(f"Cannot execute lambda function defined for conversion from {from_type} to {to_type}: {e}")

        return result, result_from_calc

    # we are only creating the conversions with the factory when needed and not all of them initially
    #  allows for less boilerplate code anad decoupling
    # may need to revisit this code if this application becomes multi-threaded
    def get_conversion_single(self, from_type: str, to_type: str) -> Conversion:
        eq = self._storage[from_type][to_type]["eq"]
        id = self._storage[from_type][to_type]["ID"]

        if id is None or id == '':
            id = str(uuid.uuid4())

        if 'obj' not in self._storage[from_type][to_type]:
            # create conversion object if its does not already exist
            #  may needs revisted if application becomes multithreaded
            #  and there are locks and we need to write to it?
            self._storage[from_type][to_type]["obj"] = self._factory(from_type, to_type, eq, id)

        return self._storage[from_type][to_type]["obj"]

    # possible future: this may need implemented
    def add(self, hash_key: str, hashmap: dict):
        raise NotImplementedError()

    # possible future: this may need implemented
    def execute_load_preexisting(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        result = 'Conversion Type: {}\n'.format(self._conversion_type)
        result += '\tInternal Storage: {}\n'.format(self._storage)
        return result
