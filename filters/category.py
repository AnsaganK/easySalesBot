from aiogram.filters.callback_data import CallbackData


class CategoryCallbackFactory(CallbackData, prefix="category"):
    name: str = None
    slug: str = None


class SubCategoryCallbackFactory(CallbackData, prefix="subcategory"):
    name: str = None
    slug: str = None
