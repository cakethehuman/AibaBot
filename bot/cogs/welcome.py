import logging

import discord
from discord.ext import commands
from ..core.config import settings
from ..services.outputformat import make_output

logger = logging.getLogger(__name__)
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot  = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel_id = settings.WELCOME_CHANNEL_ID
        channel = self.bot.get_channel(channel_id)
        logger.info(f"A member has joined")
        if channel is None:
            try:
                channel = await self.bot.fetch_channel(channel_id)
            except Exception as e:
                logger.info(f"error : {e}")
                return
            
        title = f"🌸 Yaharoo! Selamat datang, {member.display_name} Senpai~ (≧▽≦)!"
        description = ("Aku **AIBA**! 🌟 Maskot utama Soushin yang bakal setia menemani\n"
                        "dan bantuin kamu di server ini! Hehe~ ( ˶ˆ꒳ˆ˵ ) \n\n"
                        "✨ *Pstt...* Gunakan command `/help` yaa untuk mengetahui command lain...."
                        )
        ping_msg = await channel.send(member.mention)
        embed = make_output(title,description)
        await channel.send(embed=embed)
        await ping_msg.delete()
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))
    logger.info("Welcome cog loaded")
    
