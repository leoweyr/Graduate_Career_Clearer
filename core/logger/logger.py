from enum import Enum


class LogType(Enum):
    INFO = 0
    ERROR = -1
    OPERATE = 1


import datetime
from easierfile import File


class Logger:
    def __init__(self, log_dir, is_print=True):
        time_now_date = datetime.datetime.now().strftime("%Y-%m-%d")

        self.__m_file = File(f"{log_dir}/{time_now_date}.log")
        self.__m_is_print = is_print

    def log(self, log_type, content):
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        log_content = f"[{time_now} {log_type.name}]{str(content)} \n"

        self.__m_file.append(log_content)

        if self.__m_is_print:
            print(log_content)
