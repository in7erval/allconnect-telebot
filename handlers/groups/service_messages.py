from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.group_chat import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Привет, {members}.")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} вышел из чата")
    elif message.from_user.id == (await bot.get_me()).id:
        return
    else:
        await message.reply(f"{message.left_chat_member.full_name} был удален из чата "
                            f"пользователем {message.from_user.get_mention(as_html=True)}")