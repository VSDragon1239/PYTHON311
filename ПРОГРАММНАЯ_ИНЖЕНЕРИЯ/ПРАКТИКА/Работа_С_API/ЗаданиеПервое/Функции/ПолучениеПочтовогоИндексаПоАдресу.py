from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.ЗаданиеПервое.Функции import geocoder


class IndexComponentExtractor:
    def __init__(self, town):
        self.town = town

    def get_address_postal_code(self):
        # Ищем переданный адрес, ответ получаем в формате json.
        toponym = geocoder.geocode(self.town)
        # Извлекаем почтовый индекс.
        postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
        print("Из \"ПолучениеПочтовогоИндексаПоАдресу\" - postal_code   =   ", postal_code)
        return postal_code
