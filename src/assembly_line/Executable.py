from abc import ABCMeta, abstractmethod


class Executable(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass
