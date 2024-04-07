from typing import Union, Any, List, Dict

from data_model.DataModelable import DataModelable
from data_storage.Storable import Storable
from data_model.Course import Course
from data_model.TypeCastingError import TypeCastingError
from data_model.DataIncompleteError import DataIncompleteError
from data_storage.DataNotIndexableError import DataNotIndexableError
from pure_object_oriented.NoInheritMeta import NoInheritMeta


class Major(DataModelable, Storable):
    def __init__(self, builder: Union['Major.Builder', Any]):
        # Metadata.
        self.__id: int = 0
        self.__name: str = ""
        self.__edition: int = 0

        # Standard data.
        self.__standard_major_optional_credits: float = 0
        self.__standard_limited_elective_credits: float = 0
        self.__standard_optional_credits: float = 0
        self.__standard_required_courses: List[Course] = []

        if isinstance(builder, Major.Builder):
            self.__id = builder.outer_class_get_id()
            self.__name = builder.outer_class_get_name()
            self.__edition = builder.outer_class_get_edition()
        else:
            converted_object_members: List[str] = dir(builder)
            self_object_members: List[str] = ["_Major__id",
                                              "_Major__name",
                                              "_Major__edition",
                                              "_Major__standard_major_optional_credits",
                                              "_Major__standard_limited_elective_credits",
                                              "_Major__standard_optional_credits",
                                              "_Major__standard_required_courses"]

            if not set(self_object_members).issubset(set(converted_object_members)):
                raise TypeCastingError(builder, Major)
            else:
                self.__id = getattr(builder, "_Major__id")
                self.__name = getattr(builder, "_Major__name")
                self.__edition = getattr(builder, "_Major__edition")
                self.__standard_major_optional_credits = getattr(builder, "_Major__standard_major_optional_credits")
                self.__standard_limited_elective_credits = getattr(builder, "_Major__standard_limited_elective_credits")
                self.__standard_required_courses = getattr(builder, "_Major__standard_required_courses")

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

    def get_data(self) -> Dict[str, Any]:
        data_structure: Dict[str, Any] = {
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

    def get_metadata(self) -> Dict[str, str]:
        if self.is_indexable():
            metadata: Dict[str, str] = {
                "id": str(self.__id),
                "name": str(self.__name),
                "edition": str(self.__edition)
            }

            return metadata

    class Builder(metaclass=NoInheritMeta):
        def __init__(self):
            self.__id: int = 0
            self.__name: str = ""
            self.__edition: int = 0

        def id_(self, id_: int) -> 'Major.Builder':
            self.__id = id_
            return self

        def name(self, name: str) -> 'Major.Builder':
            self.__name = name
            return self

        def edition(self, edition: int) -> 'Major.Builder':
            self.__edition = edition
            return self

        def build(self) -> 'Major':
            return Major(self)

        def outer_class_get_id(self) -> int:
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

        def outer_class_get_edition(self) -> int:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__edition
