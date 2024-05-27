from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TelegramEmoji
from filters.product import ProductCallbackFactory, ProductQuantityCallbackFactory
from network.product import get_products


def generate_confirm_cart_keyboard(slug) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=f'{TelegramEmoji.X}',
        callback_data=ProductQuantityCallbackFactory(name='', slug=slug, quantity=1) # draft
    )
    builder.button(
        text=f'{TelegramEmoji.CHECK}',
        callback_data=ProductQuantityCallbackFactory(name='', slug=slug, quantity=1) # draft
    )
    builder.adjust(2)
    return builder.as_markup()
