import requests


def login(email, password):
    params = {'email': email, 'password': password}
    result = requests.post('http://127.0.0.1:5000/register', json=params)
    print(result)
    return result
