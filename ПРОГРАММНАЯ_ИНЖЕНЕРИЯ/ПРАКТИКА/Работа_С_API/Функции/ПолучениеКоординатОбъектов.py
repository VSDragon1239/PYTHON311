from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.Работа_С_API.Функции import geocoder


# Функция для получения координат
# def get_address_coords(address):
#     # Определяется функция get_address_coords, которая принимает строковый параметр address.
#
#     toponym = \
#         geocoder.geocode(address)  # Внутри функции вызывается geocode(address), которая ищет указанный адрес и
#     # возвращает результат в формате JSON.
#
#     toponym_address = \
#         toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
#     # Из полученного JSON-документа извлекается полный адрес, который находится в toponym["metaDataProperty"][
#     # "GeocoderMetaData"]["text"].
#     print(toponym_address)
#
#     # Координаты центра топонима:
#     # Из JSON-документа извлекаются координаты центра топонима, которые находятся в toponym["Point"]["pos"].
#     # Эти координаты возвращаются из функции.
#     toponym_coordinates = toponym["Point"]["pos"]
#     return toponym_coordinates
#
#
# def main():
#     """Получение координат по адресу.
#     Определяется функция main, которая отвечает за основную логику программы.
#     Внутри функции используется цикл for,
#     который проходит по списку адресов
#     (в данном случае это только один адрес: "Москва, Красная площадь, 1").
#     Для каждого адреса вызывается get_address_coords(address), результат которой (координаты)
#     сохраняется в переменную coords.
#     Затем координаты выводятся на экран в формате строки с помощью print."""
#
#     for address in ["Москва, Красная площадь, 1", "Чита, ул. Баргузинская, 49а"]:
#         coords = get_address_coords(address)
#         print(f"{address} имеет координаты: {coords}")
#     print("")
#
#
# if __name__ == "__main__":
#     main()


# Этот код предназначен для того, чтобы взять адрес,
# например "Москва, Красная площадь, 1", и с помощью функции geocode
# из библиотеки geocoder получить его географические координаты (широту и долготу).
# Затем эти координаты выводятся на экран.


class CoordsComponentExtractor:
    def __init__(self, town):
        self.town = town

    def get_address_coords(self):
        # Определяется функция get_address_coords, которая принимает строковый параметр address.

        toponym = \
            geocoder.geocode(self.town)  # Внутри функции вызывается geocode(address), которая ищет указанный адрес и
        # возвращает результат в формате JSON.

        toponym_address = \
            toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Из полученного JSON-документа извлекается полный адрес, который находится в toponym["metaDataProperty"][
        # "GeocoderMetaData"]["text"].
        print(toponym_address)

        # Координаты центра топонима:
        # Из JSON-документа извлекаются координаты центра топонима, которые находятся в toponym["Point"]["pos"].
        # Эти координаты возвращаются из функции.
        toponym_coordinates = toponym["Point"]["pos"]
        return toponym_coordinates
