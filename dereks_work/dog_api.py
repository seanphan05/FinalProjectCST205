import requests

def get_dog_url():
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    if response.status_code == 200:

        print(response)
        print(response.json())

        return response.json().get('message')

    else:
        print(f'Something went wrong: Status code {response.status_code}')

        return str(response.status_code)

if __name__ == '__main__':
    get_dog_url()
