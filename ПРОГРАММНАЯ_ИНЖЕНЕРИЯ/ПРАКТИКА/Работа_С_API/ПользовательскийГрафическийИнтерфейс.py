from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QVBoxLayout, QFileDialog, QDialog, QInputDialog, \
    QLineEdit, QLabel, QSpinBox
from PySide6.QtUiTools import loadUiType
import os

from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.Функции.ПолучениеКартинки_В_Браузере import MapDisplay
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.Функции.ПолучениеКоординатОбъектов import CoordsComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.Функции.ПолучениеОбластьКрайРеспубликуДляГорода import \
    AddressComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.Функции.ПолучениеФедеральногоОкруга import getFederal

main_gui_path = os.path.abspath("Интерфейс/ГрафическийИнтерфейс.ui")

x = -1
if x == -1:
    Ui_mainGUI, QMainWindow = loadUiType(
        'ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_API/Интерфейс/ГрафическийИнтерфейс.ui')
else:
    Ui_mainGUI, QMainWindow = loadUiType(main_gui_path)


class mainGUI(Ui_mainGUI, QMainWindow):
    def __init__(self):
        super(mainGUI, self).__init__()
        self.setupUi(self)
        self.town = ''
        self.button_connection()
        self.coords = ''

    def button_connection(self):
        self.pushButton.clicked.connect(self.getMetaData)
        self.commandLinkButton.clicked.connect(self.openStaticMap)

    def getMetaData(self):
        self.town = self.lineEdit.text()
        self.getFederalData()
        self.getAddress()
        self.getCoords()

    def displayProvince(self, province, coord=''):
        if coord == '':
            if self.plainTextEdit.toPlainText() != "":
                self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText() + '\n' + province)
            else:
                self.plainTextEdit.setPlainText(province)
        else:
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText() + '\n' + 'Координаты   ' + province)

    def getFederalData(self):
        federalInstance = getFederal(self.town)
        province = federalInstance.get_address_component(1)
        self.displayProvince(province)

    def getAddress(self):
        extractor = AddressComponentExtractor(self.town)
        area = extractor.get_address_component(2)
        self.displayProvince(area)

    def getCoords(self):
        extractor = CoordsComponentExtractor(self.town)
        self.coords = extractor.get_address_coords()
        coordText = "Координаты"
        self.displayProvince(self.coords, coordText)

    def openStaticMap(self):
        # Используем координаты, полученные в getCoords
        if self.coords:
            location_params = f"ll={self.coords.replace(' ', ',')}&spn=0.005,0.005"
            map_display = MapDisplay(location_params, "map")
            map_display.show_map()
