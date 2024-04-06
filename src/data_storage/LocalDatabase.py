import os.path
from typing import Union, List
import pickle
from datetime import datetime

from data_storage.Databaseable import Databaseable
from data_storage.DataContainer import DataContainer


class LocalDatabase(Databaseable):
    def __init__(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"The path <{path}> does not exist.")
        elif not os.path.isdir(path):
            raise NotADirectoryError(f"The path <{path} is not a directory.")

        self.__path: str = path
        self.__data_container: Union[DataContainer, None] = None

        # Initialize or retrieve metadata tags if it already exists.
        self.__metadata_tags: List[str] = []
        metadata_tags_file_path: str = os.path.join(self.__path, ".metadata_tags")

        if len(os.listdir(self.__path)) != 0 and os.path.isfile(metadata_tags_file_path):
            with open(metadata_tags_file_path, "rb") as metadata_tags_file:
                self.__metadata_tags = pickle.load(metadata_tags_file)

    def set_data_container(self, data_container: DataContainer) -> None:
        self.__data_container = data_container

    def pull(self) -> None:
        if len(self.__metadata_tags) == 0:
            return
        else:
            file_names: List[str] = os.listdir(self.__path)
            time_serial_numbers: List[int] = [int(name.split('.')[0]) for name in file_names
                                              if name.split('.')[0].isdigit()]
            last_time_serial_number: int = max(time_serial_numbers)
            data_file_name: str = str(last_time_serial_number) + ".db"
            data_file_path: str = os.path.join(self.__path, data_file_name)
            with open(data_file_path, "rb") as data_file:
                self.__data_container.copy(pickle.load(data_file))

    def push(self) -> None:
        static_data: DataContainer = self.__data_container.clone()
        static_data_metadata_tags: List[str] = static_data.get_metadata_tags()

        if len(self.__metadata_tags) == 0:
            self.__metadata_tags = static_data_metadata_tags
            metadata_tags_file_path: str = os.path.join(self.__path, ".metadata_tags")
            with open(metadata_tags_file_path, "wb") as metadata_tags_file:
                pickle.dump(self.__metadata_tags, metadata_tags_file)
        else:
            if static_data_metadata_tags != self.__metadata_tags:
                raise ValueError("The metadata tags of data container are not match the database requirement.")

        # Serialize data and store to database.
        data_file_name: str = str(datetime.now().strftime("%Y%m%d%H%M%S%f")) + ".db"
        data_file_path: str = os.path.join(self.__path, data_file_name)
        with open(data_file_path, "wb") as data_file:
            pickle.dump(static_data, data_file)

        # Clear historical data.
        file_names: List[str] = os.listdir(self.__path)
        time_serial_numbers: List[int] = [int(name.split('.')[0]) for name in file_names
                                          if name.split('.')[0].isdigit()]
        last_time_serial_number: int = max(time_serial_numbers)
        file_to_keep: List[str] = [str(last_time_serial_number) + ".db", ".metadata_tags"]
        for file_name in file_names:
            if file_name not in file_to_keep:
                os.remove(os.path.join(self.__path, file_name))
