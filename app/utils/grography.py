import math


def distance_in_km(lat1, lon1, lat2, lon2):
    r = 6378.137  # Radius of earth in KM
    d_lat = (lat2 * math.pi / 180) - (lat1 * math.pi / 180)
    d_lon = (lon2 * math.pi / 180) - (lon1 * math.pi / 180)
    a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.sin(d_lon / 2) * math.sin(d_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c

    return d