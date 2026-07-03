import random
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands
from ..services.outputformat import make_output

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Say hello to Aiba")
    async def hello_command(self, interaction: discord.Interaction):
        title = "🌸 こんにちわっっ、先輩ー！"
        description = ("Aku **AIBA**! 🌟 Maskot utama Soushin yang bakal setia nemenin "
                        "dan bantuin kamu di server ini! Hehe~ 0////0 \n\n"
                        "✨ *Pstt...* Gunakan command `/help` yaa untuk mengetahui command lain...."
                        )
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="help", description="need help?")
    async def help_command(self, interaction: discord.Interaction):

        title = "Slash Comamnds"
        
        description= (
            "**👋 General Commands**\n\n"
            "• `/hello` — Kenalan dengan aiba 🌸.\n"
            "• `/help` — Menampilkan daftar command pada server.\n"
            "• `/about` — Informasi mengenai server.\n"
            "**🦢 Soushin Commands**\n\n"
            "• `/soushin` — Pelajari apa itu Soushin.\n"
        )

        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="about", description="Informasi mengenai server")
    async def about_command(self, interaction: discord.Interaction):

        title = "🌸 こんにちは "
        
        description= (
            "Server shoushin lah intinya"
        )

        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="soushin", description="Informasi mengenai server")
    async def about_command(self, interaction: discord.Interaction):

        title = "🌸 こんにちは "
        
        description= (
            "Jelasin "
        )

        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))