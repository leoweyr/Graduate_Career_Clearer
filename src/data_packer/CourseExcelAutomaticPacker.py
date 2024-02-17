from assembly_line.Pipeline import Pipeline
from data_storage.CoursePool import CoursePool
from data_packer.Excel import Excel
from data_packer.CourseExcelPacker import CourseExcelPacker
from assembly_line.Executable import Executable


class CourseExcelAutomaticPacker(Pipeline):
    def __init__(self, excel_file_path: str, excel_sheet: str, course_pool: CoursePool):
        super().__init__()
        self.__excel: Excel = Excel(excel_file_path, excel_sheet)
        self.__course_pool: CoursePool = course_pool

    def execute(self) -> None:
        for data_index in range(2, self.__excel.long):
            self.add_station(CourseExcelPacker(self.__excel, self.__course_pool, data_index))
        super().execute()

    def add_station(self, station: Executable) -> None:
        super().add_station(station)

    @property
    def completed_stage(self) -> float:
        return super().completed_stage
