import requests

query = {'x-api-key':'9520ad95-23c2-4ad2-accf-5b0aae2d3c41'} 
# Yeah I know showing API keys is bad. But going through the 
# hassle of github secrets or sharing the api keys in a seperate
# directory is just a pain in the butt for this assignment

def get_cat_url():
    """
    Example of an API result
    [{'breeds': [], 'id': 'MTY3MDk1MQ', 'url': 'https://cdn2.thecatapi.com/images/MTY3MDk1MQ.jpg', 'width': 1024, 'height': 768}]
    """
    response = requests.get('https://api.thecatapi.com/v1/images/search', params=query)

    if response.status_code == 200:

        print(response)
        print(response.json())

        return response.json()[0].get('url') # Returns the URL of the cat image

    else:
        print(f'Something went wrong: Status code {response.status_code}')

        return str(response.status_code)

if __name__ == '__main__':
    print(get_cat_url())
