import requests

def get_dog_url():
    """
    Example of an API result
    {'message': 'https://images.dog.ceo/breeds/shihtzu/n02086240_5546.jpg', 'status': 'success'}
    """
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    if response.status_code == 200:

        print(response)
        print(response.json())

        return response.json().get('message')

    else:
        print(f'Something went wrong: Status code {response.status_code}')

        return str(response.status_code)

if __name__ == '__main__':
    print(get_dog_url())
