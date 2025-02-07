from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import Signal, QObject
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.ОбработкаНажатийМышы_И_Клавиатуры.loadUi import *
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.ОбработкаНажатийМышы_И_Клавиатуры.Функции.СозданиеОбъектаНаКнопкиМыши import \
    DrawingWidget


class Communicate(QObject):
    updateAddonWindowState = Signal(bool)
    openAdditionalWindow = Signal(str)


class mainGUI(Ui_mainGUI, QMainWindow):
    def __init__(self):
        super(mainGUI, self).__init__()
        self.addonWindowOpen = False
        self.setupUi(self)
        self.connectPushButtons()

        # Создаем объекты для обмена данными между окнами
        self.communicate = Communicate()
        self.communicate.updateAddonWindowState.connect(self.updateAddonWindowState)

    def connectPushButtons(self):
        self.BTN01111_func.clicked.connect(self.addonWindow1Interface)

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

    def addonWindow1Interface(self):
        self.ASFP = AddonWindow1()
        self.ASFP.closed.connect(self.updateAddonWindowState)  # Подключаем сигнал к слоту
        self.ASFP.show()
        self.setEnabled(self.addonWindowOpen)
        self.addonWindowOpen = True
        print('Второе окно 1 было активированно')

    def closeEvent(self, event):
        if self.addonWindowOpen:
            reply = QMessageBox.question(self, 'Предупреждение',
                                         "Вы уверены, что хотите закрыть приложение?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
                QApplication.exit()
            else:
                event.ignore()
        else:
            event.accept()
            QApplication.exit()

    def updateAddonWindowState(self):
        self.addonWindowOpen = False
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

