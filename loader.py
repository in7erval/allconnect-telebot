import asyncio

from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.mongo import Database

# from utils.db_api.db_gino import db
# from utils.db_api.postgresql import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# SSL_CERT = open(WEBHOOK_SSL_CERT, 'rb').read()
# ssl_context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)

loop = asyncio.get_event_loop()
loop.run_until_complete(Database.create())

__all__ = ["bot", "storage", "dp"]
