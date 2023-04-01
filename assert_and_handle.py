import sys

class C_PythonFile:
    def __init__(self,filePath,globalSymbols):
        self.__m_filePath = filePath
        self.__m_globalSymbols = globalSymbols
        self.__m_filePath_name = self.__m_filePath.split("\\")[-1].split(".")[0]

        self.__m_symbols_normal = []
        for globalSymbol in self.__m_globalSymbols:
            if (globalSymbol[0:2] != "__") and (globalSymbol[-1:-3] != "__") and (globalSymbol != "C_PythonFile") and (globalSymbol != "C_AssertHandler"):
                self.__m_symbols_normal.append(globalSymbol)

    @property
    def path(self):
        return self.__m_filePath

    @property
    def name(self):
        return self.__m_filePath_name

    @property
    def symbols_normal(self):
        return self.__m_symbols_normal

class C_AssertHandler:
    def __init__(self,pythonFile,expression,handleFunction = None,*handleFunctionParam):
        #Synchronize symbols of executed python file
        sys.path.append(pythonFile.path)
        for symbol in pythonFile.symbols_normal:
            exec("from {} import {}".format(pythonFile.name,symbol))
        #Assert and function handle
        try:
            self.__m_var = eval(expression)
        except:
            if handleFunction != None:
                handleFunction(*handleFunctionParam)
            self.__m_result = False
            self.__m_var = None
        else:
            self.__m_result = True
    @property
    def var(self):
        return self.__m_var

    @property
    def result(self):
        return self.__m_result