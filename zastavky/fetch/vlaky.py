import urllib.request

import geojson
import pygml.parse
import requests
from geojson import GeoJSON
from owslib.wfs import WebFeatureService


def get_stations_train() -> list[tuple[str, str, float, float]]:
    params = dict(
        service="WFS",
        version="2.0.0",
        request="GetFeature",
        typeName="zeleznice_stanice:zeleznicni_stanice_a_zastavky",
        outputFormat="json",
        srsName="urn:ogc:def:crs:EPSG::4326",
    )
    r = requests.get("https://gis.cenia.cz/geoserver/ows?service=WFS", params=params)
    data_json = r.json()
    stations = []
    for feature in data_json["features"]:
        stations.append((
            feature["properties"]["nazev"],
            "",
            feature["geometry"]["coordinates"][0][0],
            feature["geometry"]["coordinates"][0][1]
        ))
    return stations


def get_stations() -> list[tuple[str, str, float, float]]:
    stations = []
    stations.extend(get_stations_train())
    return stations