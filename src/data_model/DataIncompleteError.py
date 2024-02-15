from typing import Any


class DataIncompleteError(Exception):
    def __init__(self, object_reference: Any, missing_data: str):
        super().__init__(str(object_reference) + " is missing data <" + missing_data + ">")
