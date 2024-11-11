from arcgis.features import FeatureLayer


def get_stations_bus() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://mapy.plzensky-kraj.cz/ArcGIS/rest/services/zastavky/MapServer/1")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        stations.append((
            feature.attributes["OZNACENI"],
            "",
            feature.geometry["x"],
            feature.geometry["y"]
        ))
    return stations


def get_stations_train() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://mapy.plzensky-kraj.cz/ArcGIS/rest/services/zastavky/MapServer/0")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        stations.append((
            feature.attributes["NAZEV"],
            "",
            feature.geometry["x"],
            feature.geometry["y"]
        ))
    return stations


def get_stations() -> list[tuple[str, str, float, float]]:
    stations = []
    stations.extend(get_stations_bus())
    stations.extend(get_stations_train())
    return stations
