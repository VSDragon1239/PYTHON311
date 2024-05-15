from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QVBoxLayout, QFileDialog, QDialog, QInputDialog, \
    QLineEdit, QLabel, QSpinBox
from PySide6.QtUiTools import loadUiType
import os
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_БазойДанныхSQLite.Функции.СозданиеБазыДанных import ApartmentDatabase

main_gui_path = os.path.abspath("Интерфейсы/ГрафическийИнтерфейс.ui")

x = -1
if x == -1:
    Ui_mainGUI, QMainWindow = loadUiType('ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_БазойДанныхSQLite/Интерфейсы/ГрафическийИнтерфейс.ui')
else:
    Ui_mainGUI, QMainWindow = loadUiType(main_gui_path)


class mainGUI(Ui_mainGUI, QMainWindow):
    def __init__(self):
        super(mainGUI, self).__init__()
        self.setupUi(self)
        self.button_connection()
        self.action_connection()
        self.label.setText('Вкусности квартиры')
        self.db = None
        # self.InputDialog = InputDialog()

    def button_connection(self):
        pass

    def action_connection(self):
        self.action.triggered.connect(self.open_database)
        self.action_2.triggered.connect(self.create_database)

    def open_database(self):
        db_file, _ = QFileDialog.getOpenFileName(self, "Open SQLite Database", "",
                                                 "SQLite Database Files (*.sqlite *.db);;All Files (*)")

        if db_file:
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName(db_file)
            self.visible_database()

    def visible_database(self):
        if not self.db.open():
            print("Ошибка при открытии базы данных")

        # Создайте модель данных
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable(self.getTables()[0])
        self.model.select()
        self.tableView.setModel(self.model)

        print(self.getTables()[0])


    def getTables(self):
        query = self.db.exec_("""
            SELECT name FROM sqlite_master WHERE type='table';
        """)
        tables = []
        while query.next():
            tables.append(query.value(0))
        return tables

    def create_database(self):
        path_db = QFileDialog.getExistingDirectory(self, "Open Folder для Database", "")
        if path_db:
            db_name, ok = QInputDialog.getText(self, 'Input Dialog', 'Введите название базы данных:')
            if ok:
                self.dbA = ApartmentDatabase(db_name, path_db)
                self.dbA.create_table_items()
                data = [
                    ('Диван', 2020, 'Мебель', 'Гостиная'),
                    ('Холодильник', 2018, 'Бытовая техника', 'Кухня'),
                    ('Телевизор', 2021, 'Бытовая техника', 'Гостиная'),
                    ('Кровать', 2019, 'Мебель', 'Спальная комната'),
                    ('Стол', 2021, 'Мебель', 'Кухня'),
                    ('Стул', 2022, 'Мебель', 'Кухня'),
                    ('Шкаф', 2018, 'Мебель', 'Спальная комната'),
                    ('Плита', 2020, 'Бытовая техника', 'Кухня'),
                    ('Микроволновка', 2021, 'Бытовая техника', 'Кухня'),
                    ('Комод', 2022, 'Мебель', 'Гостиная'),
                    ('Кофеварка', 2021, 'Бытовая техника', 'Кухня'),
                    ('Ковер', 2020, 'Мебель', 'Гостиная'),
                    ('Пылесос', 2022, 'Бытовая техника', 'Кладовка'),
                    ('Зеркало', 2021, 'Мебель', 'Ванная комната'),
                ]

                self.dbA.insert_data(data)
                self.dbA.close()


    #             # Получить количество таблиц
    #             num_tables, ok = QInputDialog.getInt(self, 'Input Dialog', 'Введите количество таблиц:')
    #
    #             if ok:
    #                 # Для каждой таблицы получить название и количество столбцов
    #                 for i in range(num_tables):
    #                     table_data = {}  # Инициализация словаря для данных таблицы
    #
    #                     table_name, ok = QInputDialog.getText(self, 'Input Dialog',
    #                                                           f'Введите название таблицы {i + 1}:')
    #
    #                     if ok:
    #                         table_data['table_name'] = table_name  # Добавить название таблицы в словарь данных таблицы
    #
    #                         num_columns, ok = QInputDialog.getInt(self, 'Input Dialog',
    #                                                               f'Введите количество столбцов для таблицы {table_name}:')
    #
    #                         if ok:
    #                             table_data[
    #                                 'num_columns'] = num_columns  # Добавить количество столбцов в словарь данных таблицы
    #                             table_data['columns'] = []  # Инициализация списка для названий столбцов
    #
    #                             # Для каждого столбца получить название
    #                             for j in range(num_columns):
    #                                 column_name, ok = QInputDialog.getText(self, 'Input Dialog',
    #                                                                        f'Введите название столбца {j + 1} для таблицы {table_name}:')
    #
    #                                 if ok:
    #                                     table_data['columns'].append(
    #                                         column_name)  # Добавить название столбца в список названий столбцов
    #
    #                             data.append(table_data)  # Добавить словарь данных таблицы в список данных
    #
    #         metadata = [{'table_name': 'Предметы', 'num_columns': 5, 'columns': ['Мебель', 'Бытовая техника', 'Фигня всякая', 'Помещение', 'Тип']}]
    #         datas = self.generate_empty_records(metadata)
    #         print(datas)
    #         #
    #
    # def generate_empty_records(self, metadata):
    #     data = []
    #     for table in metadata:
    #         for _ in range(table['num_columns']):
    #             record = tuple(None for _ in range(len(table['columns'])))
    #             data.append(record)
    #     return data


# class InputDialog(QDialog):
#     def __init__(self):
#         super().__init__()
#
#         self.layout = QVBoxLayout(self)
#
#         self.db_name_label = QLabel("Название базы данных", self)
#         self.db_name_input = QLineEdit(self)
#
#         self.num_tables_label = QLabel("Количество таблиц", self)
#         self.num_tables_input = QSpinBox(self)
#         self.num_tables_input.valueChanged.connect(self.update_tables)
#
#         self.tables_inputs = []
#
#         self.layout.addWidget(self.db_name_label)
#         self.layout.addWidget(self.db_name_input)
#         self.layout.addWidget(self.num_tables_label)
#         self.layout.addWidget(self.num_tables_input)
#
#     def update_tables(self):
#         num_tables = self.num_tables_input.value()
#
#         # Удалить старые поля ввода
#         for table_input in self.tables_inputs:
#             self.layout.removeWidget(table_input)
#             table_input.deleteLater()
#         self.tables_inputs.clear()
#
#         # Добавить новые поля ввода
#         for i in range(num_tables):
#             table_input = QLineEdit(self)
#             self.layout.addWidget(table_input)
#             self.tables_inputs.append(table_input)
#
#     def getText(self):
#         pass