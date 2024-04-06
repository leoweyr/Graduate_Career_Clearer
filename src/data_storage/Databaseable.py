from abc import ABCMeta, abstractmethod

from data_storage.DataContainer import DataContainer


class Databaseable(metaclass=ABCMeta):
    @abstractmethod
    def set_data_container(self, data_container: DataContainer) -> None:
        pass

    @abstractmethod
    def pull(self) -> None:
        pass

    @abstractmethod
    def push(self) -> None:
        pass
