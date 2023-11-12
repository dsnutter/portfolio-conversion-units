from typing import Callable
from ..Model.Conversion import Conversion

# is DI singleton
class Conversions_Management():

    def __init__(self, conversion_type: str, config: dict, conversion_factory: Callable[..., Conversion]) -> None:
        self._conversion_factory = conversion_factory
        self._storage = config[conversion_type]
        self._conversion_type = conversion_type
        
    @property
    def all_from_types(self) -> list:
        return self._storage.keys()

    def all_to_types(self, from_type: str) -> list:
        return self._storage[from_type].keys()

    # we are only creating the conversions with the factory when needed and not all of them initially
    #  allows for less boilerplate code anad decoupling
    def conversion(self, from_type: str, to_type: str) -> Conversion:
        eq = self._storage[from_type][to_type]["eq"]

        self._storage[from_type][to_type]["obj"] = self._conversion_factory(from_type, to_type, eq)

        return self._storage[from_type][to_type]["obj"]

    def __str__(self) -> str:
        result = 'Conversion Type: {}\n'.format(self._conversion_type)
        result += '\tInternal Storage: {}\n'.format(self._storage)
        return result
