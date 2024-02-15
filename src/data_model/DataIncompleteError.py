from typing import Any


class DataIncompleteError(Exception):
    def __init__(self, object_reference: Any, missingdata: str):
        super().__init__(str(object_reference) + " is missing data <" + missingdata + ">")
