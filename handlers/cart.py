from aiogram import Router, types, F
from aiogram.enums import ParseMode

from filters.cart import ConfirmAddCartCallbackFactory
from keyboards.cart import generate_cart_items_keyboard
from network.cart import get_cart
from network.product import add_to_cart

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


@router.callback_query(F.data == "cart")
async def category_list(callback: types.CallbackQuery):
    cart_data = get_cart(str(callback.from_user.id))
    total_sum = cart_data.get("total_sum")
    cart_items = cart_data.get("items", [])
    keyboard = generate_cart_items_keyboard(cart_items)
    await callback.message.answer(
        text=f'<b>Ваша корзина</b>\nТоваров: {len(cart_items)}\nОбщая сумма: {total_sum} рублей',
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
