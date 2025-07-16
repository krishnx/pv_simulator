from abc import ABC, abstractmethod


class IBroker(ABC):
    """
    Interface for message broker clients.
    """

    @abstractmethod
    def publish(self, message: dict):
        pass

    @abstractmethod
    def consume(self, callback):
        pass
