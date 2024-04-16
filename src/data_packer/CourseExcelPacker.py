from typing import Tuple, Dict, List
import re

from assembly_line.Executable import Executable
from data_packer.excel import Excel
from data_model.Course import Course
from data_packer.DataTag import DataTag
from data_packer.DataType import DataType
from data_packer.DataPack import DataPack
from data_model.CourseNature import CourseNature
from data_storage.CoursePool import CoursePool


class CourseExcelPacker(Executable):
    def __init__(self, excel: Excel, data_index: int):
        self.__excel: Excel = excel
        self.__data_index: int = data_index

    def execute(self) -> None:
        course_builder: Course.Builder = Course.Builder()

        # Get the raw data.
        course_code_data_tag: DataTag = DataTag(["课程代码"], DataType.STRING)
        course_name_data_tag: DataTag = DataTag(["课程名称"], DataType.STRING)
        course_nature_data_tag: DataTag = DataTag(["课程性质"], DataType.STRING)
        course_supplier_data_tag: DataTag = DataTag(["开课学院"], DataType.STRING)
        raw_data: Tuple[DataPack, ...] = self.__excel.get_row_data(self.__data_index, [
            course_code_data_tag,
            course_name_data_tag,
            course_nature_data_tag,
            course_supplier_data_tag
        ])

        # Process id in raw data.
        id_peeling_pattern: str = r'(.*?)(?:x|X|f|$)'
        raw_data_id: str = raw_data[0].content
        peeled_data_id: str = re.search(id_peeling_pattern, raw_data_id).group(1)
        course_builder.id_(peeled_data_id)

        # Process name in raw data.
        name_peeling_pattern: str = r'^(.*?)(?:\d+|(x|I|II|III).*)$'
        raw_data_name: str = raw_data[1].content
        peeled_data_name: str = ""
        name_peeling_matched: re.Match = re.search(name_peeling_pattern, raw_data_name)
        if name_peeling_matched:
            peeled_data_name = name_peeling_matched.group(1)
        else:
            peeled_data_name = raw_data_name
        course_builder.name(peeled_data_name)

        # Process course nature in raw data.
        raw_data_nature: str = raw_data[2].content
        course_nature: CourseNature = CourseNature.UNKNOWN

        if raw_data_nature == "必修":
            course_nature = CourseNature.REQUIRED
        elif raw_data_nature == "任选":
            course_nature = CourseNature.OPTIONAL
        elif raw_data_nature == "限选":
            course_nature = CourseNature.LIMITED_ELECTIVE
        elif raw_data_nature == "专业任选":
            course_nature = CourseNature.MAJOR_OPTIONAL

        course_builder.nature(course_nature)

        # Process supplier in raw data.
        raw_data_supplier: str = raw_data[3].content
        course_builder.supplier(raw_data_supplier)

        # Create Course object containing only metadata by Course.Builder
        course: Course = course_builder.build()

        # Process terms in raw data.
        peeled_data_terms: int = -1

        if "x" in raw_data_id:
            peeled_data_terms = int(raw_data_id.split("x")[1])
        elif "X" in raw_data_id:
            peeled_data_terms = int(raw_data_id.split("X")[1])
        elif "f" in raw_data_id:
            peeled_data_terms = int(raw_data_id.split("f")[1])
        else:
            peeled_data_terms = 1

        if peeled_data_terms == 0:
            peeled_data_terms = 1

        course.set_terms(peeled_data_terms)
        course_pool: CoursePool = CoursePool()
        course_meta_data: Dict[str, str] = course.get_metadata()
        existing_same_courses_in_course_pool: List[Course] = course_pool.get_data(course_meta_data)

        if existing_same_courses_in_course_pool:
            if int(course.get_data()["terms"]) > int(existing_same_courses_in_course_pool[0].get_data()["terms"]):
                course_pool.remove_data(course_meta_data)

        # Add Course object to the course pool.
        course_pool.add_data(course)
