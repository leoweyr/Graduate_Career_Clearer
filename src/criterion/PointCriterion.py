from typing import Dict, Any

from criterion import Evaluable
from data_model.TakenCourse import TakenCourse
from data_model.TakenCourseStatus import TakenCourseStatus


class PointCriterion(Evaluable):
    def _judge(self, target: TakenCourse) -> Dict[str, Any]:
        """
        According to the principle of strict control, priority is given to judging the passing situation to avoid
        misjudgment as failing due to errors in the original data format.
        """
        if isinstance(target.points, float):
            if float(target.points) >= 60:
                return dict({"target": target, "is_pass": True})
        elif isinstance(target.points, str):
            if str(target.points) == "及格":
                return dict({"target": target, "is_pass": True})
            elif str(target.points) == "良好":
                return dict({"target": target, "is_pass": True})
            elif str(target.points) == "优秀":
                return dict({"target": target, "is_pass": True})
            elif str(target.points) == "中等":
                return dict({"target": target, "is_pass": True})
        return dict({"target": target, "is_pass": False})

    def _conclude(self, result: Dict[str, Any]) -> None:
        evaluated_target: TakenCourse = result["target"]
        if bool(result["is_pass"]):
            evaluated_target.status = TakenCourseStatus.PASSED
        else:
            evaluated_target.status = TakenCourseStatus.FAILED
