import discord
from discord.ext import commands
from ..core.config import Settings

class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot  = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = Settings.WELCOME_CHANNEL_ID
        channel = self.bot.get_channel(channel_id)
        
        if channel:
            await channel.send(f"Selamat datang {member.mention}")
        else:
            print("Channel not found")
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))