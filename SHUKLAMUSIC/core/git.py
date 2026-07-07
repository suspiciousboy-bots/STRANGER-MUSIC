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
import shlex
import os
from typing import Tuple
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
import config
import logging

# Get logger without circular import
LOGGER = logging.getLogger(__name__)


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    # Check if we are in a git repository
    if not os.path.exists(".git"):
        LOGGER.info("📦 Not a git repository - skipping git operations on Railway")
        return
    
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO
    
    try:
        repo = Repo()
        LOGGER.info(f"Git Client Found [VPS DEPLOYER]")
        
        # Fetch updates if on VPS
        try:
            origin = repo.remote("origin")
            origin.fetch()
            LOGGER.info(f"🔄 Fetching updates from upstream repository...")
        except GitCommandError as e:
            if "could not read Username" in str(e):
                LOGGER.warning("⚠️ Git authentication failed - skipping fetch")
            else:
                LOGGER.warning(f"⚠️ Git fetch error: {e}")
                
    except GitCommandError as e:
        LOGGER.warning(f"⚠️ Invalid Git Command: {e}")
        
    except InvalidGitRepositoryError:
        try:
            LOGGER.info(f"📦 Initializing git repository...")
            repo = Repo.init()
            
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            
            origin.fetch()
            repo.create_head(
                config.UPSTREAM_BRANCH,
                origin.refs[config.UPSTREAM_BRANCH],
            )
            repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
                origin.refs[config.UPSTREAM_BRANCH]
            )
            repo.heads[config.UPSTREAM_BRANCH].checkout(True)
            
            try:
                repo.create_remote("origin", config.UPSTREAM_REPO)
            except BaseException:
                pass
                
            nrs = repo.remote("origin")
            nrs.fetch(config.UPSTREAM_BRANCH)
            
            try:
                nrs.pull(config.UPSTREAM_BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
                
            install_req("pip3 install --no-cache-dir -r requirements.txt")
            LOGGER.info(f"✅ Git repository initialized successfully!")
            
        except GitCommandError as e:
            if "could not read Username" in str(e):
                LOGGER.warning("⚠️ Git authentication failed - skipping git operations")
            else:
                LOGGER.warning(f"⚠️ Git error: {e}")
                
        except Exception as e:
            LOGGER.warning(f"⚠️ Git initialization skipped: {e}")
            
    except Exception as e:
        LOGGER.warning(f"⚠️ Git operation skipped: {e}")
