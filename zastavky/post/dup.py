from geopy.distance import distance


def filter_same(stations: list[tuple[str, str, float, float]]) -> dict[str, list[tuple[str, str, float, float]]]:
    stations.sort(key=lambda x: x[0])
    filtered_stations = {}
    for i in range(1, len(stations)):
        if stations[i][0] in filtered_stations:
            is_same = False
            for test_station in filtered_stations[stations[i][0]]:
                dst = distance((test_station[2], test_station[3]), (stations[i][2], stations[i][3]))
                if dst.km < 5:
                    is_same = True
                    break
            if not is_same:
                filtered_stations[stations[i][0]].append(stations[i])
        else:
            filtered_stations[stations[i][0]] = [stations[i]]
    return filtered_stations


def as_stations(stations: dict[str, list[tuple[str, str, float, float]]]) -> list[tuple[str, str, float, float]]:
    new_stations = []
    for station_name in stations:
        new_stations.extend(stations[station_name])
    return new_stations


def find_duplicates(stations: list[tuple[str, str, float, float]]):
    stations = filter_same(stations)
    for station in stations:
        if len(stations[station]) > 1:
            print(stations[station])