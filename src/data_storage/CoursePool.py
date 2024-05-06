from typing import Optional, Union, Dict, List
from types import TracebackType

from data_storage.Pool import Pool
from data_model.Course import Course
from data_storage.Databaseable import Databaseable
from data_storage.DataContainer import DataContainer
from data_storage.Storable import Storable


class CoursePool(Pool[Course]):
    def __init__(self, database: Optional[Union[Databaseable, None]] = None):
        self.__courses: DataContainer = DataContainer[Course]()
        self.__database: Optional[Union[Databaseable, None]] = None
        if database is not None:
            self.__database = database
            self.__database.set_data_container(self.__courses)
            self.__database.pull()

    def __enter__(self) -> 'CoursePool':
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
        return "course pool"

    def add_data(self, data: Storable, force_replace: Optional[bool] = False) -> None:
        """
        Args:
            force_replace: Whether to forcefully replace existing objects in the data pool with the same metadata. Defaults to False.
        """
        if data.is_indexable():
            if len(self._find_data(self.__courses, data.get_metadata())) > 0:
                if not force_replace:
                    raise ValueError(f"Input object <{repr(Storable)}> conflicts with an existing object in the {self} "
                                     f"with the same metadata.")
                else:
                    self.remove_data(data.get_metadata())

            self.__courses.append(Course(data))

    def get_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> List[Course]:
        search_results: Dict[int, Course] = dict(self._find_data(self.__courses, condition))
        data: List[Course] = list(search_results.values())

        return data

    def remove_data(self, condition: Optional[Union[Dict[str, str], None]] = None) -> None:
        search_results: Dict[int, Course] = dict(self._find_data(self.__courses, condition))

        for index in search_results.keys():
            self.__courses.pop(index)
