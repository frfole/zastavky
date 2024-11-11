from arcgis.features import FeatureLayer


def get_stations_bus() -> list[tuple[str, str, float, float]]:
    fl = FeatureLayer("https://mapy.kr-vysocina.cz/arcgis/rest/services/Doprava/SchemaLinek/MapServer/7")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        obec = feature.attributes["OBEC"]
        cast_obce = feature.attributes["OBEC_CAST"]
        lokalita = feature.attributes["BLIZSI_MIS"]
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
    fl = FeatureLayer("https://mapy.kr-vysocina.cz/arcgis/rest/services/Doprava/SchemaLinek/MapServer/6")
    features = fl.query(out_sr=4326).features
    stations = []
    for feature in features:
        stations.append((
            feature.attributes["ZST_P"],
            "",
            feature.geometry["points"][0][0],
            feature.geometry["points"][0][1]
        ))
    return stations


def get_stations() -> list[tuple[str, str, float, float]]:
    stations = []
    stations.extend(get_stations_bus())
    stations.extend(get_stations_train())
    return stations
