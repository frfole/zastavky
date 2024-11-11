import shapefile
from pyproj import Transformer


def get_stations() -> list[tuple[str, str, float, float]]:
    sf = shapefile.Reader("https://geoportal.kraj-jihocesky.gov.cz/portal/media/Soubory/opendata/zastavky_JCK_SHP.zip")
    stations = []
    transformer = Transformer.from_crs("EPSG:5514", "EPSG:4326")
    for shapeRecord in sf.iterShapeRecords():
        coords = transformer.transform(shapeRecord.shape.points[0][0], shapeRecord.shape.points[0][1])
        stations.append((
            shapeRecord.record[1],
            "",
            coords[1],
            coords[0],
        ))
    return stations
