from abc import ABC, abstractmethod


class IProducer(ABC):
    """
    Interface for data producers.
    """

    @abstractmethod
    def produce(self):
        pass
