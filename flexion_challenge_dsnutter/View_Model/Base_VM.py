from ..helpers.Enums import BackendTypes
from .Base_Abstract import Base_Abstract

class Base_VM(Base_Abstract):

    def __init__(self, type: str, backend_type: BackendTypes, responses_config: dict = {}, conversions_config: dict = {}, load_preexisting: bool = False) -> None:
        self._type = type
        self._backend_type = backend_type
        self._load_preexisting = load_preexisting
        self._all_types = (conversions_config.keys())

        if type in responses_config:
            self._responses_config = responses_config[type]
        else:
            self._responses_config = {}
        if type in conversions_config:
            self._conversions_config = conversions_config[type]
        else:
            self._conversions_config = {}

    @property
    def all_types(self) -> list:
        return self._all_types

    """
    # persist exising items in memory to storage
    def save(self):
        raise NotImplementedError()

    def all_to_types(self, from_type: str) -> list:
        raise NotImplementedError()

    @property
    def all_from_types(self) -> list:
        raise NotImplementedError()

    def add(self, hashmap: dict):
        raise NotImplementedError()
    
    def load_preexisting(self):
        raise NotImplementedError()
    """
