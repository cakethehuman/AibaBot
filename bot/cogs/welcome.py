import json

import logging

import discord
from discord.ext import commands
from bot.core.config import settings

logger = logging.getLogger(__name__)
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot  = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        server = member.guild
        
        channel_id = settings.WELCOME_CHANNEL_ID
        channel = self.bot.get_channel(channel_id)
        logger.info(f"A member has joined {member.name}")
        if channel is None:
            try:
                channel = await self.bot.fetch_channel(channel_id)
            except Exception as e:
                logger.info(f"error : {e}")
                return
          
        embed = discord.Embed(
            description= f"Let's greet our new friend, {member.mention}! ようこそ〜！🌸\n⛩️ **Welcome to Soushin: Tarumanagara Nihon Bu!**\nYaharoo, Senpai (≧▽≦)!\nAku AIBA! Maskot utama Soushin yang bakal menemani kamu selama berada di server ini! Hehe, yoroshiku! ( ˶ˆ꒳ˆ˵ )\n﹌﹌﹌﹌﹌﹌﹌﹌\n🪷 Baca ⁠<#1149355230912323585> dan ngobrol di ⁠<#1149357512143945828>!\n🌻 Kunjungi <#1543187478595506258> dan ceritakan tentang dirimu! ♡\n\n(˶˃𐃷˂˶) HMmm... Mau tauu lebih jauh tentang Soushin  :o? Sini AIBA ajarin! \n🌹Cek `/soushin` untuk mengenal UKM dan hal-hal yang ada di dalamnya!\n⛩️ Penasaran Soushin punya kegiatan apa aja? Gunakan `/proker` untuk melihat berbagai program kerja Soushin!\n🛠️ Butuh bantuan? Gunakan `/help` untuk melihat command yang tersedia dan mengetahui apa saja yang bisa kamu lakukan di server ini!\n-# Psst... coba `/help` dulu yaa, biar nggak tersesat! Ი𐑼\n\n",
            color=16727604
        )  
        
        embed.set_author(name=server.name, icon_url=server.icon.url)
        embed.set_thumbnail(url = member.display_avatar.url if server.icon else None)
        embed.set_footer(
            text=f"Kamu adalah member soushin ke-{server.member_count}! Sugoi! (˶˃ ᵕ ˂˶)",
            icon_url=member.display_avatar.url,
        )
        
        content = f'Welcome, {member.mention}!'
        
        await channel.send(content=content,embed=embed)

        
async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))
    logger.info("Welcome cog loaded")
    
