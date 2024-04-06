import typing
from typing import TypeVar, Generic, List, Dict
import copy

from data_storage.Storable import Storable


DataContainerType: typing = TypeVar('DataContainerType', bound=Storable)


class DataContainer(Generic[DataContainerType]):
    def __init__(self):
        self.__container: List[DataContainerType] = []
        self.__metadata_tags: List[str] = []

    def clone(self) -> 'DataContainer[DataContainerType]':
        data_container_copy: DataContainer[DataContainerType] = copy.deepcopy(self)

        return data_container_copy

    def __iter__(self) -> iter:
        return iter(self.__container)

    def __len__(self) -> int:
        return len(self.__container)

    def append(self, data: DataContainerType) -> None:
        data_metadata: Dict[str, str] = data.get_metadata()
        if len(self.__metadata_tags) == 0:
            self.__metadata_tags = list(data_metadata.keys())
        else:
            if self.__metadata_tags != list(data_metadata.keys()):
                raise ValueError("The metadata of the data does not match the data container requirement.")
        self.__container.append(data)

    def pop(self, index: int) -> None:
        self.__container.pop(index)

    def get_metadata_tags(self) -> List[str]:
        if len(self.__metadata_tags) == 0:
            raise RuntimeError("Data container is not populated with any data yet.")
        return self.__metadata_tags

    def copy(self, data_container: 'DataContainer[DataContainerType]') -> None:
        if isinstance(data_container, DataContainer):
            self.__container = getattr(data_container, "_DataContainer__container")
            self.__metadata_tags = getattr(data_container, "_DataContainer__metadata_tags")
        else:
            raise TypeError("The input parameter is not a DataContainer object.")
