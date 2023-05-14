import openpyxl


class _Excel:
    def __init__(self, excel_file_path, excel_sheet):
        self._m_wb = openpyxl.load_workbook(excel_file_path)
        self._m_sheet = self._m_wb[excel_sheet]

        self.__m_info = {}
        self.__m_info["max_row"] = self._m_sheet.max_row
        self.__m_info["max_col"] = self._m_sheet.max_column

    @property
    def info(self):
        return self.__m_info


from .tag import DataLabels


class ExcelTableConverter(_Excel):
    def set_datum_row(self, row, data_labels: DataLabels):
        self.__m_column_data_labels = data_labels

        datum_row = []
        for columns in self._m_sheet.iter_cols(min_row=row, max_row=row, values_only=True):
            datum_row.append(columns[0])

        for label in data_labels:
            label.serial_num = datum_row.index(label.original)

    def get_row(self, row):
        python_dict = {}

        get_row = []
        for columns in self._m_sheet.iter_cols(min_row=row, max_row=row, values_only=True):
            get_row.append(columns[0])

        for data_labels_index, associated_column_serial_num in zip(range(0, len(self.__m_column_data_labels)),
                                                                   self.__m_column_data_labels.associated_sequence):
            python_dict[str(self.__m_column_data_labels[data_labels_index])] = get_row[associated_column_serial_num]

        return python_dict
