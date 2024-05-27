import requests


def get_cart(telegram_id: str) -> dict:
    url = 'http://127.0.0.1:8000/api/v1/cart'
    data = {'telegram_id': telegram_id}
    r = requests.post(url, data)
    if r.status_code == 200:
        return r.json()
