from geopy.geocoders import Nominatim

def coordinates_from_address(address):
    """
    :return: set - Coordinates for a given address or raise ValueError if address not found
    """
    geolocator = Nominatim(user_agent="ntdc")

    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError('Unknown address.')


from scipy import spatial

def closest_locations(coordinates, locations, count):
    """
    :param coordinates: Set of coordinates (latitude and longitude)
    :param locations: List of set of coordinates
    :param count: Number of locations to return
    :return: string - Closest locations to given coordinates from list
    """
    tree = spatial.KDTree(locations)
    dd, closest_locations = tree.query([coordinates])
    return closest_locations[0:count]
