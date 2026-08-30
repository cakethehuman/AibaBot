import logging

import discord
from discord import app_commands
from discord.ext import commands

logger = logging.getLogger(__name__)

class ProkerButtons(discord.ui.view):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label='WP', style=discord.ButtonStyle.red, custom_id="welcoming party")
    async def WP_button(self, interaction: discord.Interaction):
        await interaction.response.send_message("test code ig")

class Soushin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="soushin", description="Perkenalan tentang soushin")
    async def soushin_command(self, interaction: discord.Interaction):
        proker = ProkerButtons()
        embed = discord.Embed(
            description="Bot under contruction 🤖"
        )
        
        await interaction.response.send_message(embed=embed, view=proker)
        
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Soushin(bot))