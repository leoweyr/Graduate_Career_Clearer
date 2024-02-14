from src.criterion import Evaluable
from src.data_model.TakenCourse import TakenCourse
from src.data_model.TakenCourseStatus import TakenCourseStatus


class PointCriterion(Evaluable):
    def _judge(self, takenCourse: TakenCourse) -> dict[str: object]:
        """
        According to the principle of strict control, priority is given to judging the passing situation to avoid
        misjudgment as failing due to errors in the original data format.
        """
        if isinstance(takenCourse.points, float):
            if float(takenCourse.points) >= 60:
                return dict({"object": takenCourse, "is_pass": True})
        elif isinstance(takenCourse.points, str):
            if str(takenCourse.points) == "及格":
                return dict({"object": takenCourse, "is_pass": True})
            elif str(takenCourse.points) == "良好":
                return dict({"object": takenCourse, "is_pass": True})
            elif str(takenCourse.points) == "优秀":
                return dict({"object": takenCourse, "is_pass": True})
            elif str(takenCourse.points) == "中等":
                return dict({"object": takenCourse, "is_pass": True})
        return dict({"object": takenCourse, "is_pass": False})

    def _conclude(self, result: dict[str: object]) -> None:
        evaluated_object = result["object"]
        if bool(result["is_pass"]):
            evaluated_object.status = TakenCourseStatus.PASSED
        else:
            evaluated_object.status = TakenCourseStatus.FAILED
