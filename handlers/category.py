from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.types import URLInputFile, FSInputFile

from config import LOGO_URL
from filters.category import CategoryCallbackFactory, SubCategoryCallbackFactory
from keyboards import generate_categories_keyboard, generate_subcategories_keyboard

router = Router()


@router.callback_query(F.data == "category_list")
async def category_list(callback: types.CallbackQuery):
    keyboard = generate_categories_keyboard()

    await callback.message.answer(
        text='Доступные категории',
        reply_markup=keyboard
    )


@router.callback_query(CategoryCallbackFactory.filter())
async def category_detail(
        callback: types.CallbackQuery,
        callback_data: CategoryCallbackFactory
):
    name = callback_data.name
    slug = callback_data.slug
    keyboard = generate_subcategories_keyboard(slug)
    await callback.message.edit_text(
        text=f'Категория <b>{name}</b>',
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
