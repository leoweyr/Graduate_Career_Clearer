from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class Evaluable(metaclass=ABCMeta):
    @abstractmethod
    def _judge(self, target: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    def _conclude(self, result: Dict[str, Any]) -> None:
        pass

    def evaluate(self, target: Any) -> None:
        """
        Non-overridable.
        """
        self._conclude(self._judge(target))
