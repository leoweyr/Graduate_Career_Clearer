from abc import ABCMeta, abstractmethod


class Evaluable(metaclass=ABCMeta):
    @abstractmethod
    def _judge(self, object: object) -> dict:
        pass

    @abstractmethod
    def _conclude(self, **kwargs) -> None:
        pass

    @abstractmethod
    def evaluate(self, object: object) -> None:
        pass
