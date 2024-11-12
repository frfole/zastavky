import gtfs_kit


def get_stations() -> list[tuple[str, str, float, float]]:
    feed = gtfs_kit.read_feed("https://kordis-jmk.cz/gtfs/gtfs.zip", "m")
    stops = gtfs_kit.get_stops(feed)
    stations = []
    for stop in stops.itertuples():
        stations.append((
            stop.stop_name,
            "",
            stop.stop_lon,
            stop.stop_lat,
        ))
    return stations