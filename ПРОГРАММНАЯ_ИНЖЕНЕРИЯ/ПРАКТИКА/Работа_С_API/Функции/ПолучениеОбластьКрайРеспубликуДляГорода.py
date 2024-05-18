from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.Функции import geocoder


class AddressComponentExtractor:
    def __init__(self, town):
        self.town = town

    def get_address_component(self, component_index):
        # Ищем переданный адрес, ответ получаем в формате json.
        toponym = geocoder.geocode(self.town)

        # Получаем компонентный адрес.
        components = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
        # Извлекаем из него запрошенный компонент (Страна, Округ, Область, Район, Город и т.д.) и его название.
        return components[component_index]["name"]
