import requests

# Example of making the API request from terminal
#curl --location --request GET 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10'

def get_current_crypto_prices():
    """
    Makes the API request to get the current prices for some crypto
    
    Returns:
        list(dict{ <crypto name (str)> : <value (float)> , ... })
    """
    coins_per_USD = []

    response = requests.get('https://api.coinstats.app/public/v1/coins?skip=0&limit=4&currency=USD')

    # If the response code worked
    if response.status_code == 200:
        response_results = response.json() 
        for _, val in response_results.items(): # Looping through all the crytpo amounts
            for coin in val:
                coins_per_USD.append({coin['name']: coin['price']}) # appending the name and amount to a list
        return coins_per_USD
    ### If there was an error, return the status code
    else:
        print(f'Something went wrong: Status code {response.status_code}')
        return str(response.status_code)

if __name__ == '__main__':
    print(get_current_crypto_prices())