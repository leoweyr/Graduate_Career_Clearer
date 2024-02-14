from assembly_line.Executable import Executable
from criterion.Evaluable import Evaluable
from data_model.Graduate import Graduate


class GraduateCriterionSation(Executable):
    def __init__(self):
        self.__criterion: Evaluable = None
        self.__graduate: Graduate = None

    def execute(self) -> None:
        self.__criterion.evaluate(self.__graduate)
