from abc import ABCMeta, abstractmethod

from data_storage.DataContainer import DataContainer


class Databaseable(metaclass=ABCMeta):
    @abstractmethod
    def pull(self) -> DataContainer:
        pass

    @abstractmethod
    def push(self, data: DataContainer) -> None:
        pass
