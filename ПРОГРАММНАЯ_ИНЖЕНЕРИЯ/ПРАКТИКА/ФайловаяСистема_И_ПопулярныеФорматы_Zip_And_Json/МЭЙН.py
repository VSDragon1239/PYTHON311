from ПользовательскийГрафическийИнтерфейс import mainGUI
from PySide6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = mainGUI()
    gui.show()
    sys.exit(app.exec())
