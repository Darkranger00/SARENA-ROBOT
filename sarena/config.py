import json
from os import getenv

def get_user_list(config, key):
    with open("{}/EmikoRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    API_ID = 8289355  # integer value, dont use ""
    API_HASH = "55822f9d50c5b011177539545f760852"
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1962673406  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OPENWEATHERMAP_ID = 22322
    OWNER_USERNAME = "cute_boy701"
    BOT_USERNAME = "psycho_bbot"
    BOT_ID = ""
    SUPPORT_CHAT = "TERAYAARHOOMAI"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001554007729
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001554007729
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOG = -1001554007729

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = ""  # needed for any database modules
    MONGO_DB_URI = str("")  # needed for any database modules
    REDIS_URL = ""  # NEEDED FOR AFK AND APPROVAL MODULES
    ARQ_API_URL = "http://arq.hamker.in"
    ARQ_API_KEY = "RRWNKD-BWGWQG-ARPLYD-YHFSYM-ARQ"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1962673406"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1962673406"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1962673406"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1962673406"
    WOLVES = "1962673406"
    DONATION_LINK = "https://t.me/oye_golgappu"  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = "siap"
    HEROKU_API_KEY = "YES"
    REM_BG_API_KEY = "FJxkbrJNx7SfffHPyjAs3A3z"
    LASTFM_API_KEY = "yeah"
    CF_API_KEY = "jk"
    BL_CHATS = []  # List of groups that you want blacklisted.
    SESSION_STRING = "12342"
    STRING_SESSION = ""
    MONGO_PORT = int("27017")
    MONGO_DB = "Naina"

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
