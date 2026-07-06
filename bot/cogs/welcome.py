import logging

import discord
from discord.ext import commands
from ..core.config import settings

logger = logging.getLogger(__name__)
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot  = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel_id = settings.WELCOME_CHANNEL_ID
        channel = self.bot.get_channel(channel_id)
        logger.info(f"Test 123")
        if channel is None:
            try:
                channel = await self.bot.fetch_channel(channel_id)
            except discord.NotFound:
                logger.info(f"Ga bisa")
                return
        await channel.send("tesstttttttttttttttttttttttttttttt")
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))
    
