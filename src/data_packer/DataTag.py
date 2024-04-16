from typing import List

from data_packer import DataType


class DataTag:
    def __init__(self, names: List[str], type_: DataType):
        self.__names: List[str] = names
        self.__type: DataType = type_

    @property
    def names(self) -> List[str]:
        return self.__names

    @property
    def type(self) -> DataType:
        return self.__type
