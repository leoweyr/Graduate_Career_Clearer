import datetime
timeNow = datetime.datetime.now()

from enum import Enum

class C_File:
    def __init__(self,filePath):
        self.m_filePath = filePath
        try:
            self.m_file = open(self.m_filePath,"x")
        except:
            pass
        else:
            self.m_file.close()

    def Write(self,content):
        self.m_file = open(self.m_filePath,"w")
        self.m_file.write(content)
        self.m_file.close()

    def Append(self,content):
        self.m_file = open(self.m_filePath,"a")
        self.m_file.write(content)
        self.m_file.close()

class E_LogType(Enum):
        INFO = 1
        ERROR = 2
        Operate = 3

class C_Logger:
        def __init__(self,logType,content):
            if logType.value == 1:
                logType = "INFO"
            elif logType.value == 2:
                logType = "ERROR"
            elif logType.value == 3:
                logType = "Operate"
            else:
                pass
            logFile = C_File(timeNow.strftime("%Y-%m-%d") + ".txt")
            logContent = "[" + timeNow.strftime("%Y-%m-%d %H:%M:%S") + " " + logType + "]" + content + "\n"
            logFile.Append(logContent)
            print(logContent)