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
import time
from pyrogram import idle
from pyrogram.errors import FloodWait
from pytgcalls.exceptions import NoActiveGroupCall
import config
from SHUKLAMUSIC import LOGGER, app, userbot
from SHUKLAMUSIC.core.call import SHUKLA
from SHUKLAMUSIC.misc import sudo, heroku
from SHUKLAMUSIC.plugins import ALL_MODULES
from SHUKLAMUSIC.utils.database import get_banned_users, get_gbanned
from SHUKLAMUSIC.core.git import git


async def init():
    try:
        # Add delay to prevent rate limiting on Railway
        LOGGER(__name__).info("⏳ Waiting 10 seconds before starting...")
        await asyncio.sleep(10)
        
        # Check for string session
        if (
            not config.STRING1
            and not config.STRING2
            and not config.STRING3
            and not config.STRING4
            and not config.STRING5
        ):
            LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
            return
        
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
        
        # Load banned users
        try:
            users = await get_gbanned()
            for user_id in users:
                config.BANNED_USERS.add(user_id)
            users = await get_banned_users()
            for user_id in users:
                config.BANNED_USERS.add(user_id)
        except Exception as e:
            LOGGER(__name__).warning(f"⚠️ Could not load banned users: {e}")
        
        # Start bot
        LOGGER(__name__).info("🤖 Starting Bot...")
        await app.start()
        
        # Load all plugins
        for all_module in ALL_MODULES:
            try:
                importlib.import_module("SHUKLAMUSIC.plugins" + all_module)
            except Exception as e:
                LOGGER(__name__).warning(f"⚠️ Could not load plugin {all_module}: {e}")
        
        LOGGER("SHUKLAMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
        
        # Start userbot
        LOGGER(__name__).info("👤 Starting Userbot...")
        await userbot.start()
        
        # Start voice calls
        LOGGER(__name__).info("🎵 Starting Voice Calls...")
        await SHUKLA.start()
        
        # Stream startup video
        try:
            await SHUKLA.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
        except NoActiveGroupCall:
            LOGGER("SHUKLAMUSIC").error(
                "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧/𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
            )
            await app.stop()
            await userbot.stop()
            return
        except Exception as e:
            LOGGER(__name__).warning(f"⚠️ Could not stream startup video: {e}")
        
        # Load decorators
        try:
            await SHUKLA.decorators()
        except Exception as e:
            LOGGER(__name__).warning(f"⚠️ Could not load decorators: {e}")
        
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
        
        LOGGER("SHUKLAMUSIC").info(
            "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 ⏤͟͞ 𝐂𝐑𝐀𝐙𝐘 𝐁𝐎𝐘 ᭄࿐\n╚═════ஜ۩۞۩ஜ════╝"
        )
        LOGGER(__name__).info(f"🎵 {config.BOT_NAME} Started Successfully!")
        
        # Keep bot running
        await idle()
        
        # Clean shutdown
        await app.stop()
        await userbot.stop()
        LOGGER("SHUKLAMUSIC").info("𝗦𝗧𝗢𝗣 𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")
        
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
        await SHUKLA.stop()
        LOGGER(__name__).info("✅ Shutdown complete!")
    except Exception as e:
        LOGGER(__name__).error(f"❌ Error during shutdown: {e}")


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(init())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        LOGGER(__name__).error(f"❌ Fatal error: {e}")
