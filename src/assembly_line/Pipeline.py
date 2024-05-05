from typing import List

from assembly_line.Executable import Executable
from assembly_line.Completable import Completable


class Pipeline(Executable, Completable):
    def __init__(self):
        self.__stations: List[Executable] = []
        self.__completed_stage: int = 0

    def execute(self) -> None:
        for station in self.__stations:
            station.execute()
            self.__completed_stage += 1

    def add_station(self, station: Executable) -> None:
        self.__stations.append(station)

    def get_completion_percentage(self) -> float:
        return float(self.__completed_stage / len(self.__stations))
