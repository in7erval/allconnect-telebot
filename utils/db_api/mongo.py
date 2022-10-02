import logging
from typing import Union

import pymongo

from data.config import MONGO_CONNECTION_STRING


class Database:

    def __init__(self, pool):
        self.pool = pool

    @classmethod
    async def create(cls):
        logging.info("Connection to mongo")
        client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        logging.info("Connected to mongo " + str(client))
        logging.info("Connected to allconnect db " + str(client['allconnect']))
        return cls(client['allconnect'])

    # async def execute(self, command, *args,
    #                   fetch: bool = False,
    #                   fetchval: bool = False,
    #                   fetchrow: bool = False,
    #                   execute: bool = False):
    #     async with self.pool.acquire() as connection:
    #         connection: Connection
    #         async with connection.transaction():
    #             if fetch:
    #                 result = await connection.fetch(command, *args)
    #             elif fetchval:
    #                 result = await connection.fetchval(command, *args)
    #             elif fetchrow:
    #                 result = await connection.fetchrow(command, *args)
    #             elif execute:
    #                 result = await connection.execute(command, *args)
    #         return result
    #
    # async def create_table_users(self):
    #     sql: str = ("CREATE TABLE IF NOT EXISTS users ("
    #                 "id SERIAL PRIMARY KEY,"
    #                 "full_name VARCHAR(255) NOT NULL,"
    #                 "username VARCHAR(255) NULL,"
    #                 "telegram_id BIGINT NOT NULL UNIQUE);")
    #     await self.execute(sql, execute=True)

    # @staticmethod
    # def format_args(sql, parameters: dict):
    #     sql += " AND ".join([
    #         f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
    #                                                       start=1)
    #     ])
    #     return sql, tuple(parameters.values())

    # async def add_user(self, full_name: str, username: str, telegram_id):
    #     sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
    #     return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)
    #
    # async def select_all_users(self):
    #     sql: str = "SELECT * FROM users"
    #     return await self.execute(sql, fetch=True)
    #
    # async def select_user(self, **kwargs):
    #     sql = "SELECT * FROM users WHERE "
    #     sql, parameters = self.format_args(sql, parameters=kwargs)
    #     return await self.execute(sql, *parameters, fetchrow=True)
    #
    # async def count_users(self):
    #     sql = "SELECT COUNT(*) FROM users"
    #     return await self.execute(sql, fetchval=True)
    #
    # async def update_user_username(self, username, telegram_id):
    #     sql = "UPDATE users SET username=$1 WHERE telegram_id=$2"
    #     await self.execute(sql, username, telegram_id, execute=True)
    #
    # async def delete_users(self):
    #     await self.execute("DELETE FROM users WHERE TRUE", execute=True)
    #
    # async def drop_users(self):
    #     await self.execute("DROP TABLE users", execute=True)
