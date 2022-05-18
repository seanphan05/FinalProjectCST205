import requests

def get_dog_url():
    """
    This function makes an API request and returns a URL for a random image of a dog
    """
    url = 'https://dog.ceo/api/breeds/image/random'

    response = requests.get(url) # Make an API request

    # If the api request was successful, return the URL for the dog image
    if response.status_code == 200:
        return response.json().get('message')

    # If the api went wrong, print out an error and return the status code
    else:
        print(f'Something went wrong: Status code {response.status_code}')
        return str(response.status_code)

if __name__ == '__main__':
    print(get_dog_url())
