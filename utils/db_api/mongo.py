import logging

import pymongo
from accessify import private
from bson.objectid import ObjectId
from pymongo.collection import Collection

from data.config import MONGO_CONNECTION_STRING

TELETOKEN_COLLECTION = 'teletokens'


class Database:
    __instance = None

    @private
    def __init__(self, db):
        if not Database.__instance:
            print("init")
            self.db = db

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            logging.info("Connection to mongo")
            client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
            logging.info("Connected to mongo " + str(client))
            logging.info("Connected to allconnect db " + str(client['allconnect']))
            cls.__instance = Database(client['allconnect'])
        return cls.__instance

    def get_token_collection(self) -> Collection:
        return self.db[TELETOKEN_COLLECTION]

    def check_token(self, token):
        try:
            collection = self.get_token_collection().find_one({"_id": ObjectId(token)})
            return collection is not None
        except Exception as err:
            logging.error(err)

    def set_user_id_for_token(self, token, user_id):
        try:
            self.get_token_collection().update_one(
                {"_id": ObjectId(token)},
                {"$set": {
                    "telegramUser": user_id
                }})
        except Exception as err:
            logging.error(err)

    def check_user(self, user_id):
        try:
            collection = self.get_token_collection().find_one({"telegramUser": str(user_id)})
            return collection is not None
        except Exception as err:
            logging.error(err)

    def get_user(self, user_id):
        try:
            collection = self.get_token_collection().find_one({"telegramUser": str(user_id)})
            return self.db['users'].find_one({"_id": ObjectId(collection["user"])})
        except Exception as err:
            logging.error(err)
