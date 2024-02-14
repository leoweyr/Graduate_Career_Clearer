from enum import Enum


class CourseNature(Enum):
    UNKNOW = 0
    REQUIRED = 1
    MAJOR_OPTIONAL = 2
    LIMITED_ELECTIVE = 3
    OPTIONAL = 4