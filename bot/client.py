import logging
from pathlib import Path

import discord
from discord.ext import commands

from bot.core.config import settings

logger = logging.getLogger(__name__)


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!unused", intents=intents)

    async def setup_hook(self):
        cogs_path = Path(__file__).parent / "cogs"
        for file in cogs_path.glob("*.py"):
            if file.stem == "__init__":
                continue
            extension = f"bot.cogs.{file.stem}"
            try:
                await self.load_extension(extension)
                logger.info(f"Loaded extension: {extension}")
            except Exception as e:
                logger.exception(f"Failed to load {extension}: {e}")

        if settings.DEV_GUILD_ID:
            guild = discord.Object(id=settings.DEV_GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            logger.info(f"Synced commands to guild {settings.DEV_GUILD_ID}")
        else:
            await self.tree.sync()
            logger.info("Synced commands globally")

    async def on_ready(self):
        logger.info(f"Logged in as {self.user} ({self.user.id})")