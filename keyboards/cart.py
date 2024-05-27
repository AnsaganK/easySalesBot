from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TelegramEmoji
from filters.cart import ConfirmAddCartCallbackFactory
from filters.product import ProductQuantityCallbackFactory, ProductAddCartCallbackFactory
from network.cart import get_cart


def generate_confirm_cart_keyboard(product_id, name, slug, quantity) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=f'{TelegramEmoji.BACK}',
        callback_data=ProductQuantityCallbackFactory(product_id=product_id, name=name, slug=slug, quantity=quantity)
    )
    builder.button(
        text=f'{TelegramEmoji.CHECK}',
        callback_data=ConfirmAddCartCallbackFactory(product_id=product_id, name=name, slug=slug, quantity=quantity)
    )
    builder.adjust(2)
    return builder.as_markup()


def generate_cart_items_keyboard(cart_items: list):
    builder = InlineKeyboardBuilder()
    for item_index, item in enumerate(cart_items, start=1):
        builder.button(
            text=f'{item_index}. {item.get("product").get("name")} * {item.get("quantity")} шт.',
            callback_data=ConfirmAddCartCallbackFactory(product_id=1, name='', slug='', quantity=1)  # draft

        )
    builder.adjust(1)
    return builder.as_markup()
