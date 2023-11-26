from abc import ABC, abstractmethod


class Data_Abstract(ABC):

    @abstractmethod
    def add(self, question_type: str, hashmap: dict):
        raise NotImplementedError()

    @abstractmethod
    def get(self, ID: str):
        raise NotImplementedError()

    @abstractmethod
    def update(self, hashmap: dict):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, hashmap: dict):
        raise NotImplementedError()
