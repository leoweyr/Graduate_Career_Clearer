from abc import ABCMeta, abstractmethod
from typing import Dict


class DataModelable(metaclass=ABCMeta):
    @abstractmethod
    def is_completed(self) -> bool:
        pass
    
    @abstractmethod
    def get_data(self) -> Dict[str: object]:
        pass
