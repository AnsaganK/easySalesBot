import requests


def create_user(user):
    url = 'http://127.0.0.1:8000/api/v1/user/create'
    data = {
        'telegram_id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        print(r.json())
    else:
        print(r.status_code)
