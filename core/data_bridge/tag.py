class _Label():
    def __init__(self, name):
        self.__m_original_name = name
        self.__m_universal_name = None
        self.__m_str = self.__m_original_name

        self.__m_serial_num = None

    def __str__(self):
        return self.__m_str

    def switch_original(self):
        self.__m_str = self.__m_original_name

    def switch_universal(self):
        self.__m_str = self.__m_universal_name

    @property
    def original(self):
        return self.__m_original_name

    @property
    def universal(self):
        return self.__m_universal_name

    @universal.setter
    def universal(self, universal_name):
        self.__m_universal_name = universal_name

    @property
    def serial_num(self):
        return self.__m_serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        self.__m_serial_num = serial_num


from easierfile import File
from oopmultilang import LangSwitcher


class DataLabels():
    def __init__(self, *label_names):
        self.__m_labels = []
        for label_name in label_names:
            label = _Label(label_name)
            self.__m_labels.append(label)

        self.__m_len = len(self.__m_labels)

    def __len__(self):
        return self.__m_len

    def __iter__(self):
        self.__m_index = 0
        return self

    def __next__(self):
        if self.__m_index >= self.__m_len:
            raise StopIteration

        value = self.__m_labels[self.__m_index]
        self.__m_index += 1
        return value

    def __getitem__(self, index):
        return self.__m_labels[index]

    def universalize(self, config_path):
        config_file = File(config_path, False, False)
        universalize_labels = LangSwitcher((config_file.info["path"]))

        for label in self.__m_labels:
            label.universal = universalize_labels.str(label.original, config_file.info["name"], None)

    def switch_original(self):
        for label in self.__m_labels:
            label.switch_original()

    def switch_universal(self):
        for label in self.__m_labels:
            label.switch_universal()

    @property
    def associated_sequence(self):
        associated_sequence = []
        for label in self.__m_labels:
            associated_sequence.append(label.serial_num)
        return associated_sequence
