from abc import ABCMeta, abstractmethod


class DataModelable(metaclass=ABCMeta):
    @abstractmethod
    def is_completed(self) -> bool:
        pass