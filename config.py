# config.py
import os
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Required credentials
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Bot and owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "OfficiallyCrazyBoy07")
BOT_USERNAME = getenv("BOT_USERNAME", "SonamxMusic_bot")
BOT_NAME = getenv("BOT_NAME", "˹ 𝐒ᴏɴᴀᴍ ꭙ 𝐌ᴜꜱɪᴄ ♪˼ [ ɴᴏ ᴀᴅꜱ ]")
ASSUSERNAME = getenv("ASSUSERNAME", "Somewhere_Yours")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Limits and IDs
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
LOGGER_ID = int(getenv("LOGGER_ID", -1003401639448))
LOG_GROUP_ID = -1003401639448
OWNER_ID = int(getenv("OWNER_ID", 7790607144))

# Heroku (MUST HAVE THESE EVEN IF EMPTY)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/NoxxOP/PikachuMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CrazyyCore")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Fgx6_JRTLkFjMjE1")

# Social Links
INSTAGRAM = getenv("INSTAGRAM", "https://instagram.com/yaduwanshi_nand")
YOUTUBE = getenv("YOUTUBE", "https://youtube.com/@NandEditz")
GITHUB = getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = getenv("DONATE", "https://t.me/PikachuBots/91")
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# Assistant settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
ASSISTANT_LEAVE_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Song download limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "2145386496"))

# Session strings
STRING_SESSION = getenv("STRING_SESSION", None)
STRING_SESSION2 = getenv("STRING_SESSION2", None)
STRING_SESSION3 = getenv("STRING_SESSION3", None)
STRING_SESSION4 = getenv("STRING_SESSION4", None)
STRING_SESSION5 = getenv("STRING_SESSION5", None)

# Miscellaneous
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"
DEBUG_IGNORE_LOG = getenv("DEBUG_IGNORE_LOG", True)

###### IMAGE URLS ######

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

# Random image collection
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
    """Convert time string (MM:SS) to total seconds."""
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

# Calculate total duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is invalid. It must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is invalid. It must start with https://")
