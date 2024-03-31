class TypeCastingError(Exception):
    def __init__(self, source_object: object, target_type: type):
        self.__source_object: object = source_object
        self.__target_type: type = target_type
        super().__init__(f"Object {repr(self.__source_object)} of type {type(self.__source_object)} cannot be cast to "
                         f"type {self.__target_type}")
