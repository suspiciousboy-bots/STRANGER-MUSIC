# config.py
import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Required
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Owner & Bot Info
OWNER_ID = int(getenv("OWNER_ID", 7790607144))
OWNER_USERNAME = getenv("OWNER_USERNAME", "OfficiallyCrazyBoy07")
BOT_USERNAME = getenv("BOT_USERNAME", "SonamxMusic_bot")
BOT_NAME = getenv("BOT_NAME", "─˹ 𝘚𝘰𝘯𝘢𝘮 ✗ 𝘔𝘶𝘴𝘪𝘤 ˼─")
ASSUSERNAME = getenv("ASSUSERNAME", "SonamxAssistant")

# Logging
LOGGER_ID = int(getenv("LOGGER_ID", -1003401639448))
LOG_GROUP_ID = -1003401639448

# Debug
DEBUG_IGNORE_LOG = getenv("DEBUG_IGNORE_LOG", True)

# Session Strings
STRING_SESSION = getenv("STRING_SESSION", None)
STRING_SESSION2 = getenv("STRING_SESSION2", None)
STRING_SESSION3 = getenv("STRING_SESSION3", None)
STRING_SESSION4 = getenv("STRING_SESSION4", None)
STRING_SESSION5 = getenv("STRING_SESSION5", None)

# Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# Assistant Settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
ASSISTANT_LEAVE_TIME = int(getenv("ASSISTANT_LEAVE_TIME", 9000))

# Support & Social
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CrazyyCore")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+Fgx6_JRTLkFjMjE1")
INSTAGRAM = getenv("INSTAGRAM", "https://instagram.com/yaduwanshi_nand")
YOUTUBE = getenv("YOUTUBE", "https://youtube.com/@NandEditz")
GITHUB = getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = getenv("DONATE", "https://t.me/PikachuBots/91")
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://i.ibb.co/Y4S2BqzS/file-127.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://i.ibb.co/hJqZFsDq/file-128.jpg")
PLAYLIST_IMG_URL = "https://i.ibb.co/zHxhxwBS/file-129.jpg"
STATS_IMG_URL = "https://i.ibb.co/Y4S2BqzS/file-127.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/JWSQ6MGL/file-130.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/sdQ4JD18/file-131.jpg"
STREAM_IMG_URL = "https://i.ibb.co/NnG7CqQm/file-132.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/JWDVyMVj/file-133.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/HpnxqJmW/file-134.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/ccnMkytM/file-135.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/FqJMHkTS/file-136.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/YBv9W98j/file-138.jpg"

# SHASHANK Images
SHASHANK_IMG = [
    "https://i.ibb.co/Y4S2BqzS/file-127.jpg",
    "https://i.ibb.co/hJqZFsDq/file-128.jpg",
    "https://i.ibb.co/zHxhxwBS/file-129.jpg",
    "https://i.ibb.co/JWSQ6MGL/file-130.jpg",
    "https://i.ibb.co/sdQ4JD18/file-131.jpg",
    "https://i.ibb.co/NnG7CqQm/file-132.jpg",
    "https://i.ibb.co/JWDVyMVj/file-133.jpg",
    "https://i.ibb.co/HpnxqJmW/file-134.jpg",
    "https://i.ibb.co/ccnMkytM/file-135.jpg",
    "https://i.ibb.co/FqJMHkTS/file-136.jpg",
    "https://i.ibb.co/YBv9W98j/file-138.jpg"
]

# Helper function
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
