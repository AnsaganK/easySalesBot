from aiogram import Router, types
from aiogram.enums import ParseMode

from filters.cart import ConfirmAddCartCallbackFactory
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
