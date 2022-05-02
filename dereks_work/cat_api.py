import requests

query = {'x-api-key':'9520ad95-23c2-4ad2-accf-5b0aae2d3c41'}

response = requests.get('https://api.thecatapi.com/v1/images/search', params=query)

if response.status_code == 200:

    print(response)
    print(response.json())

else:
    print(f'Something went wrong: Status code {response.status_code}')