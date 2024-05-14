from ПользовательскийГрафическийИнтерфейс import *
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.ОбработкаНажатийМышы_И_Клавиатуры.ПользовательскийГрафическийИнтерфейс import mainGUI as SecondMainWindow
from PySide6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    guiMain = MainInterface(None)
    guiLabs = LabsInterface(guiMain, None)
    guiLabTasks = LabTasksInterface(guiLabs, None)
    guiTasks = TasksInterface(guiLabTasks)

    guiMain.labsInterfaceInstance = guiLabs

    guiLabs.labTasksInterfaceInstance = guiLabTasks

    guiLabTasks.tasksInterfaceInstance = guiTasks

    guiMain.show()
    sys.exit(app.exec())
