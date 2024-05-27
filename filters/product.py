from aiogram.filters.callback_data import CallbackData


class ProductCallbackFactory(CallbackData, prefix="product"):
    product_id: int = None
    name: str = None
    slug: str = None


class ProductQuantityCallbackFactory(CallbackData, prefix="quantity"):
    product_id: int = None
    name: str = None
    slug: str = None
    quantity: int = 1


class ProductAddCartCallbackFactory(CallbackData, prefix="cart"):
    product_id: int = None
    name: str = None
    slug: str = None
    quantity: int = 1
