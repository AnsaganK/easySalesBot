from aiogram import types
from aiogram.enums import ChatMemberStatus
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import CHANNEL_ID, GROUP_ID, TelegramEmoji


async def is_subscriber_user(message: Message) -> bool:
    bot = message.bot
    user_id = message.from_user.id

    user_channel = await bot.get_chat_member(chat_id=f'@{CHANNEL_ID}', user_id=user_id)
    user_group = await bot.get_chat_member(chat_id=f'@{GROUP_ID}', user_id=user_id)

    is_subscribe_channel: bool = user_channel.status != ChatMemberStatus.LEFT
    is_subscribe_group: bool = user_group.status != ChatMemberStatus.LEFT
    if not is_subscribe_channel or not is_subscribe_group:
        subscribe_builder = InlineKeyboardBuilder()
        subscribe_builder.row(types.InlineKeyboardButton(
            text=f"{TelegramEmoji.CHECK if is_subscribe_channel else TelegramEmoji.X} Канал",
            url=f"t.me/{CHANNEL_ID}")
        )
        subscribe_builder.row(types.InlineKeyboardButton(
            text=f"{TelegramEmoji.CHECK if is_subscribe_group else TelegramEmoji.X} Группа",
            url=f"t.me/{GROUP_ID}")
        )
        await message.answer(
            'Подпишитесь на нашу группу и канал',
            reply_markup=subscribe_builder.as_markup(),
        )
        return False
    return True
