from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TelegramEmoji
from filters.product import ProductCallbackFactory, ProductQuantityCallbackFactory, ProductAddCartCallbackFactory
from network.product import get_products


def generate_products_keyboard(slug) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    products: dict = get_products(slug).get('results')
    for product in products:
        builder.button(
            text=f'{product.get("name")} - {product.get("price")} Р.',
            callback_data=ProductCallbackFactory(product_id=product.get('id'), name=product.get("name"),
                                                 slug=product.get("slug")),
        )
    builder.adjust(2)
    return builder.as_markup()


def generate_product_keyboard(product_id: int, name: str, slug: str, quantity: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="-", callback_data=ProductQuantityCallbackFactory(product_id=product_id, name=name, slug=slug,
                                                                          quantity=quantity - 1))
    builder.button(
        text=f"{quantity}",
        callback_data=ProductQuantityCallbackFactory(product_id=product_id, name=name, slug=slug, quantity=quantity)
    )
    builder.button(
        text="+",
        callback_data=ProductQuantityCallbackFactory(
            product_id=product_id, name=name, slug=slug, quantity=quantity + 1
        )
    )

    builder.button(
        text=f"{TelegramEmoji.CART} в Корзину",
        callback_data=ProductAddCartCallbackFactory(product_id=product_id, name=name, slug=slug, quantity=quantity)
    )
    builder.button(
        text=f"{TelegramEmoji.STAR} в Избранное", callback_data="category_list"
    )
    builder.adjust(3, 1, 1)

    return builder.as_markup()
