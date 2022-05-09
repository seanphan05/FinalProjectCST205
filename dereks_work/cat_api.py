import requests

query = {'x-api-key':'9520ad95-23c2-4ad2-accf-5b0aae2d3c41'}

def get_cat_url():
    response = requests.get('https://api.thecatapi.com/v1/images/search', params=query)

    if response.status_code == 200:

        print(response)
        print(response.json())

        return response.json()[0].get('url')

    else:
        print(f'Something went wrong: Status code {response.status_code}')

        return str(response.status_code)

if __name__ == '__main__':
    print(get_cat_url())
