from typing import Dict

from data_storage.Pool import Pool


class ObjectNotFoundError(Exception):
    def __init__(self, pool: Pool, object_metadata: Dict[str, str]):
        self.__pool: Pool = pool
        self.__object_metadata: Dict[str, str] = object_metadata
        super().__init__(f"Object with metadata <{self.__object_metadata}> not found in {self.__pool}.")
