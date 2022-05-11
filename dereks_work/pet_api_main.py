import numpy as np
try:
    from .cat_api import get_cat_url
    from .dog_api import get_dog_url
    from .test_data import cat_test_data, dog_test_data
    from .crypto_api import get_current_crypto_prices
except:
    from cat_api import get_cat_url
    from dog_api import get_dog_url
    from test_data import cat_test_data, dog_test_data
    from crypto_api import get_current_crypto_prices


cat_test_data_copy = cat_test_data.copy()
dog_test_data_copy = dog_test_data.copy()


def get_cat_dog_url_and_prices(size: int, use_test_data=True) -> list(list()):
    """
    This function will get us the URL's containing the animal images and some random USD value amount

    Args:
        size (int): The number of dog and cat URL's we want to get. Max size is 10
        use_test_data (bool): a boolean to use only the testing data instead of making API call. Used for testing and developement purposes. 

    Returns:
        list(list())
    """
    # Checking to make sure the user didn't enter in more than 10
    if size > 10:
        print('The most amount of API calls you can use in a single time is 10.\nChanging the size to 10...')
        size = 10

    # Saving the API results to a list
    api_results = []

    # Getting the current crypto prices
    crypto_prices = get_current_crypto_prices()

    # Randomly selects a dog or cat API
    for rand_val in np.random.choice([0,1], size=(size)):
        cur_api_result = {}
        random_pet_price = np.random.randint(1000) # 1000 dollars is the max pet price
        
        # 0 for cat API
        if rand_val == 0: 
            if use_test_data: # For testing purposes
                num_random_choice_left = len(cat_test_data_copy)
                random_test_choice = cat_test_data_copy[np.random.randint(num_random_choice_left)]
                animal_url = random_test_choice[0].get('url')
            else:
                print('Making cat API call')
                animal_url = get_cat_url()
        
        # 1 for dog api call
        if rand_val == 1: 
            if use_test_data:
                num_random_choice_left = len(dog_test_data_copy)
                random_test_choice = dog_test_data_copy[np.random.randint(num_random_choice_left)]
                animal_url = random_test_choice.get('message')
            else:
                print('Making dog API call')
                animal_url = get_dog_url()

        cur_api_result['url'] = animal_url
        cur_api_result['USD'] = random_pet_price

        # Converiting the random USD number to crptyo
        for crypto in crypto_prices:
            key, val = list(crypto.keys())[0], list(crypto.values())[0]
            cur_api_result[key] = val * random_pet_price

        # Adding the results to the total list    
        api_results.append(cur_api_result)

    return api_results

if __name__ == '__main__':

    results = get_cat_dog_url_and_prices(10)
    print(results)


