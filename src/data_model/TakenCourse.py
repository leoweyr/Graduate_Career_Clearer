from typing import Any, Dict

from data_model.DataModelable import DataModelable
from data_model.Course import Course
from criterion.PointCriterion import PointCriterion
from data_model.TakenCourseStatus import TakenCourseStatus
from data_model.DataIncompleteError import DataIncompleteError


class TakenCourse(DataModelable):
    def __init__(self, course: Course, points: Any, point_criterion: PointCriterion):
        self.__course: Course = course
        self.__status: TakenCourseStatus = TakenCourseStatus.UNKNOWN
        self.__points: Any = points
        self.__points_criterion: PointCriterion = point_criterion

    def is_completed(self) -> bool:
        if self.__course.is_completed():
            if self.__status == TakenCourseStatus.UNKNOWN:
                raise DataIncompleteError(self, "status")
            elif self.__points is None:
                raise DataIncompleteError(self, "points")
            else:
                return True

    def get_data(self) -> Dict[str, Any]:
        data_structure: Dict[str, Any] = {
            "course": self.__course,
            "status": self.__status,
            "points": self.__points
        }

        return data_structure

    def is_pass(self) -> bool:
        if self.__status == TakenCourseStatus.UNKNOWN:
            self.__points_criterion.evaluate(self)
        if self.__status == TakenCourseStatus.PASSED:
            return True
        else:
            return False

    @property
    def status(self) -> TakenCourseStatus:
        return self.__status

    @status.setter
    def status(self, status: TakenCourseStatus) -> None:
        self.__status = status
