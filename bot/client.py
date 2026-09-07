import logging
from pathlib import Path

import discord
from discord.ext import commands

from bot.cogs.general import RulesInfo
from bot.cogs.roles import KelasRolesButton
from bot.cogs.roles import AngkatanButton
from bot.cogs.roles import FakultasButton
from bot.cogs.roles import PronounsButton
from bot.cogs.roles import DmButton

from bot.core.config import settings

logger = logging.getLogger(__name__)


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(command_prefix="!unused", intents=intents)

    async def setup_hook(self):
        self.add_view(RulesInfo())
        self.add_view(KelasRolesButton())
        self.add_view(AngkatanButton())
        self.add_view(FakultasButton())
        self.add_view(PronounsButton())
        self.add_view(DmButton())
        logger.info("Persistent view 'Kelas Roles Button' has been registered.")
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