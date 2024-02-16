from typing import List, Dict, Any

from data_storage.Pool import Pool
from data_model.Course import Course
from data_model.DataModelable import DataModelable


class CoursePool(Pool):
    def __init__(self):
        self.__courses: List[Course] = []

    def add_data(self, data: DataModelable) -> None:
        self.__courses.append(data)

    def get_data(self, condition: Dict[str, Any] = None) -> List[DataModelable]:
        search_results: Dict[int, DataModelable] = dict(self._find_data(self.__courses, condition))

        return list(search_results.values())

    def remove_data(self, condition: Dict[str, Any] = None) -> None:
        search_results: Dict[int, DataModelable] = dict(self._find_data(self.__courses, condition))

        for index in search_results.keys():
            self.__courses.pop(index)
