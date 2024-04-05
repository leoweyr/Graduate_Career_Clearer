from typing import Optional, Union, Dict, List
from types import TracebackType

from data_storage.Pool import Pool
from data_storage.Databaseable import Databaseable
from data_storage.DataContainer import DataContainer
from data_storage.Storable import Storable
from data_model.Course import Course


class CoursePool(Pool):
    def __init__(self, database: Databaseable):
        self.__database: Databaseable = database
        self.__courses: DataContainer = database.pull()

    def __enter__(self) -> 'CoursePool':
        return self

    def __exit__(self,
                 exc_type: Optional['BaseException'],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None:
        self.__database.push(self.__courses)

    def __str__(self) -> str:
        return "course pool"

    def add_data(self, data: Storable) -> None:
        if data.is_indexable() and len(self._find_data(self.__courses, data.get_metadata())) == 0:
            self.__courses.append(data)

    def get_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> List[Course]:
        search_results: Dict[int, Storable] = dict(self._find_data(self.__courses, condition))
        data: List[Course] = []

        for search_result_data in search_results.values():
            data.append(Course(search_result_data))

        return data

    def remove_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> None:
        search_results: Dict[int, Storable] = dict(self._find_data(self.__courses, condition))

        for index in search_results.keys():
            self.__courses.pop(index)
