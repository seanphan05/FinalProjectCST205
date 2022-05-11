import requests

#curl --location --request GET 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10'

def get_crypto_from_USD(usd_price: int):

    coins_per_USD = []

    response = requests.get('https://api.coinstats.app/public/v1/coins?skip=0&limit=4&currency=USD')

    if response.status_code == 200:

        response_results = response.json()

        for _, val in response_results.items():
            for coin in val:
                coins_per_USD.append({coin['name']: coin['price'] * usd_price})

        return coins_per_USD
    else:
        print(f'Something went wrong: Status code {response.status_code}')

        return str(response.status_code)

if __name__ == '__main__':
    print(get_crypto_from_USD(50))