from abc import ABC, abstractmethod


class Component(ABC):
    """Abstract component class"""
    @abstractmethod
    def print(self):
        pass
