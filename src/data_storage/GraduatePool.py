from typing import Optional, Union, Dict, List
from types import TracebackType

from data_storage.Pool import Pool
from data_model.Graduate import Graduate
from data_storage.Databaseable import Databaseable
from data_storage.DataContainer import DataContainer
from data_storage.Storable import Storable


class GraduatePool(Pool[Graduate]):
    def __init__(self, database: Optional[Union[Databaseable, None]] = None):
        self.__graduates: DataContainer = DataContainer[Graduate]()
        self.__database: Optional[Union[Databaseable, None]] = None
        if database is not None:
            self.__database = database
            self.__database.set_data_container(self.__graduates)
            self.__database.pull()

    def __enter__(self) -> 'GraduatePool':
        if self.__database is not None:
            self.__database.pull()
        return self

    def __exit__(self,
                 exc_type: Optional['BaseException'],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None:
        if self.__database is not None:
            self.__database.push()

    def __str__(self) -> str:
        return "graduate pool"

    def add_data(self, data: Storable) -> None:
        if data.is_indexable() and len(self._find_data(self.__graduates, data.get_metadata())) == 0:
            self.__graduates.append(Graduate(data))

    def get_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> List[Graduate]:
        search_results: Dict[int, Graduate] = dict(self._find_data(self.__graduates, condition))
        data: List[Graduate] = list(search_results.values())

        return data

    def remove_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> None:
        search_results: Dict[int, Graduate] = dict(self._find_data(self.__graduates, condition))

        for index in search_results.keys():
            self.__graduates.pop(index)
