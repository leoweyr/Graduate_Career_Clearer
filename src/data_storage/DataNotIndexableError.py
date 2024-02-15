from typing import Any


class DataNotIndexableError(Exception):
    def __init__(self, object_reference: Any, missing_metadata: str):
        super().__init__(str(object_reference) + " is missing metadata <" + missing_metadata + ">")
