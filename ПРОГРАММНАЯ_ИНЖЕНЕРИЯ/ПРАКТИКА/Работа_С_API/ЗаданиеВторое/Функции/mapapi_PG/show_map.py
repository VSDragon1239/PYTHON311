import webbrowser


def show_map(location_params, map_type="map"):
    """
    Отображает карту в браузере по заданным параметрам.

    :param location_params: Параметры местоположения для отображения карты.
    :param map_type: Тип карты (например, "map" для карты, "sat" для спутникового изображения).
    """
    base_url = "https://static-maps.yandex.ru/1.x/?"
    params = f"{location_params}&l={map_type}"
    url = base_url + params
    webbrowser.open(url)

