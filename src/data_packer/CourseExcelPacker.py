from typing import Tuple
import re

from assembly_line.Executable import Executable
from data_packer.Excel import Excel
from data_storage.CoursePool import CoursePool
from data_model.Course import Course
from data_packer.DataType import DataType
from data_model.CourseNature import CourseNature


class CourseExcelPacker(Executable):
    def __init__(self, excel: Excel, course_pool: CoursePool, data_index: int):
        self.__excel: Excel = excel
        self.__course_pool: CoursePool = course_pool
        self.__data_index: int = data_index

    def execute(self) -> None:
        course_builder: Course.Builder = Course.Builder()

        # Get the raw data.
        raw_data: Tuple[str, ...] = self.__excel.get_row_data(self.__data_index, {
            "课程代码": DataType.STRING,
            "课程名称": DataType.STRING,
            "课程性质": DataType.STRING,
            "开课学院": DataType.STRING
        })

        # Process id in raw data.
        id_peeling_pattern: str = r'(.*?)(?:x|X|f|$)'
        raw_data_id: str = raw_data[0]
        peeled_data_id: str = re.search(id_peeling_pattern, raw_data_id).group(1)
        course_builder.id(peeled_data_id)

        # Process name in raw data.
        name_peeling_pattern: str = r'^(.*?)(?:\d+|(x|I|II|III).*)$'
        raw_data_name: str = raw_data[1]
        peeled_data_name: str = ""
        name_peeling_matched: re.Match = re.search(name_peeling_pattern, raw_data_name)
        if name_peeling_matched:
            peeled_data_name = name_peeling_matched.group(1)
        else:
            peeled_data_name = raw_data_name
        course_builder.name(peeled_data_name)

        # Process course nature in raw data.
        raw_data_nature: str = raw_data[2]
        course_nature: CourseNature = CourseNature.UNKNOW

        if raw_data_nature == "必修":
            course_nature = CourseNature.REQUIRED
        elif raw_data_nature == "任选":
            course_nature = CourseNature.OPTIONAL
        elif raw_data_nature == "限选":
            course_nature = CourseNature.LIMITED_ELECTIVE
        elif raw_data_nature == "'专业任选":
            course_nature = CourseNature.MAJOR_OPTIONAL

        course_builder.nature(course_nature)

        # Process supplier in raw data.
        raw_data_supplier: str = raw_data[3]
        course_builder.supplier(raw_data_supplier)

        # Add course object to the course pool.
        course: Course = course_builder.build()
        self.__course_pool.add_data(course)