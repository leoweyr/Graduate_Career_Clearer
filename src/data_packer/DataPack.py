from typing import Optional, Union, Any

from data_packer.DataTag import DataTag
from data_packer.DataType import DataType


class DataPack:
    def __init__(self, tag: DataTag, used_tag_name: Optional[Union[str, None]] = None, content: Optional[Any] = None):
        self.__tag: DataTag = tag
        self._used_tag_name_backup: Union[str, None] = None
        self.__used_tag_name_reference: Union[int, None] = None
        self.__content: Any = None

        if used_tag_name in self.__tag.names:
            self.__used_tag_name_reference = self.__tag.names.index(used_tag_name)
            self._used_tag_name_backup = used_tag_name

        if content is not None:
            if self.__tag.type == DataType.INTEGER:
                self.__content = int(content)
            elif self.__tag.type == DataType.FLOAT:
                self.__content = float(content)
            elif self.__tag.type == DataType.STRING:
                self.__content = str(content)

    @property
    def tag(self) -> DataTag:
        return self.__tag

    @property
    def used_tag_name(self) -> Union[str, None]:
        """
        Reference the name used in names member of DataTag in case it is renaming rather than being stored statically
        in the member of DataPack.
        """
        if self.__used_tag_name_reference is not None and self.__used_tag_name_reference + 1 <= len(self.__tag.names):
            used_tag_name: str = self.__tag.names[self.__used_tag_name_reference]
            self._used_tag_name_backup = used_tag_name
            return used_tag_name
        else:
            return self._used_tag_name_backup

    @property
    def content(self) -> Union[int, float, str]:
        return self.__content
