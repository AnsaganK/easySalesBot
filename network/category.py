import requests


def get_categories() -> dict:
    url = "http://127.0.0.1:8000/api/v1/category"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()


def get_category(slug) -> dict:
    url = f"http://127.0.0.1:8000/api/v1/category/{slug}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
