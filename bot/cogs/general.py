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
        title = "🌸 こんにちは!"
        description = ("私は **AIBA**! 🌟\n"
                       "Aku maskot utama shoushin yang siap membantu kamu di sever ini\n"
                        "Gunnakan command /help untuk liat semua command pada server"
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