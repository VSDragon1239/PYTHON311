from PySide6.QtUiTools import loadUiType
import os

from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеКартинки_В_Браузере import MapDisplay
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеКартинкиВ_НовомОкне import MapWindow
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеКоординатОбъектов import CoordsComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеОбластьКрайРеспубликуДляГорода import \
    AddressComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеПочтовогоИндексаПоАдресу import \
    IndexComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеФедеральногоОкруга import getFederal

main_gui_path = os.path.abspath("ЗаданиеПервое/Интерфейс/ГрафическийИнтерфейс.ui")
print(main_gui_path)
x = -1
if x == -1:
    Ui_mainGUI, QMainWindow = loadUiType(
        'ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_API/ЗаданиеПервое/Интерфейс/ГрафическийИнтерфейс.ui')
else:
    Ui_mainGUI, QMainWindow = loadUiType(main_gui_path)


class mainGUI(Ui_mainGUI, QMainWindow):
    def __init__(self):
        super(mainGUI, self).__init__()
        self.setupUi(self)
        self.town = ''
        self.button_connection()
        self.coords = ''
        self.mapType = 'map'
        self.location_params = ''

    def button_connection(self):
        self.pushButton.clicked.connect(self.getMetaData)
        self.commandLinkButton.clicked.connect(self.openStaticMap)
        self.commandLinkButton_2.clicked.connect(self.openStaticMapImage)
        self.radioButton.toggled.connect(self.onToggledMap)

    def getMetaData(self):
        # print('#' * 5, end='\r')
        # print('@' * 2, end='\r')
        # sys.stdout.write("\r")
        print('GetMetaData', end='\n', )
        self.plainTextEdit.setPlainText(None)
        self.town = self.lineEdit.text()
        self.getFederalData()
        self.getAddress()
        self.getIndex()
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
        """
            Федеральный округ
        """
        federalInstance = getFederal(self.town)
        province = federalInstance.get_address_component(1)
        self.displayProvince(province)

    def getAddress(self):
        """
        Область, край, республика, другое...
        """
        AddressInstance = AddressComponentExtractor(self.town)
        area = AddressInstance.get_address_component(2)
        self.displayProvince(area)

    def getCoords(self):
        """
            Получение координат и их запись в «self.coords»
        """
        extractor = CoordsComponentExtractor(self.town)
        self.coords = extractor.get_address_coords()
        print('Из "getCoords" в "ПГИ" - self.coords  =   ', self.coords)
        coordText = "Координаты"
        self.displayProvince(self.coords, coordText)
        self.location_params = f"ll={self.coords.replace(' ', ',')}&spn=0.005,0.005"

    def getIndex(self):
        extractor = IndexComponentExtractor(self.town)
        index = extractor.get_address_postal_code()
        self.displayProvince(index)

    def openStaticMap(self):
        """
            Используем координаты из «self.coord» для открытия статик карты
        """
        if self.coords:

            map_display = MapDisplay(self.location_params, self.mapType)
            map_display.show_map()

    def onToggledMap(self, checked):
        if checked:
            self.mapType = 'sat'
        else:
            self.mapType = 'map'

    def openStaticMapImage(self):
        """
            Открытие в новом окне картинку выбранного места на карте
        """
        if self.coords:
            self.map_displayImage = MapWindow(self.location_params, self.mapType)
            self.map_displayImage.show()

