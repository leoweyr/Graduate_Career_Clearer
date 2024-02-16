from typing import List, Dict, Any

from data_storage.Pool import Pool
from data_model.Major import Major
from data_model.DataModelable import DataModelable


class MajorPool(Pool):
    def __init__(self):
        self.__majors: List[Major] = []

    def add_data(self, data: DataModelable) -> None:
        self.__majors.append(data)

    def get_data(self, condition: Dict[str, Any] = None) -> List[DataModelable]:
        search_results: Dict[int, DataModelable] = dict(self._find_data(self.__majors, condition))

        return list(search_results.values())

    def remove_data(self, condition: Dict[str, Any] = None) -> None:
        search_results: Dict[int, DataModelable] = dict(self._find_data(self.__majors, condition))

        for index in search_results.keys():
            self.__majors.pop(index)
