import requests


def get_products(slug) -> dict:
    url = f"http://127.0.0.1:8000/api/v1/subcategory/{slug}/products"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()


def get_product(slug) -> dict:
    url = f"http://127.0.0.1:8000/api/v1/product/{slug}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
