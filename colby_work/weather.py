import requests

def get_monterey_weather():
    api_key = '5758fb87d0125025a8e357c34f764643'
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'

    payload = {
        'appid' : api_key,
        'units' : 'imperial',
        'lat' : 36.6002,
        'lon' : -121.8947
    }

    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        # print(data)
        return data
    except:
        print('failed')
