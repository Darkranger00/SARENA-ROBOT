import asyncio
import sys
import logging as log
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Naina import MONGO_DB_URI
from Naina.confing import get_int_key, get_str_key


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["Naina"]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("ᴄᴀɴ'ᴛ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴍᴏɴɢᴏᴅʙ! ᴇxɪᴛɪɴɢ. ʙʏʏʏ ..."))
