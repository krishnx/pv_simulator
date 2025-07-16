from abc import ABC, abstractmethod


class ILogger(ABC):
    """
    Interface for logging data.
    """

    @abstractmethod
    def log(self, data: dict):
        pass
