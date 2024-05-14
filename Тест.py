from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication
from PySide6.QtCore import Qt

class Window1(QMainWindow):
    def __init__(self, window2, window3):
        super().__init__()
        self.setWindowTitle('Window 1')
        self.window2 = window2
        self.window3 = window3
        self.button = QPushButton('Open Window 2', self)
        self.button.clicked.connect(self.open_window2)
        self.setCentralWidget(self.button)

    def open_window2(self):
        self.hide()
        self.window2.show()


class Window2(QMainWindow):
    def __init__(self, window1, window3):
        super().__init__()
        self.setWindowTitle('Window 2')
        self.window1 = window1
        self.window3 = window3
        self.button = QPushButton('Open Window 3', self)
        self.button.clicked.connect(self.open_window3)
        self.setCentralWidget(self.button)

    def open_window3(self):
        self.hide()
        self.window3.show()


class Window3(QMainWindow):
    def __init__(self, window1, window2):
        super().__init__()
        self.setWindowTitle('Window 3')
        self.window1 = window1
        self.window2 = window2
        self.button = QPushButton('Open Window 1', self)
        self.button.clicked.connect(self.open_window1)
        self.setCentralWidget(self.button)

    def open_window1(self):
        self.hide()
        self.window1.show()


app = QApplication([])
window1 = Window1(None, None)
window2 = Window2(window1, None)
window3 = Window3(window1, window2)
window1.window2 = window2
window1.window3 = window3
window1.show()
app.exec_()
