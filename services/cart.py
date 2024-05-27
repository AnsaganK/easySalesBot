from aiogram.enums import ParseMode
from aiogram.types import Message

from keyboards.cart import generate_cart_items_keyboard
from network.cart import get_cart


async def send_cart_data(message: Message, user_id: str):
    cart_data = get_cart(user_id)
    total_sum = cart_data.get("total_sum")
    cart_items = cart_data.get("items", [])
    keyboard = generate_cart_items_keyboard(cart_items)
    await message.answer(
        text=f'<b>Ваша корзина</b>\nТоваров: {len(cart_items)}\nОбщая сумма: {total_sum} рублей',
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
