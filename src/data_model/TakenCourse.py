from typing import Dict, Any

from src.data_model.Course import Course
from src.criterion.PointCriterion import PointCriterion
from src.data_model.TakenCourseStatus import TakenCourseStatus
from src.data_model.DataIncompleteError import DataIncompleteError


class TakenCourse(Course):
    def __init__(self, point_criterion: PointCriterion):
        super().__init__()
        self.__status: TakenCourseStatus = TakenCourseStatus.UNKNOWN
        self.__points: Any = None
        self.__points_criterion: PointCriterion = point_criterion

    def is_complete(self) -> bool:
        if self.__points is None:
            raise DataIncompleteError(self, "points")
        elif super().is_completed():
            return True

    def get_data(self) -> Dict[str: Any]:
        data_structure: Dict[str: Any] = {
            "points": self.__points
        }

        data_structure.update(super().get_data())

        return data_structure

    def is_pass(self) -> bool:
        if self.__points == TakenCourseStatus.UNKNOWN:
            if self.is_complete():
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

    @property
    def points(self) -> Any:
        return self.__points
