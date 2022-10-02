from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink

from loader import dp
from states.RegisterToken import RegisterToken
from utils.db_api.mongo import Database

STOP_WORD = 'СТОП'


@dp.message_handler(Command('token'))
async def start_token(message: types.Message, state: FSMContext):
    if Database.get_instance().check_user(message.from_user.id):
        user = Database.get_instance().get_user(message.from_user.id)
        await message.answer(
            "Аккаунт " +
            hlink(f"{user['firstName']} {user['lastName']}", "https://allconnect.site/user" + str(user["_id"]))
            + " уже привязан")
    else:
        await message.answer("Пришли свой токен или 'СТОП' для отмены")
        await RegisterToken.Start.set()


@dp.message_handler(state=RegisterToken.Start)
async def receive_token(message: types.Message, state: FSMContext):
    token = message.text
    if token == STOP_WORD:
        await message.answer('Остановка')
        await state.reset_state(with_data=True)
        return
    if len(token) != 24:
        await message.answer('Это не похоже на токен... Длина токена 24 символа, попробуй ещё раз')
        return
    db = Database.get_instance()
    msg = await message.answer('Проверяем...')
    await msg.edit_text('Токен найден. Привязываем аккаунт...' if db.check_token(token) else 'Токен не найден')
    db.set_user_id_for_token(token, str(message.from_user.id))
    user = Database.get_instance().get_user(message.from_user.id)
    await msg.edit_text('Аккаунт ' +
                        hlink(f"{user['firstName']} {user['lastName']}",
                              "https://allconnect.site/user" + str(user["_id"])) +
                        ' привязан')
    await state.reset_state(with_data=True)
