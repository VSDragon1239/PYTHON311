from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QFileSystemModel
from PySide6.QtCore import Signal, QObject
from PySide6.QtUiTools import loadUiType
import os

test_x = 1
if test_x == -1:
    Ui_mainGUI, QMainWindow = loadUiType('ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/ФайловаяСистема_И_ПопулярныеФорматы_Zip_And_Json/Интерфейсы/ГрафическийИнтерфейсМэйн.ui')
else:
    Ui_mainGUI, QMainWindow = loadUiType('Интерфейсы/ГрафическийИнтерфейсМэйн.ui')


class mainGUI(Ui_mainGUI, QMainWindow):
    def __init__(self):
        super(mainGUI, self).__init__()
        self.addon_window_open = False
        self.setupUi(self)
        self.selected_directory = ''
        self.button_connection()

        self.model = QFileSystemModel()

    def button_connection(self):
        self.pushButton.clicked.connect(self.selectPath)
        self.pushButton_2.clicked.connect(self.testing_h_r_f)
        self.pushButton_3.clicked.connect(self.checking_size_from_path)

    def back_page(self):
        pass

    def continue_page(self):
        pass

    def selectPath(self):
        self.selected_directory = QFileDialog.getExistingDirectory(
            None,
            "Выберите директорию",
            "/path/to/default/directory"  # Начальный путь (необязательно)
        )

        if self.selected_directory:
            print("Выбранная директория:", self.selected_directory)
            self.lineEdit.setText(self.selected_directory)

            self.model.setRootPath("")

            # Устанавливаем модель для treeView
            self.treeView.setModel(self.model)
            self.model.setRootPath(self.lineEdit.text())
            self.treeView.setRootIndex(self.model.index(self.lineEdit.text()))
        else:
            print("Выбор отменен")

    def checker(self, lineedit_name):
        pass

    def select_path(self):
        pass

    def human_read_format(self, size):
        size1 = int(size)
        X = 10
        if self.check_size(size) == 0:
            if size < 2 ** X:
                return str(size) + "Б"  # Байты
            elif size < 2 ** (X * 2):
                return str(round((size / (2 ** X)))) + "КБ"
            elif size < 2 ** 30:
                return str(round(size / 2 ** (X * 2))) + "МБ"
            elif size < 2 ** 40:
                return str(round(size / 2 ** (X * 3))) + "ГБ"

    def check_size(self, size):
        if size >= 0:
            return 0
        else:
            print("Неправильный ввод!")
            return -1

    def testing_h_r_f(self):
        X = self.plainTextEdit.toPlainText()
        X = eval(X)


        test = []
        x = 0
        for i in X:
            x += 1
            test.append(self.human_read_format(i))
        output_string = '\n'.join(str(item) for item in test)
        self.plainTextEdit_2.setPlainText(output_string)

    # Чтение всех файлов в папке, с флажком только чтение файлов (не надо читать папки)
    def get_files_sizes(self, path="", only_read_files=True):
        list_files = []
        list_files_and_folders = []
        list_all = []

        for file in os.listdir(os.chdir(path)):
            file_and_size = {os.path.splitext(file): self.human_read_format(os.path.getsize(file))}
            if os.path.isfile(file):
                list_files.append(file_and_size)
                list_files_and_folders.append(file_and_size)
            else:
                list_files_and_folders.append(file_and_size)

        if only_read_files:
            for file_name in list_files:
                for i in file_name.values():
                    for x in file_name.keys():
                        list_all.append([x[0], x[1], i])
            return list_all
        else:
            for file_name in list_files_and_folders:
                for i in file_name.values():
                    for x in file_name.keys():
                        list_all.append([x[0], x[1], i])
            return list_all

    def checking_size_from_path(self):
        lines = self.get_files_sizes(path=self.lineEdit.text())
        output_string = '\n'.join('\t'.join(item) for item in lines)
        self.plainTextEdit_3.setPlainText(output_string)