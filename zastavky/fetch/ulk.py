from arcgis.features import FeatureLayer


def get_stations_bus() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://ags.kr-ustecky.cz/arcgis/rest/services/Doprava/zastavky/MapServer/0")
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
    return stations
