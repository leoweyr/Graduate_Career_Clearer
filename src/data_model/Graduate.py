from typing import Union, Any, List, Dict, Optional

from data_model.DataModelable import DataModelable
from data_storage.Storable import Storable
from data_model.Gender import Gender
from data_model.Major import Major
from data_model.TakenCourse import TakenCourse
from data_model.TypeCastingError import TypeCastingError
from data_model.DataIncompleteError import DataIncompleteError
from data_storage.DataNotIndexableError import DataNotIndexableError
from criterion.PointCriterion import PointCriterion
from data_storage.CoursePool import CoursePool
from data_model.Course import Course
from data_storage.ObjectNotFoundError import ObjectNotFoundError
from pure_object_oriented.NoInheritMeta import NoInheritMeta


class Graduate(DataModelable, Storable):
    def __init__(self, builder: Union['Graduate.Builder', Any]):
        # Basic student information.
        self.__id: int = 0
        self.__name: str = ""
        self.__gender: Gender = Gender.UNKNOWN
        self.__grade: int = 0
        self.__class: str = ""
        self.__college: str = ""
        self.__major: Union[Major, None] = None

        # Graduate career information
        self.__gpa: float = 0
        self.__required_credits: float = 0
        self.__major_optional_credits: float = 0
        self.__limited_elective_credits: float = 0
        self.__optional_credits: float = 0
        self.__taken_courses: List[TakenCourse] = []

        if isinstance(builder, Graduate.Builder):
            self.__id = builder.outer_class_get_id()
            self.__name = builder.outer_class_get_name()
            self.__gender = builder.outer_class_get_gender()
            self.__grade = builder.outer_class_get_grade()
            self.__class = builder.outer_class_get_class()
            self.__college = builder.outer_class_get_college()
            self.__major = builder.outer_class_get_major()
        else:
            converted_object_members: List[str] = dir(builder)
            self_object_members: List[str] = ["_Graduate__id",
                                              "_Graduate__name",
                                              "_Graduate__gender",
                                              "_Graduate__grade",
                                              "_Graduate__class",
                                              "_Graduate__college",
                                              "_Graduate__major",
                                              "_Graduate__gpa",
                                              "_Graduate__required_credits",
                                              "_Graduate__major_optional_credits",
                                              "_Graduate__limited_elective_credits",
                                              "_Graduate__optional_credits",
                                              "_Graduate__taken_courses"]

            if not set(self_object_members).issubset(set(converted_object_members)):
                raise TypeCastingError(builder, Graduate)
            else:
                self.__id = getattr(builder, "_Graduate__id")
                self.__name = getattr(builder, "_Graduate__name")
                self.__gender = getattr(builder, "_Graduate__gender")
                self.__grade = getattr(builder, "_Graduate__grade")
                self.__class = getattr(builder, "_Graduate__class")
                self.__college = getattr(builder, "_Graduate__college")
                self.__major = getattr(builder, "_Graduate__major")
                self.__gpa = getattr(builder, "_Graduate__gpa")
                self.__required_credits = getattr(builder, "_Graduate__required_credits")
                self.__major_optional_credits = getattr(builder, "_Graduate__major_optional_credits")
                self.__limited_elective_credits = getattr(builder, "_Graduate__limited_elective_credits")
                self.__optional_credits = getattr(builder, "_Graduate__optional_credits")
                self.__taken_courses = getattr(builder, "_Graduate__taken_courses")

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
        elif len(self.__taken_courses) == 0:
            raise DataIncompleteError(self, "taken_courses")
        else:
            return True

    def get_data(self) -> Dict[str, Any]:
        data_structure: Dict[str, Any] = {
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
            "taken_courses": self.__taken_courses
        }

        return data_structure

    def is_indexable(self) -> bool:
        if self.__id == 0:
            raise DataNotIndexableError(self, "id")
        elif self.__name == "":
            raise DataNotIndexableError(self, "name")
        elif self.__gender == Gender.UNKNOWN:
            raise DataNotIndexableError(self, "gender")
        elif self.__grade == 0:
            raise DataNotIndexableError(self, "grade")
        elif self.__class == "":
            raise DataNotIndexableError(self, "class")
        elif self.__college == "":
            raise DataNotIndexableError(self, "college")
        elif self.__major is None:
            raise DataNotIndexableError(self, "major")
        else:
            return True

    def get_metadata(self) -> Dict[str, str]:
        if self.is_indexable():
            metadata: Dict[str, str] = {
                "id": str(self.__id),
                "name": str(self.__name),
                "gender": str(self.__gender),
                "grade": str(self.__grade),
                "class": str(self.__class),
                "college": str(self.__college),
                "major": str(self.__major)
            }

            return metadata

    def set_gpa(self, gpa: float) -> None:
        self.__gpa = gpa

    def set_required_credits(self, required_credits: float) -> None:
        self.__required_credits = required_credits

    def set_major_optional_credits(self, major_optional_credits: float) -> None:
        self.__major_optional_credits = major_optional_credits

    def set_limited_elective_credits(self, limited_elective_credits: float) -> None:
        self.__limited_elective_credits = limited_elective_credits

    def set_optional_credits(self, optional_credits: float) -> None:
        self.__optional_credits = optional_credits

    def add_taken_courses(self, course_metadata: Dict[str, str], points: Any, point_criterion: PointCriterion) -> None:
        course_pool: CoursePool = CoursePool()
        courses: List[Course] = course_pool.get_data(course_metadata)

        if len(courses) == 0:
            raise ObjectNotFoundError(course_pool, course_metadata)
        elif len(courses) > 1:
            ValueError(f"Input course_metadata <{course_metadata}> does not uniquely correspond to the single Course "
                       f"object.")
        else:
            self.__taken_courses.append(TakenCourse(courses[0], points, point_criterion))

    def remove_taken_courses(self, condition: Optional[Union[Dict[str, str], None]] = None) -> None:
        index: int = 0
        removed_indices: List[int] = []

        for taken_course in self.__taken_courses:
            course_metadata: Dict[str, str] = taken_course.get_data()["course"].get_metadata()
            matched: bool = True

            if condition is not None:
                for key, value in condition.items():
                    if key not in course_metadata or course_metadata[key] != value:
                        matched = False
                        break

            if matched or condition is None:
                removed_indices.append(index)

            index += 1

        for index in removed_indices:
            self.__taken_courses.pop(index)

    class Builder(metaclass=NoInheritMeta):
        def __init__(self):
            self.__id: int = 0
            self.__name: str = ""
            self.__gender: Gender = Gender.UNKNOWN
            self.__grade: int = 0
            self.__class: str = ""
            self.__college: str = ""
            self.__major: Union[Major, None] = None

        def id_(self, id_: int) -> None:
            self.__id = id_

        def name(self, name: str) -> None:
            self.__name = name

        def gender(self, gender: Gender) -> None:
            self.__gender = gender

        def grade(self, grade: int) -> None:
            self.__grade = grade

        def class_(self, class_: str) -> None:
            self.__class = class_

        def college(self, college: str) -> None:
            self.__college = college

        def major(self, major: Major) -> None:
            self.__major = major

        def build(self) -> 'Graduate':
            return Graduate(self)

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

        def outer_class_get_gender(self) -> Gender:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__gender

        def outer_class_get_grade(self) -> int:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__grade

        def outer_class_get_class(self) -> str:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__class

        def outer_class_get_college(self) -> str:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__college

        def outer_class_get_major(self) -> Union[Major, None]:
            """
            Due to Python's lack of support for outer class accessing private members of inner class, this method is
            specifically designed to address this issue. Furthermore, it cannot be invoked externally.
            """
            return self.__major
