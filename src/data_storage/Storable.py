from abc import ABCMeta, abstractmethod
from typing import Dict, Any


class Storable(metaclass=ABCMeta):
    @abstractmethod
    def __getstate__(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def __setstate__(self, state: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def is_indexable(self) -> bool:
        pass

    @abstractmethod
    def get_metadata(self) -> Dict[str, str]:
        pass
