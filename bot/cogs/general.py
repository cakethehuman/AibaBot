import logging
import random
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands
from ..services.outputformat import make_output

logger = logging.getLogger(__name__)
class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Say hello to Aiba")
    async def hello_command(self, interaction: discord.Interaction):
        title = "🌸 Yaharoo! Selamat datang, Senpai~ (≧▽≦)"
        description = ("Aku **AIBA**! 🌟 Maskot utama Soushin yang bakal setia nemenin"
                        "dan bantuin kamu di server ini! Hehe~ ( ˶ˆ꒳ˆ˵ ) \n\n"
                        "✨ *Pstt...* Gunakan command `/help` yaa untuk mengetahui command lain...."
                        )
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="help", description="need help?")
    async def help_command(self, interaction: discord.Interaction):

        title = "🌸 こんにちは, Kamu bigung yaa ada command apa aja?! "
        
        description= (
            "sini aiba kasi paham (❁´◡`❁)"
        )

        embed = make_output(title,description)
        
        embed.add_field(
            name="**💬 ──────── General ────────**\n\n",
            value=  "• `/hello` — Kenalan dengan aiba 🌸.\n"
                    "• `/help` — Menampilkan daftar command pada server.\n"
                    "• `/about` — Informasi mengenai server.\n"
        )
        
        embed.add_field(
            name="**🦢 ──────── Soushin ────────**\n\n",
            value=  "• `/soushin` — Mengenali soushin 🌟.\n"
                    "• `/proker` — Proker aja saja yang ada di soushin.\n"
                    "• `/bph` — Struktur BPH.\n"
        )
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="about", description="Informasi mengenai server")
    async def about_command(self, interaction: discord.Interaction):

        title = "🌸 こんにちは, Selamat datang di Soushin! "
        
        description= (
            "Biar nggak nyasar, aiba udah buatin panduan singkat buat channel-channel di sini yaa~ (●'◡'●)"
        )

        embed = make_output(title,description)
        
        embed.add_field(
            name="💬 ──────── Sosial ────────",
            value=(
                "**<#1149357512143945828>** - Tempat ngobrol bareng\n"
                "**<#1149705399650484284>** - Pamerin makanan enak! 🍜\n"
                "**<#1150392131815489577>** - Pamerin pet kalian! 😺🐶\n"
                "**<#1149705265722171472>** - Sharing Foto 📸\n"
            ),
            inline=False
        )
        
        embed.add_field(
            name="☕ ──────── Soushin Cafe ────────",
            value=(
                "**<#1150389525441425468>** - Galeri buat pamer hasil karya seni kamu! 🎨 \n"
                "**<#1150424223995658362>** - Sharing tentang bahasa jepang 🗾\n"
                "**<#1150391779565240362>** - Tempat sharing foto cosplay 🪞\n"
                "**<#1150388138104066048>** - Tempat untuk artist ngobrol 🖼️\n"
                "**<#1155837776248446996>** - Main bot Mudae 🤖\n"
                "**<#1149726973644525710>** - Tempat puterin musik 🎵\n"
            ),
            inline=False
        )
        
        embed.add_field(
            name="🔊 ──────── Voice Chat ────────",
            value =( 
                "**<#1149705154422112256>** - Chat VC 💬\n"    
                "**<#1150389234826477598>** - VC artist 🔊\n"
                "**<#1150393560173125772>** - VC cosplay 🔊\n"
                "**<#1150742314013179915>** - Coffee shop 🔊\n"
                "**<#1150424179284377674>** - VC Bahasa 🔊\n"
                "**<#1216022911651942440>** - Random VC 🔊\n"
            ),
            inline = False
        )
        
        embed.add_field(
            name="🍡 ──────── Fandom ────────",
            value =( 
                "**<#1150390344916148236>** - Anime 🏯\n"    
                "**<#1150311053041868850>** - Genshin impact\n"
                "**<#1150311089825906750>** - Honkai: Star Rail\n"
                "**<#1150311370093502495>** - Wuthering Waves \n"
                "**<#1150430616437923982>** - Manga dan manhwa \n"
            ),
            inline = False
        )
        
        embed.add_field(
            name="👾 ──────── Gaming ────────",
            value =( 
                "**<#1289434009146753074>** - Gaming chat💬\n"    
                "**<#1150390653197488179>** - Gaming VC 1 🎮\n"
                "**<#1150390731337384017>** - Gaming VC 2 🎮\n"
                "**<#1150390772533841920>** - Gaming VC 3 🎮\n"
            ),
            inline = False
        )
        
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))