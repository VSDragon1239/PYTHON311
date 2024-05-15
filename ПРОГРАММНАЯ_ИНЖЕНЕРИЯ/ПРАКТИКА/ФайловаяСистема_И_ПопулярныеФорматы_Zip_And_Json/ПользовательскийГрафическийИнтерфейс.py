import zipfile

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QFileSystemModel
from PySide6.QtCore import Signal, QObject
from PySide6.QtUiTools import loadUiType
import os

test_x = -1
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
        self.pushButton_4.clicked.connect(self.return_files_in_zip)

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
            return -1

    def checker(self, lineedit_name):
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
        if self.lineEdit.text() == 'Path://':
            path = self.selectPath()
            if path == -1:
                return -1
        lines = self.get_files_sizes(path=self.lineEdit.text())
        output_string = '\n'.join('\t'.join(item) for item in lines)
        self.plainTextEdit_3.setPlainText(output_string)

    def build_file_tree(self, file_list):
        """
        Строит дерево файлов из списка имен файлов
        """
        tree = {}

        for filename in file_list:
            filename = filename.encode('cp437').decode('cp866')
            # Разбиваем имя файла на части по разделителю "/"
            parts = filename.strip('/').split('/')

            # Временное дерево
            current_level = tree

            # Проходим по каждой части и создаем вложенные словари
            for part in parts:
                if part not in current_level:
                    # Если последняя часть (файл), создаем как файл, иначе как папку
                    current_level[part] = {}
                current_level = current_level[part]

        return tree

    def print_tree(self, tree, indent=0):
        """
        Рекурсивно выводит дерево файлов
        """
        for key, value in tree.items():
            # Печатаем отступ в зависимости от глубины
            print(" " * indent, key, sep="")

            # Если это папка (имеет вложения), рекурсивно вызываем функцию
            if isinstance(value, dict) and value:
                self.print_tree(value, indent + 2)

    # def read_zipfile(self, archive):
    #     with zipfile.ZipFile(archive, 'r') as myzip:
    #         file_list = myzip.namelist()
    #
    #     # Сортируем по глубине (по числу '/') и имени
    #     sorted_file_list = sorted(file_list, key=lambda x: (x.count('/'), x))
    #
    #     # Строим дерево файлов
    #     file_tree = self.build_file_tree(sorted_file_list)
    #
    #     return file_tree

    def build_tree_widget(self, tree, parent_item=None):
        """
        Рекурсивно строит виджет дерева из дерева файлов
        """
        if parent_item is None:
            # Создаем модель, если это первый вызов функции
            self.model = QStandardItemModel()
            self.model.setHorizontalHeaderLabels(['Name'])
            parent_item = self.model.invisibleRootItem()

        # Проходим по всем элементам в дереве
        for key, value in tree.items():
            # Создаем новый элемент для каждого ключа в дереве
            item = QStandardItem(key)

            # Добавляем новый элемент к родительскому элементу
            parent_item.appendRow(item)

            # Если это папка (имеет вложения), рекурсивно вызываем функцию
            if isinstance(value, dict) and value:
                self.build_tree_widget(value, item)

    def read_zipfile(self, archive):
        with zipfile.ZipFile(archive, 'r') as myzip:
            file_list = myzip.namelist()

            # Создаем словарь для хранения размеров файлов
            file_sizes = {}

            for filename in file_list:
                # Получаем информацию о файле
                info = myzip.getinfo(filename)

                # Сохраняем размер файла
                file_sizes[filename] = info.file_size

            # Сортируем по глубине (по числу '/') и имени
            sorted_file_list = sorted(file_list, key=lambda x: (x.count('/'), x))

            # Строим дерево файлов
            file_tree = self.build_file_tree(sorted_file_list)

        return file_tree, file_sizes

    def return_files_in_zip(self, path=""):
        archive_path = self.chose_archive()
        if archive_path is None:
            return -1
        file_tree, file_sizes = self.read_zipfile(archive_path)

        # Строим виджет дерева из дерева файлов
        self.build_tree_widget(file_tree)

        # Устанавливаем модель для self.treeView_2
        self.treeView_2.setModel(self.model)

        # Создаем строку для вывода размеров файлов
        output_string = ""
        for filename, size in file_sizes.items():
            output_string += f"{filename}: {self.human_read_format(size)}\n"

        # Выводим размеры файлов в plainTextEdit_4
        self.plainTextEdit_4.setPlainText(output_string)

    def chose_archive(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        archive_path, _ = QFileDialog.getOpenFileName(
            None,
            "Выберите архив",
            "/path/to/default/directory",  # Начальный путь (необязательно)
            "Zip Files (*.zip);;All Files (*)",
            options=options
        )

        if archive_path:
            print("Выбранный архив:", archive_path)
            return archive_path

        else:
            print("Выбор отменен")