from typing import Any

from criterion import Evaluable
from data_model.DataModelable import DataModelable


class PointCriterion(Evaluable):
    def judge(self, target: DataModelable) -> bool:
        """
        According to the principle of strict control, priority is given to judging the passing situation to avoid
        misjudgment as failing due to errors in the original data format.
        """
        if target.is_completed():
            target_points: Any = target.get_data()["points"]

            try:
                float(target_points)
            except ValueError:
                if str(target_points) == "及格":
                    return True
                elif str(target_points) == "良好":
                    return True
                elif str(target_points) == "优秀":
                    return True
                elif str(target_points) == "中等":
                    return True
            else:
                if float(target_points) >= 60:
                    return True
            finally:
                return False
