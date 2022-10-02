from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        # user = await select_user(message.from_user.id)
        # return user and user.is_admin
        return True
