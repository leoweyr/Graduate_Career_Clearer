from data_storage.Storable import Storable


class DataNotIndexableError(Exception):
    def __init__(self, storable_object: Storable, missing_metadata: str):
        self.__storable_object: Storable = storable_object
        self.__missing_metadata: str = missing_metadata
        super().__init__(f"{repr(self.__storable_object)} is missing metadata <{self.__missing_metadata}>.")
