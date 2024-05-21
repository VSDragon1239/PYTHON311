from PySide6.QtUiTools import loadUiType
import os

from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеКартинки_В_Браузере import MapDisplay
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеКоординатОбъектов import CoordsComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеОбластьКрайРеспубликуДляГорода import \
    AddressComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеПочтовогоИндексаПоАдресу import \
    IndexComponentExtractor
from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции.ПолучениеФедеральногоОкруга import getFederal

main_gui_path = os.path.abspath("ЗаданиеВторое/Интерфейс/ГрафическийИнтерфейс.ui")
print(main_gui_path)
x = 1
if x == -1:
    Ui_mainGUI, QMainWindow = loadUiType(
        'ПРОГРАММНАЯ_ИНЖЕНЕРИЯ/ПРАКТИКА/Работа_С_API/ЗаданиеВторое/Интерфейс/ГрафическийИнтерфейс.ui')
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

    def button_connection(self):
        self.pushButton.clicked.connect(self.getMetaData)
        self.commandLinkButton.clicked.connect(self.openStaticMap)
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

    def onToggledMap(self, checked):
        if checked:
            self.mapType = 'sat'
        else:
            self.mapType = 'map'

    def openStaticMap(self):
        """
            Используем координаты из «self.coord» для открытия статик карты
        """
        if self.coords:
            location_params = f"ll={self.coords.replace(' ', ',')}&spn=0.005,0.005"
            map_display = MapDisplay(location_params, self.mapType)
            map_display.show_map()

    def openStaticMapImage(self):
        """
            Открытие в новом окне картинку выбранного места на карте
        """
        if self.coords:
            pass

