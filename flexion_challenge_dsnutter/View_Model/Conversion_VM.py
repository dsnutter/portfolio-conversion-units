from .Base_VM import Base_VM
from typing import Callable
from ..Model.Conversion import Conversion

# controls operationss on the conversion Models, and persistance
class Conversion_VM(Base_VM):

    def __init__(self, conversion_type: str, config: dict, factory: Callable[..., Conversion]) -> None:
        self._conversion_factory = factory
        if conversion_type in config:
            self._storage = config[conversion_type]
        else:
            self._storage = {}
        self._conversion_type = conversion_type
    
    @property
    def all_from_types(self) -> list:
        return self._storage.keys()

    def all_to_types(self, from_type: str) -> list:
        return self._storage[from_type].keys()

    def convert(self, input: float, from_type, to_type) -> float:
        try:
            conversion_single = self.conversion(from_type, to_type)
            result = conversion_single.equation_lambda(input)
        except:
            raise ValueError("Cannot execute lambda function defined")

        return result

    # we are only creating the conversions with the factory when needed and not all of them initially
    #  allows for less boilerplate code anad decoupling
    # may need to revisit this code if this application becomes multi-threaded
    def conversion(self, from_type: str, to_type: str) -> Conversion:
        eq = self._storage[from_type][to_type]["eq"]

        # if a certain conversion object does not already exist, then create it
        # if not ('obj' in self._storage[from_type][to_type] or not ('obj' in self._storage[from_type][to_type] and self._storage[from_type][to_type]["obj"] is None)):
        self._storage[from_type][to_type]["obj"] = self._conversion_factory(from_type, to_type, eq)

        return self._storage[from_type][to_type]["obj"]

    def __str__(self) -> str:
        result = 'Conversion Type: {}\n'.format(self._conversion_type)
        result += '\tInternal Storage: {}\n'.format(self._storage)
        return result
