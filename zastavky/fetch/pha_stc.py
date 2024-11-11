from arcgis.features import FeatureLayer


def get_stations() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://services5.arcgis.com/SBTXIEUGWbqzUecw/arcgis/rest/services/DOP_CUR_DOP_PID_ZASTAVKY_B/FeatureServer/0")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        stations.append((
            feature.attributes["ZAST_NAZEV"],
            feature.attributes["ZAST_NAZEV1"],
            feature.geometry["x"],
            feature.geometry["y"]
        ))
    return stations