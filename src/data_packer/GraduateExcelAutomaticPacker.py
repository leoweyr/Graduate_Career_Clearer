from assembly_line.Pipeline import Pipeline
from data_packer.excel import Excel
from data_packer.GraduateExcelPacker import GraduateExcelPacker
from assembly_line.Executable import Executable


class GraduateExcelAutomaticPacker(Pipeline):
    def __init__(self, excel_file_path: str, excel_sheet: str):
        super().__init__()
        self.__excel: Excel = Excel(excel_file_path, excel_sheet)

    def execute(self) -> None:
        for data_index in range(2, self.__excel.long):
            self.add_station(GraduateExcelPacker(self.__excel, data_index))
        super().execute()

    def add_station(self, station: Executable) -> None:
        super().add_station(station)

    def get_completion_percentage(self) -> float:
        return super().get_completion_percentage()