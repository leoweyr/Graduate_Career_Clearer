from abc import ABCMeta, abstractmethod
from typing import Dict


class Storable(metaclass=ABCMeta):
    @abstractmethod
    def is_indexable(self) -> bool:
        pass

    @abstractmethod
    def get_metadata(self) -> Dict[str: str]:
        pass
