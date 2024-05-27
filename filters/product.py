from aiogram.filters.callback_data import CallbackData


class ProductCallbackFactory(CallbackData, prefix="product"):
    name: str = None
    slug: str = None


class ProductQuantityCallbackFactory(CallbackData, prefix="quantity"):
    name: str = None
    slug: str = None
    quantity: int = 1


class ProductAddCartCallbackFactory(CallbackData, prefix="cart"):
    name: str = None
    slug: str = None
    quantity: int = 1
