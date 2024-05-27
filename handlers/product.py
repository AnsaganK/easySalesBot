from typing import Union

from aiogram import Router, types
from aiogram.enums import ParseMode

from filters.category import SubCategoryCallbackFactory
from filters.product import ProductCallbackFactory, ProductQuantityCallbackFactory, ProductAddCartCallbackFactory
from keyboards.cart import generate_confirm_cart_keyboard
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
        callback_data: Union[ProductCallbackFactory, ProductQuantityCallbackFactory]
):
    name = callback_data.name
    slug = callback_data.slug
    if isinstance(callback_data, ProductCallbackFactory):
        keyboard = generate_product_keyboard(name, slug, 1)
        await callback.message.edit_text(
            text=f'<b>{name}</b>',
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML
        )
    elif isinstance(callback_data, ProductQuantityCallbackFactory):
        quantity = callback_data.quantity
        keyboard = generate_product_keyboard(name, slug, quantity)
        await callback.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(ProductAddCartCallbackFactory.filter())
async def add_cart(
        callback: types.CallbackQuery,
        callback_data: ProductAddCartCallbackFactory
):
    name = callback_data.name
    slug = callback_data.slug
    quantity = callback_data.quantity
    await callback.message.edit_text(
        text=f'<b>{name}</b>',
        reply_markup=generate_confirm_cart_keyboard(slug),
        parse_mode=ParseMode.HTML
    )
