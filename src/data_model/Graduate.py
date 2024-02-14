from src.data_model.DataModelable import DataModelable
from src.data_model.DataIncompleteError import DataIncompleteError
from src.data_model.Gender import Gender
from src.data_model.Course import Course


class Graduate(DataModelable):
    def __init__(self):
        # Basic student information.
        self.__id: int = 0
        self.__name: str = ""
        self.__gender: Gender = Gender.UNKNOWN
        self.__grade: int = 0
        self.__class: str = ""
        self.__college: str = ""
        self.__major: str = ""

        # Graduate career information
        self.__gpa: float = 0
        self.__required_credits: float = 0
        self.__major_optional_credits: float = 0
        self.__limited_elective_credits: float = 0
        self.__optional_credits: float = 0
        self.__courses: list[Course] = []

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
