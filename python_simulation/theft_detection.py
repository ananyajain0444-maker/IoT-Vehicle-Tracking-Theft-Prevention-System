def detect_theft(is_inside_geofence):
    if not is_inside_geofence:
        return 'THEFT ALERT'
    return 'SAFE'
