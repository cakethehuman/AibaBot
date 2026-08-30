import logging

import discord
from discord import app_commands
from discord.ext import commands

logger = logging.getLogger(__name__)
class Soushin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="soushin", description="Perkenalan tentang soushin")
    async def soushin_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description="Bot under contruction 🤖"
        )
        await interaction.response.send_message(embed=embed)
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Soushin(bot))