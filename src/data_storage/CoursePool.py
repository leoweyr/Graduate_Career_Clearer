from typing import List, Dict

from data_storage.Pool import Pool
from data_model.Course import Course
from data_storage.Storable import Storable


class CoursePool(Pool):
    def __init__(self):
        self.__courses: List[Course] = []

    def add_data(self, data: Storable) -> None:
        if data.is_indexable() and len(self._find_data(self.__courses, data.get_metadata())) == 0:
            self.__courses.append(data)

    def get_data(self, condition: Dict[str, str] = None) -> List[Storable]:
        search_results: Dict[int, Storable] = dict(self._find_data(self.__courses, condition))

        return list(search_results.values())

    def remove_data(self, condition: Dict[str, str] = None) -> None:
        search_results: Dict[int, Storable] = dict(self._find_data(self.__courses, condition))

        for index in search_results.keys():
            self.__courses.pop(index)
