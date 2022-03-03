import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = list(set(int(x) for x in os.environ.get("BOT_OWNER", "").split()))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = list(set(int(x) for x in os.environ.get("UPDATES_CHANNEL", "").split()))
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-100").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	HOME_TEXT = """
سلام [{}](tg://user?id={}) عزیز 🌸

من ربات آپلود اختصاصیه چنل [Hot Land 🏖](https://t.me/HotLandXD) هستم

خوش اومدی ❤️🔥
"""
