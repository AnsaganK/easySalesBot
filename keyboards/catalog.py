from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from config import TelegramEmoji


def generate_catalog_keyboard() -> InlineKeyboardMarkup:
    button1 = types.InlineKeyboardButton(
        text=f"{TelegramEmoji.SHOP} Категории", callback_data="category_list"
    )
    button2 = types.InlineKeyboardButton(
        text=f"{TelegramEmoji.PERSON} Кабинет", callback_data="cabinet"
    )
    button3 = types.InlineKeyboardButton(
        text=f"{TelegramEmoji.CART} Корзина", callback_data="cart"
    )
    button4 = types.InlineKeyboardButton(
        text=f"{TelegramEmoji.STAR} Избранные", callback_data="favourite"
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button1], [button2], [button3, button4]])

    return markup
