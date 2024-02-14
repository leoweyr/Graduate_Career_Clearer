from src.data_model.Course import Course
from src.criterion.PointCriterion import PointCriterion
from src.data_model.TakenCourseStatus import TakenCourseStatus
from src.data_model.DataIncompleteError import DataIncompleteError


class TakenCourse(Course):
    def __init__(self, point_criterion: PointCriterion):
        super().__init__()
        self.__status: TakenCourseStatus = TakenCourseStatus.UNKNOWN
        self.__points: object = None
        self.__points_criterion: PointCriterion = point_criterion

    def is_complete(self) -> bool:
        if self.__points is None:
            raise DataIncompleteError(self, "points")
        elif super().is_completed():
            return True

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
    def status(self, status: TakenCourseStatus):
        self.__status = status

    @property
    def points(self) -> object:
        return self.__points
