from PySide6 import QtCore, QtGui, QtUiTools
from PySide6.QtWidgets import QApplication


def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = loadUiWidget("C:\(1)PROGRAMMIROVANIE\PYTHON\TESTGUIui.ui")
    MainWindow.show()
    sys.exit(app.exec_())