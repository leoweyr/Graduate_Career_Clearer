from abc import ABCMeta, abstractmethod


class Completable(metaclass=ABCMeta):
    @abstractmethod
    def get_completion_percentage(self) -> float:
        pass
