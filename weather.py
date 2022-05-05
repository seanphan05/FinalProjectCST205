import requests
api_key = '5758fb87d0125025a8e357c34f764643'
def get_monterey_weather():
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    coords = get_monterey_coords()
    
    payload = {
        'appid' : api_key,
        'units' : 'imperial',
        'lat' : coords['lat'],
        'lon' : coords['lon']
    }
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        data['wind']['dir'] = get_wind_direction(data)
        data['weather'][0]['description'] = data['weather'][0]['description'].title()
        # print(data)
        return data
    except:
        print('failed')
def get_monterey_coords():
    endpoint = 'http://api.openweathermap.org/geo/1.0/direct'
    
    payload = {
        'q' : 'Monterey,CA,US',
        'appid' : api_key,
        'limit' : 1
    }

    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        return {'lat': data[0]['lat'], 'lon' : data[0]['lon']}
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