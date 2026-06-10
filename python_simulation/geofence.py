from geopy.distance import geodesic

SAFE_LOCATION = (28.6139, 77.2090)
SAFE_RADIUS_METERS = 500

def check_geofence(latitude, longitude):
    current_location = (latitude, longitude)
    distance = geodesic(SAFE_LOCATION, current_location).meters

    if distance > SAFE_RADIUS_METERS:
        return False
    return True
