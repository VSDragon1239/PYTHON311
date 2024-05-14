from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import Signal, QObject
from PySide6.QtUiTools import loadUiType
import os

from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.ОбработкаНажатийМышы_И_Клавиатуры.Функции.СозданиеОбъектаНаКнопкиМыши import \
    DrawingWidget

# main_gui_path = os.path.abspath("Интерфейсы/ГрафическийИнтерфейс.ui")
# addon_gui_path = os.path.abspath("Интерфейсы/ГрафическийИнтерфейс.ui")
# print(loadUiType(main_gui_path))

Ui_mainGUI, QMainWindow = loadUiType('ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_БазойДанныхSQLite/Интерфейсы/ГрафическийИнтерфейс.ui')
Ui_AddonWindow1, QWidget = loadUiType("ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_БазойДанныхSQLite/Интерфейсы/ВторойГрафическийИнтерфейс.ui")


class Communicate(QObject):
    update_addon_window_state = Signal(bool)
    open_additional_window = Signal(str)


class mainGUI(Ui_mainGUI, QMainWindow):
    def __init__(self):
        super(mainGUI, self).__init__()
        self.addon_window_open = False
        self.setupUi(self)
        self.button_connection()

        # Создаем объекты для обмена данными между окнами
        self.communicate = Communicate()
        self.communicate.update_addon_window_state.connect(self.update_addon_window_state)

    def button_connection(self):
        self.BTN01111_func.clicked.connect(self.addon_window_btn)

    def back_page(self):
        pass

    def continue_page(self):
        pass

    def check_path_name(self):
        pass

    def checker(self, lineedit_name):
        pass

    def select_path(self):
        pass

    def random_under_title(self):
        pass

    def addon_window_btn(self):
        self.ASFP = AddonWindow1()
        self.ASFP.closed.connect(self.update_addon_window_state)  # Подключаем сигнал к слоту
        self.ASFP.show()
        self.setEnabled(self.addon_window_open)
        self.addon_window_open = True
        print('Второе окно 1 было активированно')

    def closeEvent(self, event):
        if self.addon_window_open:
            QMessageBox.warning(self, 'Предупреждение', 'Нельзя закрыть главное окно, когда открыто второе окно!')
            event.ignore()
        else:
            reply = QMessageBox.question(self, 'Предупреждение',
                                         "Вы уверены, что хотите закрыть приложение?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def update_addon_window_state(self):
        self.addon_window_open = False
        self.setDisabled(False)


class AddonWindow1(Ui_AddonWindow1, QWidget):
    closed = Signal()  # Создаем сигнал, который будет отправлен при закрытии окна

    def __init__(self):
        super(AddonWindow1, self).__init__()
        self.setupUi(self)
        self.connectBTN()

    def connectBTN(self):
        self.pushButton.clicked.connect(self.activatedWidget)

    def activatedWidget(self):
        self.widget = DrawingWidget()
        self.widget.show()

    def closeEvent(self, event):
        self.closed.emit()  # Отправляем сигнал при закрытии окна
        event.accept()

