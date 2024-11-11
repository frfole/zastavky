from arcgis.features import FeatureLayer


def get_stations_bus() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://services.arcgis.com/S6UQzkU4EoJgYA53/arcgis/rest/services/Autobusov%C3%A9_zast%C3%A1vky_IREDO/FeatureServer/22")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        obec = feature.attributes["obec"]
        cast_obce = feature.attributes["cast_obce"]
        lokalita = feature.attributes["lokalita"]
        if cast_obce:
            cast_obce = cast_obce.strip()
        if lokalita:
            lokalita = lokalita.strip()
        if cast_obce and not lokalita:
            nazev = obec + "," + cast_obce
        elif lokalita and not cast_obce:
            nazev = obec + ",," + lokalita
        elif cast_obce and lokalita:
            nazev = obec + "," + cast_obce + "," + lokalita
        else:
            nazev = obec
        stations.append((
            nazev,
            "",
            feature.geometry["x"],
            feature.geometry["y"]
        ))
    return stations


def get_stations_train() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://services.arcgis.com/S6UQzkU4EoJgYA53/arcgis/rest/services/Vlakov%C3%A9_zast%C3%A1vky_IREDO/FeatureServer/0")
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
