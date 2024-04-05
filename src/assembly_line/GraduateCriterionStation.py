from typing import Union

from assembly_line.Executable import Executable
from criterion.Evaluable import Evaluable
from data_model.Graduate import Graduate


class GraduateCriterionStation(Executable):
    def __init__(self):
        self.__criterion: Union[Evaluable, None] = None
        self.__graduate: Union[Graduate, None] = None

    def execute(self) -> None:
        self.__criterion.evaluate(self.__graduate)
