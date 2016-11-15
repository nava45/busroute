
ROUTE_MAP = {}

def store_routes(broute):
    routes = map(int, broute.split())
    rid, stationids = routes[0], routes[1:]
    print rid, stationids
    ROUTE_MAP[rid] = stationids


def lookup_station(arr_station, dep_station):
    for rid, stations in ROUTE_MAP.iteritems():
        if arr_station in stations and dep_station in stations:
            return True, rid
    return False, ''

