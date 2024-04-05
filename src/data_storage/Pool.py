import typing
from typing import TypeVar, Generic, Optional, Union, Dict, List
from abc import abstractmethod

from data_storage.Storable import Storable
from pure_object_oriented.ABCAndSingletonMeta import ABCAndSingletonMeta
from data_storage.DataContainer import DataContainer


PoolType: typing = TypeVar('PoolType', bound=Storable)


class Pool(Generic[PoolType], metaclass=ABCAndSingletonMeta):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def add_data(self, data: Storable) -> None:
        pass

    @abstractmethod
    def get_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> List[Storable]:
        pass

    @abstractmethod
    def remove_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> None:
        pass

    def _find_data(self, data_pool: DataContainer, condition: Dict[str, str]) -> Dict[int, PoolType]:
        index: int = 0
        search_results: Dict[int, PoolType] = {}

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
