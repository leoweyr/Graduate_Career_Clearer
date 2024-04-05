from abc import ABCMeta, abstractmethod
from typing import Dict, Any

from data_model.DataModelable import DataModelable


class Evaluable(metaclass=ABCMeta):
    @abstractmethod
    def _judge(self, target: DataModelable) -> Dict[str, Any]:
        pass

    @abstractmethod
    def _conclude(self, result: Dict[str, Any]) -> None:
        pass

    def evaluate(self, target: DataModelable) -> None:
        """
        Non-overridable.
        """
        self._conclude(self._judge(target))
