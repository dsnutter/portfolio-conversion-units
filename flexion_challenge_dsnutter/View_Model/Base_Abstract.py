from abc import ABC, abstractmethod
from ..helpers.Enums import BackendTypes

class Base_Abstract(ABC):

    @abstractmethod
    def __init__(self, type: str, backend_type: BackendTypes, responses_config: dict = None, conversions_config: dict = None, load_preexisting: bool = False) -> None:
        pass

    # persist exising items in memory to storage
    @abstractmethod
    def save(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def all_types(self) -> list:
        raise NotImplementedError()

    @abstractmethod    
    def all_keys(self) -> list:
        raise NotImplementedError()

    @abstractmethod    
    def all_keys_level2(self, key: str) -> list:
        raise NotImplementedError()

    @abstractmethod    
    def all_keys_level3(self, key_outer: str, key_inner) -> list:
        raise NotImplementedError()

    # DSN Notes: this needs better test coverage
    @abstractmethod    
    def add(self, hash_key: str, hashmap: dict):
        raise NotImplementedError()
    
    @abstractmethod    
    def execute_load_preexisting(self):
        raise NotImplementedError()


