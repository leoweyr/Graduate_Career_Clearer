from typing import List

from data_model.DataModelable import DataModelable
from data_model.Course import Course
from data_model.DataIncompleteError import DataIncompleteError


class Major(DataModelable):
    def __init__(self):
        # Metadata.
        self.__id: int = 0
        self.__name: str = ""
        self.__edition: int = 0

        # Standard data.
        self.__standard_major_optional_credits: float = 0
        self.__standard_limited_elective_credits: float = 0
        self.__standard_optional_credits: float = 0
        self.__standard_required_courses: List[Course] = []

    def is_completed(self) -> bool:
        if self.__id == 0:
            raise DataIncompleteError(self, "id")
        elif self.__name == "":
            raise DataIncompleteError(self, "name")
        elif self.__edition == 0:
            raise DataIncompleteError(self, "edition")
        elif self.__standard_major_optional_credits == 0:
            raise DataIncompleteError(self, "standard major optional credits")
        elif self.__standard_limited_elective_credits == 0:
            raise DataIncompleteError(self, "standard limited elective credits")
        elif self.__standard_optional_credits == 0:
            raise DataIncompleteError(self, "standard optional credits")
        elif len(self.__standard_required_courses) == 0:
            raise DataIncompleteError(self, "standard required courses")
        else:
            return True
