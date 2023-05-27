import requests

host = 'family-clients.ru'
port = ''


def login(email, password) -> dict:
    params = {'email': email, 'password': password}
    result = requests.post(f'http://{host}{port}/login', json=params)
    return result.json()


def get_product_card(jwt) -> dict:
    headers = {'authorization': f'Bearer {jwt}'}
    result = requests.get(f'http://{host}{port}/api/cart', headers=headers)
    return result.json()


def create_product(jwt, name, description, image, price) -> dict:
    headers = {'authorization': f'Bearer {jwt}'}
    params = {
        'name': name,
        'description': description,
        'image': image,
        'price': price
    }

    result = requests.post(f'http://{host}{port}/api/cart', headers=headers, json=params)
    return result.json()
