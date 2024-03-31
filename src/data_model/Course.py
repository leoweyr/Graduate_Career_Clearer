from typing import Dict, Any

from src.data_model.DataModelable import DataModelable
from data_storage.Storable import Storable
from src.data_model.CourseNature import CourseNature
from src.data_model.DataIncompleteError import DataIncompleteError
from data_storage.DataNotIndexableError import DataNotIndexableError
from pure_object_oriented.NoInheritMeta import NoInheritMeta


class Course(DataModelable, Storable):
    def __init__(self, builder: 'Course.Builder'):
        self.__id: str = builder.outer_class_get_id()
        self.__name: str = builder.outer_class_get_name()
        self.__nature: CourseNature = builder.outer_class_get_nature()
        self.__supplier: str = builder.outer_class_get_supplier()

    def is_completed(self) -> bool:
        if self.__id == "":
            raise DataIncompleteError(self, "id")
        elif self.__name == "":
            raise DataIncompleteError(self, "name")
        elif self.__nature == CourseNature.UNKNOW:
            raise DataIncompleteError(self, "nature")
        elif self.__supplier == "":
            raise DataIncompleteError(self, "supplier")
        else:
            return True

    def get_data(self) -> Dict[str, Any]:
        data_structure: Dict[str, Any] = {
            "id": self.__id,
            "name": self.__name,
            "nature": self.__nature,
            "supplier": self.__supplier
        }

        return data_structure

    def is_indexable(self) -> bool:
        if self.__id == "":
            raise DataNotIndexableError(self, "id")
        elif self.__name == "":
            raise DataNotIndexableError(self, "name")
        elif self.__nature == CourseNature.UNKNOW:
            raise DataNotIndexableError(self, "nature")
        elif self.__supplier == "":
            raise DataNotIndexableError(self, "supplier")
        else:
            return True

    def get_metadata(self) -> Dict[str, str]:
        if self.is_indexable():
            metadata: Dict[str, str] = {
                "id": str(self.__id),
                "name": str(self.__name),
                "nature": str(self.__nature),
                "supplier": str(self.__supplier)
            }

            return metadata

    class Builder(metaclass=NoInheritMeta):
        def __init__(self):
            self.__id: str = ""
            self.__name: str = ""
            self.__nature: CourseNature = CourseNature.UNKNOW
            self.__supplier: str = ""

        def id(self, id: str) -> 'Course.Builder':
            self.__id = id
            return self

        def name(self, name: str) -> 'Course.Builder':
            self.__name = name
            return self

        def nature(self, nature: CourseNature) -> 'Course.Builder':
            self.__nature = nature
            return self

        def supplier(self, supplier: str) -> 'Course.Builder':
            self.__supplier = supplier
            return self

        def build(self) -> 'Course':
            return Course(self)

        def outer_class_get_id(self) -> str:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__id

        def outer_class_get_name(self) -> str:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__name

        def outer_class_get_nature(self) -> CourseNature:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__nature

        def outer_class_get_supplier(self) -> str:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__supplier
