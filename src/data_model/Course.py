from functools import singledispatchmethod
from typing import Dict, Any, List

from pure_object_oriented.NoInheritMeta import NoInheritMeta
from src.data_model.CourseNature import CourseNature
from src.data_model.DataModelable import DataModelable
from data_model.TypeCastingError import TypeCastingError
from data_storage.Storable import Storable
from src.data_model.DataIncompleteError import DataIncompleteError
from data_storage.DataNotIndexableError import DataNotIndexableError


class CourseBuilder(metaclass=NoInheritMeta):
    """
    This class was originally intended to be an inner class of Course, but due to the mechanisms of `register`
    decorators in Python, it had to be moved as an external class.
    """
    def __init__(self):
        self.__id: str = ""
        self.__name: str = ""
        self.__nature: CourseNature = CourseNature.UNKNOW
        self.__supplier: str = ""

    def id(self, id: str) -> 'CourseBuilder':
        self.__id = id
        return self

    def name(self, name: str) -> 'CourseBuilder':
        self.__name = name
        return self

    def nature(self, nature: CourseNature) -> 'CourseBuilder':
        self.__nature = nature
        return self

    def supplier(self, supplier: str) -> 'CourseBuilder':
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


class Course(DataModelable, Storable):
    @singledispatchmethod
    def __init__(self, *args):
        raise NotImplementedError("Unsupported method")

    @__init__.register(CourseBuilder)
    def _(self, builder: CourseBuilder):
        self.__id: str = builder.outer_class_get_id()
        self.__name: str = builder.outer_class_get_name()
        self.__nature: CourseNature = builder.outer_class_get_nature()
        self.__supplier: str = builder.outer_class_get_supplier()

    @__init__.register(DataModelable)
    def _(self, converted_object: DataModelable):
        converted_object_data: Dict[str, Any] = converted_object.get_data()
        converted_object_data_keys: List[str] = list(converted_object_data.keys())
        this_object_data_keys: List[str] = ["id", "name", "nature", "supplier"]

        if converted_object_data_keys != this_object_data_keys:
            raise TypeCastingError(converted_object, Course)
        else:
            self.__id: str = converted_object_data["id"]
            self.__name: str = converted_object_data["name"]
            self.__nature: CourseNature = converted_object_data["nature"]
            self.__supplier: str = converted_object_data["supplier"]

    @__init__.register(Storable)
    def _(self, converted_object: Storable):
        converted_object_data_keys: List[str] = dir(converted_object)
        this_object_data_keys: List[str] = ["_Course__id", "_Course__name", "_Course__nature", "_Course__supplier"]

        if not set(this_object_data_keys).issubset(set(converted_object_data_keys)):
            raise TypeCastingError(converted_object, Course)
        else:
            self.__id: str = getattr(converted_object, "_Course__id")
            self.__name: str = getattr(converted_object, "_Course__name")
            self.__nature: CourseNature = getattr(converted_object, "_Course__nature")
            self.__supplier: str = getattr(converted_object, "_Course__supplier")

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
