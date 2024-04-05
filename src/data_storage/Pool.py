from abc import abstractmethod
from typing import Optional, Union, Dict, List

from pure_object_oriented.ABCAndSingletonMeta import ABCAndSingletonMeta
from data_storage.Storable import Storable
from data_storage.DataContainer import DataContainer


class Pool(metaclass=ABCAndSingletonMeta):
    @abstractmethod
    def add_data(self, data: Storable) -> None:
        pass

    @abstractmethod
    def get_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> List[Storable]:
        pass

    @abstractmethod
    def remove_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> None:
        pass

    def _find_data(self, data_pool: DataContainer, condition: Dict[str, str]) -> Dict[int, Storable]:
        index: int = 0
        search_results: Dict[int, Storable] = {}

        for data in data_pool:
            structured_data: Dict[str, str] = data.get_metadata()
            matched: bool = True

            if condition is not None:
                for key, value in condition.items():
                    if key not in structured_data or structured_data[key] != value:
                        matched = False
                        break

            if matched or condition is None:
                search_results[index] = data

            index += 1

        return search_results
