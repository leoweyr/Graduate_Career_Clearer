from abc import ABCMeta, abstractmethod

from data_model.DataModelable import DataModelable


class Evaluable(metaclass=ABCMeta):
    @abstractmethod
    def judge(self, target: DataModelable) -> bool:
        pass
