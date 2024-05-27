from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from filters.cart import ConfirmAddCartCallbackFactory
from keyboards.cart import generate_cart_items_keyboard
from network.cart import get_cart
from network.product import add_to_cart
from services.cart import send_cart_data

router = Router()


@router.callback_query(ConfirmAddCartCallbackFactory.filter())
async def add_product(
        callback: types.CallbackQuery,
        callback_data: ConfirmAddCartCallbackFactory
):
    product_id = callback_data.product_id
    name = callback_data.name
    slug = callback_data.slug
    quantity = callback_data.quantity

    data = {
        'product': product_id,
        'quantity': quantity,
        'telegram_id': callback.from_user.id,
    }
    response = add_to_cart(data)
    await callback.message.edit_text(
        text=f'{response.get("message", "Серверная ошибка")}',
        parse_mode=ParseMode.HTML
    )


@router.message(Command('cart'))
async def my_cart_command(message: Message):
    await send_cart_data(message, str(message.from_user.id))


@router.callback_query(F.data == "my_cart")
async def my_cart(callback: types.CallbackQuery):
    await send_cart_data(callback.message, str(callback.from_user.id))
