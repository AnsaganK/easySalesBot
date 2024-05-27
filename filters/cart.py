from aiogram.filters.callback_data import CallbackData


class ConfirmAddCartCallbackFactory(CallbackData, prefix="confirm_cart"):
    product_id: int = None
    name: str = None
    slug: str = None
    quantity: int = 1
