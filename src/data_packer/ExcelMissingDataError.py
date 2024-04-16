from data_packer.excel import Excel
from data_packer.DataPack import DataPack


class ExcelMissingDataError(Exception):
    def __init__(self, excel: Excel, data_pack: DataPack):
        self.__excel: Excel = excel
        self.__data_pack = data_pack
        super().__init__(f"Excel <{excel}> is missing data for {data_pack.used_tag_name}.")
