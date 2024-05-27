from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from filters.category import CategoryCallbackFactory, SubCategoryCallbackFactory
from network import get_categories, get_category


def generate_categories_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    categories: dict = get_categories()
    for category in categories:
        builder.button(
            text=category.get('name'),
            callback_data=CategoryCallbackFactory(name=category.get('name'), slug=category.get('slug'))
        )
    builder.adjust(2)
    return builder.as_markup()


def generate_subcategories_keyboard(slug) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    subcategories: dict = get_category(slug).get('subcategories')
    for subcategory in subcategories:
        builder.button(
            text=f'{subcategory.get("name")} ({subcategory.get("product_count")})',
            callback_data=SubCategoryCallbackFactory(name=subcategory.get('name'), slug=subcategory.get('slug'))
        )
    builder.adjust(3)

    return builder.as_markup()
