from typing import Dict, Any

from src.data_model.DataModelable import DataModelable
from data_storage.Storable import Storable
from src.data_model.CourseNature import CourseNature
from src.data_model.DataIncompleteError import DataIncompleteError
from data_storage.DataNotIndexableError import DataNotIndexableError


class Course(DataModelable, Storable):
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

    def get_data(self) -> Dict[str: Any]:
        data_structure: Dict[str: Any] = {
            "id": self._id,
            "name": self._name,
            "nature": self._nature,
            "supplier": self._supplier
        }

        return data_structure

    def is_indexable(self) -> bool:
        if self._id == "":
            raise DataNotIndexableError(self, "id")
        elif self._name == "":
            raise DataNotIndexableError(self, "name")
        elif self._nature == CourseNature.UNKNOW:
            raise DataNotIndexableError(self, "nature")
        elif self._supplier == "":
            raise DataNotIndexableError(self, "supplier")
        else:
            return True

    def get_metadata(self) -> Dict[str: str]:
        if self.is_indexable():
            metadata: Dict[str: str] = {
                "id": str(self._id),
                "name": str(self._name),
                "nature": str(self._nature),
                "supplier": str(self._supplier)
            }

            return metadata
