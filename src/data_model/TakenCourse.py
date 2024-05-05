from typing import Any, Dict, List

from data_model.DataModelable import DataModelable
from data_model.Course import Course
from criterion.PointCriterion import PointCriterion
from data_storage.CoursePool import CoursePool
from data_storage.ObjectNotFoundError import ObjectNotFoundError
from data_model.DataIncompleteError import DataIncompleteError


class TakenCourse(DataModelable):
    def __init__(self, course: Course, points: Any, point_criterion: PointCriterion):
        self.__course: Course = course
        self.__points: Any = points
        self.__points_criterion: PointCriterion = point_criterion

    def __getstate__(self) -> Dict[str, Any]:
        state: Dict[str, Any] = self.__dict__.copy()
        static_course: Dict[str, str] = self.__course.get_metadata()
        state["_TakenCourse__course"] = static_course

        return state

    def __setstate__(self, state: Dict[str, Any]) -> None:
        static_course: Dict[str, str] = state["_TakenCourse__course"]
        course_pool: CoursePool = CoursePool()
        courses: List[Course] = course_pool.get_data(static_course)

        if len(courses) == 0:
            raise ObjectNotFoundError(course_pool, static_course)
        elif len(courses) > 1:
            raise ValueError(f"The single static course data <{static_course}> stored in deserialized TakenCourse "
                             f"object does not correspond to the single Course object in the course pool.")
        else:
            state["_TakenCourse__course"] = courses[0]

        self.__dict__.update(state)

    def is_completed(self) -> bool:
        if self.__course.is_completed():
            if self.__points is None:
                raise DataIncompleteError(self, "points")
            else:
                return True

    def get_data(self) -> Dict[str, Any]:
        data_structure: Dict[str, Any] = {
            "course": self.__course,
            "points": self.__points
        }

        return data_structure

    def is_pass(self) -> bool:
        return self.__points_criterion.judge(self)
