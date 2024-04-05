from data_model.DataModelable import DataModelable


class DataIncompleteError(Exception):
    def __init__(self, data_modelable_object: DataModelable, missing_data: str):
        self.__data_modelable_object: DataModelable = data_modelable_object
        self.__missing_data: str = missing_data
        super().__init__(f"{repr(self.__data_modelable_object)} is missing data <{self.__missing_data}>.")
