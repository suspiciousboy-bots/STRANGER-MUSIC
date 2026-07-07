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
import asyncio
import importlib
import os
import time
from pyrogram.errors import FloodWait
from SHUKLAMUSIC import LOGGER, app, userbot, call
from SHUKLAMUSIC.core.bot import bot
from SHUKLAMUSIC.misc import dbb, sudo, heroku
from SHUKLAMUSIC.core.git import git
import config

# Start time
START_TIME = time.time()

async def init():
    try:
        # Add delay to prevent rate limiting on Railway
        LOGGER(__name__).info("⏳ Waiting 10 seconds before starting...")
        await asyncio.sleep(10)
        
        # Load database
        dbb()
        
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
        
        # Load sudo users
        await sudo()
        
        # Start bot
        LOGGER(__name__).info("🤖 Starting Bot...")
        await app.start()
        
        # Start userbot (assistant)
        LOGGER(__name__).info("👤 Starting Userbot...")
        await userbot.start()
        
        # Start voice calls
        LOGGER(__name__).info("🎵 Starting Voice Calls...")
        await call.start()
        
        # Load all plugins
        LOGGER(__name__).info("📦 Loading Plugins...")
        all_modules = ""
        plugins_path = "SHUKLAMUSIC/plugins"
        
        if os.path.exists(plugins_path):
            for module in os.listdir(plugins_path):
                if module.endswith(".py") and module != "__init__.py":
                    module_name = module[:-3]
                    all_modules += f"SHUKLAMUSIC.plugins.{module_name}, "
                    try:
                        importlib.import_module(f"SHUKLAMUSIC.plugins.{module_name}")
                    except Exception as e:
                        LOGGER(__name__).warning(f"⚠️ Failed to load plugin {module_name}: {e}")
        
        if all_modules:
            LOGGER(__name__).info(f"✅ Loaded Modules: {all_modules[:-2]}")
        else:
            LOGGER(__name__).info("✅ No plugins found to load")
        
        # Send startup message to log group
        try:
            await app.send_message(
                config.LOG_GROUP_ID,
                f"✅ **{config.BOT_NAME} Started Successfully!**\n\n"
                f"• **Bot:** @{config.BOT_USERNAME}\n"
                f"• **Owner:** @{config.OWNER_USERNAME}\n"
                f"• **Started at:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"• **Platform:** Railway\n"
                f"• **Status:** 🟢 Online"
            )
        except Exception as e:
            LOGGER(__name__).warning(f"⚠️ Could not send startup message: {e}")
        
        LOGGER(__name__).info(f"🎵 {config.BOT_NAME} Started Successfully!")
        
    except FloodWait as e:
        wait_time = e.x
        LOGGER(__name__).warning(f"⚠️ FloodWait: Telegram says wait {wait_time} seconds")
        LOGGER(__name__).info(f"⏳ Sleeping for {wait_time} seconds...")
        await asyncio.sleep(wait_time)
        LOGGER(__name__).info("🔄 Retrying after FloodWait...")
        await init()
        
    except Exception as e:
        LOGGER(__name__).error(f"❌ Error during initialization: {e}")
        LOGGER(__name__).info("🔄 Retrying in 60 seconds...")
        await asyncio.sleep(60)
        await init()


async def shutdown():
    LOGGER(__name__).info("🛑 Shutting down...")
    try:
        await app.stop()
        await userbot.stop()
        await call.stop()
        LOGGER(__name__).info("✅ Shutdown complete!")
    except Exception as e:
        LOGGER(__name__).error(f"❌ Error during shutdown: {e}")


async def main():
    try:
        await init()
        
        # Keep the bot running
        while True:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        await shutdown()
    except Exception as e:
        LOGGER(__name__).error(f"❌ Fatal error: {e}")
        await shutdown()


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        LOGGER(__name__).error(f"❌ Fatal error: {e}")
