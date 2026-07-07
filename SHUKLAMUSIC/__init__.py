# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------
import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# Setup logging
LOG_FILE = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

LOGGER = logging.getLogger(__name__)

# Import config
try:
    import config
except ImportError as e:
    LOGGER(__name__).error(f"❌ Could not import config: {e}")
    sys.exit(1)

# Import core modules with error handling
try:
    from SHUKLAMUSIC.core.bot import SHUKLA
    from SHUKLAMUSIC.core.dir import dirr
    from SHUKLAMUSIC.core.git import git
    from SHUKLAMUSIC.core.userbot import Userbot
    from SHUKLAMUSIC.misc import dbb, heroku
except ImportError as e:
    LOGGER(__name__).error(f"❌ Could not import core modules: {e}")
    sys.exit(1)

# Initialize directories
try:
    dirr()
    LOGGER(__name__).info("✅ Directories initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ Could not initialize directories: {e}")

# Initialize database
try:
    dbb()
    LOGGER(__name__).info("✅ Database initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ Could not initialize database: {e}")

# Git operations - will skip if not in git repo
try:
    git()
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ Git operation skipped: {e}")

# Heroku operations - disabled for Railway
try:
    heroku()
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ Heroku operation skipped: {e}")

# Initialize bot and userbot
try:
    app = SHUKLA()
    LOGGER(__name__).info("✅ Bot initialized")
except Exception as e:
    LOGGER(__name__).error(f"❌ Could not initialize bot: {e}")
    sys.exit(1)

try:
    userbot = Userbot()
    LOGGER(__name__).info("✅ Userbot initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ Could not initialize userbot: {e}")
    userbot = None

# Initialize APIs
try:
    from SafoneAPI import SafoneAPI
    api = SafoneAPI()
    LOGGER(__name__).info("✅ API initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ Could not initialize API: {e}")
    api = None

# Initialize platforms
try:
    from .platforms import *
    Apple = AppleAPI()
    Carbon = CarbonAPI()
    SoundCloud = SoundAPI()
    Spotify = SpotifyAPI()
    Resso = RessoAPI()
    Telegram = TeleAPI()
    YouTube = YouTubeAPI()
    LOGGER(__name__).info("✅ Platforms initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ Could not initialize platforms: {e}")

APP = "InflexOwnerBot"  # connect music api key "Dont change it"

# Test MongoDB connection
try:
    from SHUKLAMUSIC.core.mongo import mongodb
    # Try to ping the database
    mongodb.command('ping')
    LOGGER(__name__).info("✅ MongoDB connection established")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ MongoDB connection failed: {e}")

LOGGER(__name__).info(f"🚀 Starting {config.BOT_NAME}...")
LOGGER(__name__).info(f"👤 Owner: @{config.OWNER_USERNAME}")
LOGGER(__name__).info(f"🤖 Bot: @{config.BOT_USERNAME}")
LOGGER(__name__).info(f"📦 Platform: Railway")
