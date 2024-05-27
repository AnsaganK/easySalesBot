from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TelegramEmoji
from filters.product import ProductCallbackFactory, ProductQuantityCallbackFactory
from network.product import get_products


def generate_products_keyboard(slug) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    products: dict = get_products(slug).get('results')
    for product in products:
        builder.button(
            text=f'{product.get("name")} - {product.get("price")} Р.',
            callback_data=ProductCallbackFactory(name=product.get("name"), slug=product.get("slug")),
        )
    builder.adjust(2)
    return builder.as_markup()


def generate_product_keyboard(slug: str, quantity: int) -> InlineKeyboardMarkup:
    button1 = types.InlineKeyboardButton(
        text=f"{TelegramEmoji.CART} в Корзину", callback_data="category_list"
    )
    button2 = types.InlineKeyboardButton(
        text=f"{TelegramEmoji.STAR} в Избранное", callback_data="category_list"
    )

    button3 = types.InlineKeyboardButton(
        text="-", callback_data=ProductQuantityCallbackFactory.new(quantity=quantity - 1)
    )
    button4 = types.InlineKeyboardButton(
        text=f"{quantity}", callback_data=""
    )
    button5 = types.InlineKeyboardButton(
        text="+", callback_data=ProductQuantityCallbackFactory.new(quantity=quantity + 1)
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button3, button4, button5], [button1], [button2]])

    return markup
