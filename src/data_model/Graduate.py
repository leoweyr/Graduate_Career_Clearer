from typing import List, Dict

from data_model.DataModelable import DataModelable
from data_model.DataIncompleteError import DataIncompleteError
from data_model.Gender import Gender
from data_model.Major import Major
from data_model.TakenCourse import TakenCourse


class Graduate(DataModelable):
    def __init__(self):
        # Basic student information.
        self.__id: int = 0
        self.__name: str = ""
        self.__gender: Gender = Gender.UNKNOWN
        self.__grade: int = 0
        self.__class: str = ""
        self.__college: str = ""
        self.__major: Major = None

        # Graduate career information
        self.__gpa: float = 0
        self.__required_credits: float = 0
        self.__major_optional_credits: float = 0
        self.__limited_elective_credits: float = 0
        self.__optional_credits: float = 0
        self.__courses: List[TakenCourse] = []

    def is_completed(self) -> bool:
        if self.__id == 0:
            raise DataIncompleteError(self, "id")
        elif self.__name == "":
            raise DataIncompleteError(self, "name")
        elif self.__gender == Gender.UNKNOWN:
            raise DataIncompleteError(self, "gender")
        elif self.__grade == 0:
            raise DataIncompleteError(self, "grade")
        elif self.__class == "":
            raise DataIncompleteError(self, "class")
        elif self.__college == "":
            raise DataIncompleteError(self, "college")
        elif self.__major == "":
            raise DataIncompleteError(self, "major")
        elif self.__gpa == 0:
            raise DataIncompleteError(self, "gpa")
        elif self.__required_credits == 0:
            raise DataIncompleteError(self, "required_credits")
        elif self.__major_optional_credits == 0:
            raise DataIncompleteError(self, "major_optional_credits")
        elif self.__limited_elective_credits == 0:
            raise DataIncompleteError(self, "limited_elective_credits")
        elif self.__optional_credits == 0:
            raise DataIncompleteError(self, "optional_credits")
        elif len(self.__courses) == 0:
            raise DataIncompleteError(self, "courses")
        else:
            return True

    def get_data(self) -> Dict[str: object]:
        data_structure: Dict[str: object] = {
            "id": self.__id,
            "name": self.__name,
            "gender": self.__gender,
            "class": self.__class,
            "college": self.__college,
            "major": self.__major,
            "gpa": self.__gpa,
            "required_credits": self.__required_credits,
            "major_optional_credits": self.__major_optional_credits,
            "limited_elective_credits": self.__limited_elective_credits,
            "optional_credits": self.__optional_credits,
            "courses": self.__courses
        }

        return data_structure
