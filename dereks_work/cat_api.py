import requests

query = {'x-api-key':'9520ad95-23c2-4ad2-accf-5b0aae2d3c41'}
# We understand leaving an API key out like this is bad practice, but given how much of a pain using
# something like github secrets or using gitignore to hide a folder with API keys in it, this is fine 

def get_cat_url():
    """
    This function makes an API request and returns a URL for a random image of a cat
    """
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url, params=query) # making API request

    # If the api request was successful, return the URL for the cat image
    if response.status_code == 200:
        return response.json()[0].get('url')

    # If the api went wrong, print out an error and return the status code
    else:
        print(f'Something went wrong: Status code {response.status_code}')
        return str(response.status_code)

if __name__ == '__main__':
    print(get_cat_url())
