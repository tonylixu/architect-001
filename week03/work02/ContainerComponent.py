from abc import ABC, abstractmethod


class ContainerComponent(ABC):
    """Abstract component class"""
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def add_node(self):
        pass
