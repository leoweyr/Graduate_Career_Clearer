from typing import List, Dict, Any

from data_model.DataModelable import DataModelable
from data_storage.Storable import Storable
from data_model.Course import Course
from data_model.DataIncompleteError import DataIncompleteError
from data_storage.DataNotIndexableError import DataNotIndexableError


class Major(DataModelable, Storable):
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

    def __str__(self) -> str:
        return self.__name

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

    def get_data(self) -> Dict[str: Any]:
        data_structure: Dict[str: Any] = {
            "id": self.__id,
            "name": self.__name,
            "edition": self.__edition,
            "standard_major_optional_credits": self.__standard_major_optional_credits,
            "standard_limited_elective_credits": self.__standard_limited_elective_credits,
            "standard_optional_credits": self.__standard_optional_credits,
            "standard_required_courses": self.__standard_required_courses
        }

        return data_structure

    def is_indexable(self) -> bool:
        if self.__id == 0:
            raise DataNotIndexableError(self, "id")
        elif self.__name == "":
            raise DataNotIndexableError(self, "name")
        elif self.__edition == 0:
            raise DataNotIndexableError(self, "edition")
        else:
            return True

    def get_metadata(self) -> Dict[str: str]:
        if self.is_indexable():
            metadata: Dict[str: str] = {
                "id": str(self.__id),
                "name": str(self.__name),
                "edition": str(self.__edition)
            }

            return metadata
