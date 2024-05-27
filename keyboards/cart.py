from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TelegramEmoji
from filters.cart import ConfirmAddCartCallbackFactory
from filters.product import ProductQuantityCallbackFactory, ProductAddCartCallbackFactory


def generate_confirm_cart_keyboard(product_id, name, slug, quantity) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=f'{TelegramEmoji.BACK}',
        callback_data=ProductQuantityCallbackFactory(product_id=product_id, name=name, slug=slug, quantity=quantity)
    )
    builder.button(
        text=f'{TelegramEmoji.CHECK}',
        callback_data=ConfirmAddCartCallbackFactory(product_id=product_id, name=name, slug=slug, quantity=quantity)  # draft
    )
    builder.adjust(2)
    return builder.as_markup()
