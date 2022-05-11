import requests
import math
api_key = '5758fb87d0125025a8e357c34f764643'
bing_key = 'Am7F2ze1ur7AiRfHCja5K5BcRlWU0YrFUOTkPuPkADEWkz2w139sYjoKge6D1bJw'

def get_monterey_info():
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    coords = get_monterey_coords()

    payload = {
        'appid': api_key,
        'units': 'imperial',
        'lat': coords['lat'],
        'lon': coords['lon']
    }
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        data['wind']['dir'] = get_wind_direction(data)
        data['weather'][0]['description'] = data['weather'][0]['description'].title()
        data['traffic'] = get_traffic_condition()
        return data
    except:
        print('failed')


def get_monterey_coords():
    endpoint = 'http://api.openweathermap.org/geo/1.0/direct'

    payload = {
        'q': 'Monterey,CA,US',
        'appid': api_key,
        'limit': 1
    }

    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        return {'lat': data[0]['lat'], 'lon': data[0]['lon']}
    except:
        print('failed')


def get_wind_direction(data):
    degrees = data['wind']['deg']
    if 0 <= degrees <= 22.5 or 337.5 <= degrees <= 360:
        return 'north'
    elif 22.5 <= degrees <= 67.5:
        return 'northeast'
    elif 67.5 <= degrees <= 112.5:
        return 'east'
    elif 112.5 <= degrees <= 157.5:
        return 'southeast'
    elif 157.5 <= degrees <= 202.5:
        return 'south'
    elif 202.5 <= degrees <= 247.5:
        return 'southwest'
    elif 247.5 <= degrees <= 292.5:
        return 'west'
    elif 292.5 <= degrees <= 337.5:
        return 'northwest'


def get_traffic_condition():
    # Create bounding box for traffic api
    # latitude and longitute of Monterey center
    latitude = 36.585748570870585
    longitude = -121.91417070420516
    # Km distance: 100km
    offset = (1.0 / 1000.0) * 100

    north = round(latitude + offset, 3)
    south = round(latitude - offset, 3)
    lngOffset = offset * math.cos(latitude * math.pi / 180.0)
    east = round(longitude + lngOffset, 3)
    west = round(longitude - lngOffset, 3)

    # Bing Map Conventions:
    severity_list = {"1": "Low Impact", "2": "Minor", "3": "Moderate", "4": "Serious"}
    type_list = {"1": "Accident", "2": "Congestion", "3": "DisabledVehicle", "4": "MassTransit", "5": "Miscellaneous",
                 "6": "OtherNews", "7": "PlannedEvent", "8": "RoadHazard", "9": "Construction", "10": "Alert",
                 "11": "Weather"}
    road_info = {"True": "Closed", "False": "Open"}
    endpoint = "http://dev.virtualearth.net/REST/v1/Traffic/Incidents/" + str(south) + "," + str(west) + "," + str(
        north) + "," + str(east) + "?key=" + str(bing_key)

    try:
        r = requests.get(endpoint)
        data = r.json()
        description = data['resourceSets'][0]['resources'][0]['description']
        sev = data['resourceSets'][0]['resources'][0]['severity']
        severity = severity_list[str(sev)]
        inc_type = data['resourceSets'][0]['resources'][0]['type']
        incident_type = type_list[str(inc_type)]
        road = data['resourceSets'][0]['resources'][0]['roadClosed']
        road_closed = road_info[str(road)]
        return {"description": description, "severity": severity, "incident_type": incident_type,
                "road_closed": road_closed}
    except:
        print('failed')