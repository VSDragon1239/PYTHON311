from PySide6.QtWebEngineWidgets import QWebEngineView


class MapWindow(QWebEngineView):
    def __init__(self, location_params, map_type="map"):
        super().__init__()

        base_url = "https://static-maps.yandex.ru/1.x/?"
        params = f"{location_params}&l={map_type}"
        url = base_url + params

        self.load(url)
