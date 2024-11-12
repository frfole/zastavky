import argparse
from argparse import FileType

import geojson
from geojson import Feature, Point, FeatureCollection

import zastavky.fetch.hkk
import zastavky.fetch.jhc
import zastavky.fetch.lbc
import zastavky.fetch.pak
import zastavky.fetch.pha_stc
import zastavky.fetch.plk
import zastavky.fetch.ulk
import zastavky.fetch.vlaky
import zastavky.fetch.vys
import zastavky.fetch.jhm
from zastavky.post.dup import filter_same, as_stations


def export_as_geojson(stations: list[tuple[str, str, float, float]], output):
    new_stations = [
        Feature(
            geometry=Point((station[2], station[3])),
            properties={"name": station[0], "altname": station[0]}
        )
        for station in stations
    ]
    stations_collection = FeatureCollection(new_stations)
    with output as f:
        geojson.dump(stations_collection, f)

def load_from_geojson() -> list[tuple[str, str, float, float]]:
    stations = []
    with open("out.geojson") as f:
        station_collection = geojson.load(f)
        for i in station_collection.features:
            stations.append((
                i.properties["name"],
                i.properties["altname"],
                i.geometry.coordinates[0],
                i.geometry.coordinates[1]
            ))
    return stations


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--pha-stc", help="Fetches stations in Prague and Central Bohemian region", action="store_true")
    arg_parser.add_argument("--hkk", help="Fetches stations in Hradec Králové region", action="store_true")
    arg_parser.add_argument("--pak", help="Fetches stations in Pardubice region", action="store_true")
    arg_parser.add_argument("--lbc", help="Fetches stations in Liberec region", action="store_true")
    arg_parser.add_argument("--jhc", help="Fetches stations in South Bohemian region", action="store_true")
    arg_parser.add_argument("--plk", help="Fetches stations in Plzeň region", action="store_true")
    arg_parser.add_argument("--ulk", help="Fetches stations in Ustí nad Labem region", action="store_true")
    arg_parser.add_argument("--vys", help="Fetches stations in Vysočina region", action="store_true")
    arg_parser.add_argument("--jhm", help="Fetches stations in South Moravian region", action="store_true")
    arg_parser.add_argument("--vlaky", help="Fetches train stations in Czechia", action="store_true")
    arg_parser.add_argument("--all", help="Fetches stations from all sources", action="store_true")
    arg_parser.add_argument("--dedup", help="Merges station of same name and location into one", action="store_false")
    arg_parser.add_argument("output", help="Output geojson file for stations", type=FileType("w"))
    args = arg_parser.parse_args()

    all_stations = []
    if args.pha_stc or args.all:
        print("Fetching in Prague and Central Bohemian region...")
        all_stations.extend(zastavky.fetch.pha_stc.get_stations())
    if args.hkk or args.all:
        print("Fetching in Hradec Králové region...")
        all_stations.extend(zastavky.fetch.hkk.get_stations())
    if args.pak or args.all:
        print("Fetching in Pardubice region...")
        all_stations.extend(zastavky.fetch.pak.get_stations())
    if args.lbc or args.all:
        print("Fetching in Liberec region...")
        all_stations.extend(zastavky.fetch.lbc.get_stations())
    if args.jhc or args.all:
        print("Fetching in South Bohemian region...")
        all_stations.extend(zastavky.fetch.jhc.get_stations())
    if args.plk or args.all:
        print("Fetching in Plzeň region...")
        all_stations.extend(zastavky.fetch.plk.get_stations())
    if args.ulk or args.all:
        print("Fetching in Ústí nad Labem region...")
        all_stations.extend(zastavky.fetch.ulk.get_stations())
    if args.vys or args.all:
        print("Fetching in Vysočina region...")
        all_stations.extend(zastavky.fetch.vys.get_stations())
    if args.jhm or args.all:
        print("Fetching in South Moravian region...")
        all_stations.extend(zastavky.fetch.jhm.get_stations())
    if args.vlaky or args.all:
        print("Fetching trains...")
        all_stations.extend(zastavky.fetch.vlaky.get_stations())
    if args.dedup:
        print("Removing duplicate entries...")
        all_stations = as_stations(filter_same(all_stations))
    print("Saving", len(all_stations), "stations")
    export_as_geojson(all_stations, args.output)
    print("Done")

if __name__ == '__main__':
    main()
