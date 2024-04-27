from typing import Tuple, Union, Dict, List
import re

from assembly_line.Executable import Executable
from data_packer.excel import Excel
from data_packer.DataTag import DataTag
from data_packer.DataType import DataType
from data_packer.DataPack import DataPack
from data_packer.ExcelMissingDataError import ExcelMissingDataError
from data_model.Gender import Gender
from data_model.Graduate import Graduate
from data_storage.GraduatePool import GraduatePool
from data_model.Major import Major
from data_storage.MajorPool import MajorPool
from data_storage.ObjectNotFoundError import ObjectNotFoundError
from criterion.PointCriterion import PointCriterion


class GraduateExcelPacker(Executable):
    def __init__(self, excel: Excel, data_index: int):
        self.__excel: Excel = excel
        self.__data_index: int = data_index

    def execute(self) -> None:
        # Setting DataTag for extracting graduate basic information.
        graduate_id_data_tag: DataTag = DataTag(["学号"], DataType.INTEGER)
        graduate_name_data_tag: DataTag = DataTag(["姓名"], DataType.STRING)
        graduate_gender_data_tag: DataTag = DataTag(["性别"], DataType.STRING)
        graduate_class_data_tag: DataTag = DataTag(["班级"], DataType.STRING)
        graduate_college_data_tag: DataTag = DataTag(["学院"], DataType.STRING)
        graduate_major_data_tag: DataTag = DataTag(["专业", "专业名称"], DataType.STRING)

        # Setting DataTag for extracting graduate career information.
        graduate_gpa_data_tag: DataTag = DataTag(["平均学分绩点"], DataType.FLOAT)
        graduate_required_credits_data_tag: DataTag = DataTag(["必修"], DataType.FLOAT)
        graduate_major_optional_credits_data_tag: DataTag = DataTag(["专业任选"], DataType.FLOAT)
        graduate_limited_elective_credits_data_tag: DataTag = DataTag(["限选"], DataType.FLOAT)
        graduate_optional_credits_data_tag: DataTag = DataTag(["任选"], DataType.FLOAT)

        # Setting DataTag for extracting graduate taken course information.
        taken_course_code_data_tag: DataTag = DataTag(["课程代码"], DataType.STRING)
        taken_course_points_data_tag: DataTag = DataTag(["最高成绩"], DataType.STRING)

        # Get the raw data.
        raw_data: Tuple[DataPack, ...] = self.__excel.get_row_data(self.__data_index, [
            graduate_id_data_tag,
            graduate_name_data_tag,
            graduate_gender_data_tag,
            graduate_class_data_tag,
            graduate_college_data_tag,
            graduate_major_data_tag,
            graduate_gpa_data_tag,
            graduate_required_credits_data_tag,
            graduate_major_optional_credits_data_tag,
            graduate_limited_elective_credits_data_tag,
            graduate_optional_credits_data_tag,
            taken_course_code_data_tag,
            taken_course_points_data_tag
        ])

        # Check whether necessary raw data is missing.
        if raw_data[0].content is None:
            raise ExcelMissingDataError(self.__excel, raw_data[0])
        elif raw_data[1].content is None:
            raise ExcelMissingDataError(self.__excel, raw_data[1])
        elif raw_data[2].content is None:
            raise ExcelMissingDataError(self.__excel, raw_data[2])
        elif raw_data[3].content is None:
            raise ExcelMissingDataError(self.__excel, raw_data[3])
        elif raw_data[4].content is None:
            raise ExcelMissingDataError(self.__excel, raw_data[4])
        elif raw_data[5].content is None:
            raise ExcelMissingDataError(self.__excel, raw_data[5])

        # Process id in raw data.
        raw_data_id: int = raw_data[0].content

        # Process name in raw data.
        raw_data_name: str = raw_data[1].content

        # Process gender in raw data.
        raw_data_gender: str = raw_data[2].content
        peeled_data_gender: Gender = Gender.UNKNOWN

        if raw_data_gender == "男":
            peeled_data_gender = Gender.MALE
        elif raw_data_gender == "女":
            peeled_data_gender = Gender.FEMALE
        else:
            raise ValueError(f"Invalid value <{raw_data_gender}> for graduate gender in excel <{self.__excel}> row "
                             f"<{self.__data_index}>.")

        # Process class in raw data.
        raw_data_class: str = raw_data[3].content

        # Process grade in raw data.
        peeled_data_grade: int = int(str(raw_data_id)[:2] + raw_data_class[3:5])

        # Process college in raw data.
        raw_data_college: str = raw_data[4].content

        """
        Just get major from the raw data first, then decide whether to process it after confirming the existence 
        of the Graduate object in the graduate pool, thus achieving the purpose of reducing unnecessary operations.
        """
        raw_data_major: str = raw_data[5].content

        """
        Check if the Graduate object already exists in the graduate pool.
        If it does, retrieve it for use directly.
        If it doesn't exist, prepare to create a new one.
        """
        graduate: Union[Graduate, None] = None
        graduate_builder: Graduate.Builder = Graduate.Builder()
        graduate_pool: GraduatePool = GraduatePool()
        graduate_metadata: Dict[str, str] = {
            "id": str(raw_data_id),
            "name": str(raw_data_name),
            "gender": str(peeled_data_gender),
            "grade": str(peeled_data_grade),
            "class": str(raw_data_class),
            "college": str(raw_data_college),
            "major": str(raw_data_major)
        }
        existing_same_graduates_in_graduate_pool: List[Graduate] = graduate_pool.get_data(graduate_metadata)

        if existing_same_graduates_in_graduate_pool:
            graduate = existing_same_graduates_in_graduate_pool[0]
        else:
            # Process major in raw data before creating the Graduate object.
            peeled_data_major: Union[Major, None] = None
            major_pool: MajorPool = MajorPool()
            condition_for_major_retrieval: Dict[str, str] = {"name": raw_data_major}
            retrieved_majors: List[Major] = major_pool.get_data(condition_for_major_retrieval)

            if len(retrieved_majors) == 0:
                raise ObjectNotFoundError(major_pool, condition_for_major_retrieval)
            elif len(retrieved_majors) == 1:
                peeled_data_major = retrieved_majors[0]
            else:
                # Filter out the major that match the edition corresponding to the graduate grade.
                retrieved_majors_sorted = sorted(retrieved_majors, key=lambda major: major.get_data()["edition"])

                for retrieved_major in retrieved_majors_sorted:
                    retrieved_major_edition: int = retrieved_major.get_data()["edition"]
                    if retrieved_major_edition <= peeled_data_grade:
                        peeled_data_major = retrieved_major
                    else:
                        break

                if peeled_data_major is None:
                    raise ValueError(
                        f"No major in the major pool meets graduate of grade <{peeled_data_grade}> obtained "
                        f"from excel <{self.__excel}> row <{self.__data_index}>.")

            # Create Graduate object by Graduate.Builder.
            graduate = (
                graduate_builder.
                id_(raw_data_id).
                name(raw_data_name).
                gender(peeled_data_gender).
                grade(peeled_data_grade).
                class_(raw_data_class).
                college(raw_data_college).
                major(peeled_data_major).
                build()
            )

        # Process gpa if it exists in raw data.
        if raw_data[6].content is not None:
            graduate.set_gpa(raw_data[6].content)

        # Process required credits if it exists in raw data.
        if raw_data[7].content is not None:
            graduate.set_required_credits(raw_data[7].content)

        # Process major optional credits if it exists in raw data.
        if raw_data[8].content is not None:
            graduate.set_major_optional_credits(raw_data[8].content)

        # Process limited elective credits if it exists in raw data.
        if raw_data[9].content is not None:
            graduate.set_limited_elective_credits(raw_data[9].content)

        # Process optional credits if it exists in raw data.
        if raw_data[10].content is not None:
            graduate.set_optional_credits(raw_data[10].content)

        # Process taken course if it exists in raw data.
        if raw_data[11].content is not None and raw_data[12].content is not None:
            # Process taken course id in raw data.
            taken_course_id_peeling_pattern: str = r'(.*?)(?:x|X|f|$)'
            peeled_taken_course_id: str = re.search(taken_course_id_peeling_pattern, raw_data[11].content).group(1)

            # Add taken course to the Graduate object.
            graduate.add_taken_courses({"id": peeled_taken_course_id}, peeled_taken_course_id, PointCriterion())

        # Add Graduate object to the graduate pool if it is new.
        if not existing_same_graduates_in_graduate_pool:
            graduate_pool.add_data(graduate)
