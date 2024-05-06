from typing import Optional, Union, Dict, List
from types import TracebackType

from data_storage.Pool import Pool
from data_model.Major import Major
from data_storage.Databaseable import Databaseable
from data_storage.DataContainer import DataContainer
from data_storage.Storable import Storable


class MajorPool(Pool[Major]):
    def __init__(self, database: Optional[Union[Databaseable, None]] = None):
        self.__majors: DataContainer = DataContainer[Major]()
        self.__database: Optional[Union[Databaseable, None]] = None
        if database is not None:
            self.__database = database
            self.__database.set_data_container(self.__majors)
            self.__database.pull()

    def __enter__(self) -> 'MajorPool':
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
        return "major pool"

    def add_data(self, data: Storable, force_replace: Optional[bool] = False) -> None:
        """
        Args:
            force_replace: Whether to forcefully replace existing objects in the data pool with the same metadata. Defaults to False.
        """
        if data.is_indexable():
            if len(self._find_data(self.__majors, data.get_metadata())) > 0:
                if not force_replace:
                    raise ValueError(f"Input object <{repr(Storable)}> conflicts with an existing object in the {self} "
                                     f"with the same metadata.")
                else:
                    self.remove_data(data.get_metadata())

            self.__majors.append(Major(data))

    def get_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> List[Major]:
        search_results: Dict[int, Major] = dict(self._find_data(self.__majors, condition))
        data: List[Major] = list(search_results.values())

        return data

    def remove_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> None:
        search_results: Dict[int, Major] = dict(self._find_data(self.__majors, condition))

        for index in search_results.keys():
            self.__majors.pop(index)
