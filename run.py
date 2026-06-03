# run.py
import asyncio
from SHUKLAMUSIC import init

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
