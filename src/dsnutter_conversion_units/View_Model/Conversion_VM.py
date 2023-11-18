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

    def __init__(self, type: str, backend_type: BackendTypes, config: Configurations, 
                 factory: Callable[..., Conversion]) -> None:
        super(Conversion_VM, self).__init__(type, backend_type, config)

        self._factory = factory
        self._storage = self._config.conversions_config[type]
        self._response_factory = factory

    # persist exising items in memory to storage
    def save(self):
        raise NotImplementedError()

    def all_keys(self) -> list:
        return list(self._storage.keys())

    def all_keys_level2(self, key: str) -> list:
        if key not in self._storage:
            return []
        return list(self._storage[key].keys())

    # does not really apply to conversions right now, so not implemented
    def all_keys_level3(self, key_outer: str, key_inner) -> list:
        raise NotImplementedError()

    @property
    def all_from_types(self) -> list:
        return self.all_keys()

    def all_to_types(self, from_type: str) -> list:
        return self.all_keys_level2(from_type)

    # returns result to two decimal places
    def convert_input(self, input: float, from_type, to_type) -> Decimal:
        try:
            conversion_single = self.conversion(from_type, to_type)
            result_from_calc = str(conversion_single.equation_lambda(float(input)))
            # we want to round to two decimal places, then round to one due to the float/decimal
            #   precision 3.14159............... when converted to float
            result = Functions.round_float_decimal_places(str(result_from_calc), 2)
        except SyntaxError as se:
            raise SyntaxError(f'Cannot execute lambda function defined for conversion from {from_type} to {to_type}: {se}')
        except Exception as e:
            raise ValueError(f"Cannot execute lambda function defined for conversion from {from_type} to {to_type}: {e}")

        return result, result_from_calc

    # we are only creating the conversions with the factory when needed and not all of them initially
    #  allows for less boilerplate code anad decoupling
    # may need to revisit this code if this application becomes multi-threaded
    def conversion(self, from_type: str, to_type: str) -> Conversion:
        eq = self._storage[from_type][to_type]["eq"]
        id = self._storage[from_type][to_type]["ID"]

        if id is None or id == '':
            id = str(uuid.uuid4())

        # create conversion object
        self._storage[from_type][to_type]["obj"] = self._factory(from_type, to_type, eq, id)

        return self._storage[from_type][to_type]["obj"]

    # DSN Notes: this needs better test coverage
    def add(self, hash_key: str, hashmap: dict):
        raise NotImplementedError()

    def execute_load_preexisting(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        result = 'Conversion Type: {}\n'.format(self._conversion_type)
        result += '\tInternal Storage: {}\n'.format(self._storage)
        return result
