class DataIncompleteError(Exception):
    def __init__(self, object: object, missingdata: str):
        super().__init__(str(object) + " is missing data <" + missingdata + ">")