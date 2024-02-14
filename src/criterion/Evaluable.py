from abc import ABCMeta, abstractmethod


class Evaluable(metaclass=ABCMeta):
    @abstractmethod
    def _judge(self, object: object) -> dict[str, object]:
        pass

    @abstractmethod
    def _conclude(self, result: dict[str, object]) -> None:
        pass

    def evaluate(self, object: object) -> None:
        """
        Non-overridable.
        """
        self._conclude(self._judge(object))
