from arcgis.features import FeatureLayer


def get_stations_bus() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://services6.arcgis.com/ogJAiK65nXL1mXAW/arcgis/rest/services/Autobusov%C3%A9_zast%C3%A1vky_IREDO/FeatureServer/0")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        stations.append((
            feature.attributes["nazev"],
            "",
            feature.geometry["x"],
            feature.geometry["y"]
        ))
    return stations


def get_stations_train() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://services6.arcgis.com/ogJAiK65nXL1mXAW/arcgis/rest/services/%C5%BDelezni%C4%8Dn%C3%AD_stanice_a_zast%C3%A1vky_VDKHK/FeatureServer/0")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        stations.append((
            feature.attributes["nazev"],
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
