from abc import ABCMeta, abstractmethod
from typing import Dict, Any, List
from abc import abstractmethod

from data_storage.SingletonMeta import SingletonMeta
from data_model.DataModelable import DataModelable
from data_storage.ABCAndSingletonMeta import ABCAndSingletonMeta


class Pool(metaclass=ABCAndSingletonMeta):
    @abstractmethod
    def add_data(self, data: DataModelable) -> None:
        pass

    @abstractmethod
    def get_data(self, condition: Dict[str, Any] = None) -> List[DataModelable]:
        pass

    @abstractmethod
    def remove_data(self, condition: Dict[str, Any] = None) -> None:
        pass

    def _find_data(self, data_pool: List[DataModelable], condition: Dict[str, Any]) -> Dict[int, DataModelable]:
        index: int = 0
        search_results: Dict[int, DataModelable] = {}

        for data in data_pool:
            structured_data: Dict[str, Any] = data.get_data()
            matched: bool = True

            for key, value in condition.items():
                if key not in structured_data or structured_data[key] != value:
                    matched = False
                    break

            if matched or condition is None:
                search_results[index] = data

            index += 1

        return search_results
