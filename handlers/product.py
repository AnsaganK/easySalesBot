from aiogram import Router, types
from aiogram.enums import ParseMode

from filters.category import SubCategoryCallbackFactory
from filters.product import ProductCallbackFactory, ProductQuantityCallbackFactory
from keyboards.product import generate_products_keyboard, generate_product_keyboard

router = Router()


@router.callback_query(SubCategoryCallbackFactory.filter())
async def product_list(
        callback: types.CallbackQuery,
        callback_data: SubCategoryCallbackFactory
):
    name = callback_data.name
    slug = callback_data.slug
    keyboard = generate_products_keyboard(slug)
    await callback.message.edit_text(
        text=f'<b>{name}</b>',
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )


@router.callback_query(ProductQuantityCallbackFactory.filter())
@router.callback_query(ProductCallbackFactory.filter())
async def product_detail(
        callback: types.CallbackQuery,
        callback_data: ProductCallbackFactory
):
    name = callback_data.name
    slug = callback_data.slug
    keyboard = generate_product_keyboard(slug, 1)
    await callback.message.edit_text(
        text=f'<b>{name}</b>',
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
