import shapefile


def get_stations() -> list[tuple[str, str, float, float]]:
    sf = shapefile.Reader("https://dopravnimapy.kraj-lbc.cz/opendata/zastavky_shp_wgs84.zip", encoding="windows-1250")
    stations = []
    for shapeRecord in sf.iterShapeRecords():
        stations.append((
            shapeRecord.record[1],
            "",
            shapeRecord.record[6],
            shapeRecord.record[7],
        ))
    return stations
