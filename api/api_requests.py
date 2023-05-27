import requests

host = '127.0.0.1'
port = 8000


def login(email, password) -> dict:
    params = {'email': email, 'password': password}
    result = requests.post(f'http://{host}:{port}/login', json=params)
    return result.json()


# def get_product_list() -> dict:
#     return {}


def get_product_card(jwt) -> dict:
    params = {'authorization': f'Bearer {jwt}'}
    result = requests.post('http://{host}:{port}/api/cart', headers=params)
    return result.json()
