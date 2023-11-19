from ..helpers.Enums import BackendTypes
from .Base_Abstract import Base_Abstract
from ..di.Configurations import Configurations


class Base_VM(Base_Abstract):

    def __init__(self, question_type: str, backend_type: BackendTypes, config: Configurations) -> None:
        self._question_type = question_type
        self._backend_type = backend_type
        self._all_types = (config.conversions_config.keys())
        self._config = config

    @property
    def all_types(self) -> list:
        return self._all_types

    @property
    def current_type(self) -> list:
        return self._question_type

    """
    def save(self):
        raise NotImplementedError()

    def all_to_types(self, from_type: str) -> list:
        raise NotImplementedError()

    @property
    def all_from_types(self) -> list:
        raise NotImplementedError()

    def add(self, hashmap: dict):
        raise NotImplementedError()
    """
