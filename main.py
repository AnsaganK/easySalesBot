import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN, CHANNEL_ID, GROUP_ID, LOGO_FILE_ID
from handlers import category, product
from keyboards.catalog import generate_catalog_keyboard
from network.subscribe import is_subscriber_user
from network.user import create_user

# TOKEN = getenv("BOT_TOKEN")
TOKEN = BOT_TOKEN
CHANNEL_ID = CHANNEL_ID
GROUP_ID = GROUP_ID

dp = Dispatcher()
dp.include_routers(category.router)
dp.include_routers(product.router)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    is_subscriber = await is_subscriber_user(message)
    if is_subscriber:
        create_user(message.from_user)
        keyboard = generate_catalog_keyboard()
        await message.answer_photo(LOGO_FILE_ID, f'Добро пожаловать в EasySales', reply_markup=keyboard)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
