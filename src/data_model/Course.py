from src.data_model.DataIncompleteError import DataIncompleteError
from src.data_model.DataModelable import DataModelable
from src.data_model.CourseNature import CourseNature


class Course(DataModelable):
    def __init__(self):
        self._id: str = ""
        self._name: str = ""
        self._nature: CourseNature = CourseNature.UNKNOW
        self._supplier: str = ""

    def is_completed(self) -> bool:
        if self._id == "":
            raise DataIncompleteError(self, "id")
        elif self._name == "":
            raise DataIncompleteError(self, "name")
        elif self._nature == CourseNature.UNKNOW:
            raise DataIncompleteError(self, "nature")
        elif self._supplier == "":
            raise DataIncompleteError(self, "supplier")
        else:
            return True
