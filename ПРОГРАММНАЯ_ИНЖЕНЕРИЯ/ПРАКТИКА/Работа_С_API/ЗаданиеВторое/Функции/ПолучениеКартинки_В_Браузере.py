# from mapapi_PG import show_map
import webbrowser


# def show_maps():
#     # Параметры позиционирования карты и ее тип.
#     map_locations = {
#         "Австралия": ("ll=135.746181,-27.483765&spn=20,20", "sat")
#     }
#
#     for map_location, map_type in map_locations.values():
#         show_map(map_location, map_type)
#
#
# def main():
#     # Показать спутниковый снимок Австралии
#     show_maps()
#
#
# if __name__ == "__main__":
#     main()


class MapDisplay:
    def __init__(self, location_params, map_type="map"):
        self.location_params = location_params
        self.map_type = map_type

    def show_map(self):
        """
        Отображает карту в браузере по заданным параметрам.
        """
        base_url = "https://static-maps.yandex.ru/1.x/?"
        params = f"{self.location_params}&l={self.map_type}"
        url = base_url + params
        webbrowser.open(url)




    # @staticmethod
    # def show_maps():
    #     # Параметры позиционирования карты и ее тип.
    #     map_locations = {
    #         "Австралия": ("ll=135.746181,-27.483765&spn=20,20", "sat")
    #     }
    #
    #     for location_params, map_type in map_locations.values():
    #         map_display = MapDisplay(location_params, map_type)
    #         map_display.show_map()
