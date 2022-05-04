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