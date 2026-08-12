import logging

import discord
from discord.ext import commands
from bot.core.config import settings
from bot.services.outputformat import make_output

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
            
        title = f"👋 Hey {member.display_name}, welcome to Soushin! ようこそ〜！ 🌸"

        description = (
            "⛩️ Welcome to Soushin: Tarumanagara Nihon Bu!\n"
            "Yaharoo! Senpai\\~ (≧▽≦)!\n"
            "Aku AIBA! ✨ Maskot utama Soushin yang bakal menemani kamu selama berada di server ini. Hehe\\~ ( ˶ˆ꒳ˆ˵ )\n\n"
            "📢 Here's what you need to know to get started:\n\n"
            "- 📖 Kenalan dengan Soushin\n"
            "  Mau tahu lebih jauh tentang Soushin? Cek /soushin untuk mengenal UKM dan hal-hal yang ada di dalamnya!\n"
            "- ⛩️ Lihat Program Kerja\n"
            "  Penasaran Soushin punya kegiatan apa aja? Gunakan /proker untuk melihat berbagai program kerja Soushin!\n"
            "- 🛠️ Butuh bantuan?\n"
            "  Gunakan /help untuk melihat command yang tersedia dan mengetahui apa saja yang bisa kamu lakukan di server ini!\n\n"
            "> Psst... coba /help dulu yaa, biar nggak tersesat\\~ (๑˃̵ᴗ˂̵)و\n\n"
            "🌸 Selamat bergabung di Soushin! Semoga betah dan have fun di sini!\n"
            "じゃあ、よろしくお願いします！ ✨"
        )
        
        embed = make_output(title,description)
        await channel.send(embed=embed)

        
async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))
    logger.info("Welcome cog loaded")
    
