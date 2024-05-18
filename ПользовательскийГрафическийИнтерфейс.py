from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import Signal, QObject
from PySide6.QtUiTools import loadUiType
import os
import subprocess
import sys


mainUiPath = os.path.abspath("ГлавноеМеню.ui")
labsUiPath = os.path.abspath("ЛабороторныеРаботы.ui")
labTasksUiPath = os.path.abspath("ЛабароторныеЗадачи.ui")
tasksUiPath = os.path.abspath("ИнтерфейсЗадач.ui")

mainGui, QMainGui = loadUiType(mainUiPath)
labsGui, QLabsGui = loadUiType(labsUiPath)
labTasksGui, QLabTasksGui = loadUiType(labTasksUiPath)
tasksGui, QTasksGui = loadUiType(tasksUiPath)


class Communicate(QObject):
    updateAddonWindowState = Signal(bool)
    openAdditionalWindow = Signal(str)


class MainInterface(mainGui, QMainGui):
    def __init__(self, LabsInterface):
        super(mainGui, self).__init__()
        self.setupUi(self)
        self.buttonConnection()
        self.labsInterfaceInstance = LabsInterface
        self.labTasksInterfaceInstance = LabTasksInterface

    def buttonConnection(self):
        self.pushButton_4.clicked.connect(self.activatedQWidgetLabsInterface)

    def activatedQWidgetLabsInterface(self):
        self.hide()  # Скрываем главное окно
        self.labsInterfaceInstance.show()  # Показываем дополнительное окно


class LabsInterface(labsGui, QLabsGui):
    def __init__(self, MainInterface, LabTasksInterface):
        super(labsGui, self).__init__()
        self.setupUi(self)

        self.MainInterfaceInstance = MainInterface
        self.labTasksInterfaceInstance = LabTasksInterface

        self.connectPushButtons()

    def connectPushButtons(self):
        self.pushButton.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(1))
        self.pushButton_2.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(2))
        self.pushButton_3.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(3))
        self.pushButton_4.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(4))
        self.pushButton_5.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(5))
        self.pushButton_6.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(6))
        self.pushButton_7.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(7))
        self.pushButton_8.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(8))
        self.pushButton_9.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(9))
        self.pushButton_10.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(10))
        self.pushButton_11.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(11))
        self.pushButton_12.clicked.connect(lambda: self.activatedQWidgetLabTasksInterface(12))

        self.pushButton_13.clicked.connect(self.backEvent)

    def backEvent(self):
        self.hide()  # Скрываем окно
        self.MainInterfaceInstance.show()

    def activatedQWidgetLabTasksInterface(self, labsInterfaceId=1):
        print('Проверка ЛР', labsInterfaceId)
        self.hide()
        self.labTasksInterfaceInstance.labsInterfaceId = labsInterfaceId
        self.labTasksInterfaceInstance.label.setText("ЛР - " + str(self.labTasksInterfaceInstance.labsInterfaceId))
        self.labTasksInterfaceInstance.show()


class LabTasksInterface(labTasksGui, QLabTasksGui):
    def __init__(self, LabsInterface, TasksInterface):
        super(labTasksGui, self).__init__()
        self.setupUi(self)
        self.labsInterfaceId = 0

        self.tasksInterfaceInstance = TasksInterface
        self.labsInterfaceInstance = LabsInterface

        self.connectPushButton()

    def connectPushButton(self):
        self.pushButton.clicked.connect(lambda: self.activatedQWidgetTasksInterface(1))
        self.pushButton_2.clicked.connect(lambda: self.activatedQWidgetTasksInterface(2))
        self.pushButton_3.clicked.connect(lambda: self.activatedQWidgetTasksInterface(3))
        self.pushButton_4.clicked.connect(lambda: self.activatedQWidgetTasksInterface(4))
        self.pushButton_5.clicked.connect(lambda: self.activatedQWidgetTasksInterface(5))
        self.pushButton_6.clicked.connect(lambda: self.activatedQWidgetTasksInterface(6))
        self.pushButton_7.clicked.connect(lambda: self.activatedQWidgetTasksInterface(7))
        self.pushButton_8.clicked.connect(lambda: self.activatedQWidgetTasksInterface(8))
        self.pushButton_9.clicked.connect(lambda: self.activatedQWidgetTasksInterface(9))
        self.pushButton_10.clicked.connect(lambda: self.activatedQWidgetTasksInterface(10))
        self.pushButton_11.clicked.connect(lambda: self.activatedQWidgetTasksInterface(11))
        self.pushButton_12.clicked.connect(lambda: self.activatedQWidgetTasksInterface(12))
        self.pushButton_13.clicked.connect(self.backEvent)

    def activatedQWidgetTasksInterface(self, TasksInterfaceId):
        print('Проверка задания: ', TasksInterfaceId)
        self.hide()

        self.tasksInterfaceInstance.labsInterfaceId = self.labsInterfaceId
        self.tasksInterfaceInstance.TasksInterfaceId = TasksInterfaceId
        self.tasksInterfaceInstance.label.setText("Задача " + str(self.tasksInterfaceInstance.TasksInterfaceId))
        self.getTaskPlainText(self.labsInterfaceId, TasksInterfaceId)

        self.tasksInterfaceInstance.disconnectTask()
        self.tasksInterfaceInstance.connectTask()
        self.tasksInterfaceInstance.show()

    def getTaskPlainText(self, labsInterfaceId, TasksInterfaceId):
        if labsInterfaceId == 6 and TasksInterfaceId == 3:
            self.tasksInterfaceInstance.plainTextEdit.setPlainText(
                'Создайте sqlite базу данных, в которой можно хранить информацию об объектах, которые находятся в квартире: название вещи, год покупки, тип (мебель, бытовая техника и т. д.) и помещение, в котором этот объект находится (кухня, гостиная, спальная комната и т. д.). Учтите, что в одной комнате может быть много разных объектов, и к одному типу может принадлежать также несколько объектов. Наполните ее тестовыми данными. \n Примечание: в данной задаче необходимо создать только базу данных sqlite.')
        elif labsInterfaceId == 5 and TasksInterfaceId == 1:
            self.tasksInterfaceInstance.plainTextEdit.setPlainText(
                'Напишите функцию get_result(name), которая принимает на вход имя файла базы данных, по структуре идентичной «films.db», и удаляет все фильмы в жанре комедии из БД.')
        elif labsInterfaceId == 5 and TasksInterfaceId == 7:
            self.tasksInterfaceInstance.plainTextEdit.setPlainText(
                'Напишите функцию get_result(name), которая принимает на вход имя файла базы данных, по структуре идентичной «films.db», и выполняет запрос, обновляющий таблицу с фильмами таким образом, чтобы длина мюзиклов, превышающая 100 минут, стала равна 100.')
        else:
            self.tasksInterfaceInstance.plainTextEdit.setPlainText('')

    def backEvent(self):
        self.hide()
        self.labsInterfaceInstance.show()


class TasksInterface(tasksGui, QTasksGui):
    def __init__(self, LabTasksInterface):
        super(tasksGui, self).__init__()
        self.setupUi(self)
        self.connectPushButton()
        self.labsInterfaceId = 0
        self.TasksInterfaceId = 0
        self.labTasksInterfaceInstance = LabTasksInterface

    def connectPushButton(self):
        self.pushButton_2.clicked.connect(self.backEvent)

    def backEvent(self):
        self.hide()
        self.labTasksInterfaceInstance.show()

    def connectTask(self):
        print(self.TasksInterfaceId, self.labsInterfaceId)
        self.pushButton.clicked.connect(lambda: self.activateTaskLab1(self.labsInterfaceId, self.TasksInterfaceId))

    def disconnectTask(self):
        self.pushButton.clicked.disconnect()

    def activateTaskLab1(self, labId, taskId):
        print('Активация Задания: ', taskId, '\n', 'ЛР - ', labId)
        if labId == 6 and taskId == 1:
            subprocess.Popen([sys.executable, "ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/ОбработкаНажатийМышы_И_Клавиатуры/МЭЙН.py"])
        elif labId == 6 and taskId == 3:
            subprocess.Popen([sys.executable, "ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_БазойДанныхSQLite/МЭЙН.py"])
        elif labId == 8 and taskId == 1:
            subprocess.Popen([sys.executable, "ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/ФайловаяСистема_И_ПопулярныеФорматы_Zip_And_Json/МЭЙН.py"])
        elif labId == 9 and taskId == 1:
            subprocess.Popen([sys.executable, "ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_API/МЭЙН.py"])


