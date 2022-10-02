from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.utils.markdown import hcode

from loader import dp

COMMANDS = {'help': 'Эта справка',
            'token': 'Привязать аккаунт',
            }


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "Список команд:\n"
    for command, descr in COMMANDS.items():
        text += f'\t{hcode("/" + command)} - {descr}' + '\n'
    await message.answer(text)
