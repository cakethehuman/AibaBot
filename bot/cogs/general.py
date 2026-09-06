import logging

import discord
from discord import app_commands
from discord.ext import commands

from bot.core.config import settings

logger = logging.getLogger(__name__)
class RulesInfo(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label='𑣲 Rules', style=discord.ButtonStyle.gray, custom_id="Rules")
    async def Rules(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Rules", ephemeral=True)
    
    @discord.ui.button(label='✦ Info', style=discord.ButtonStyle.gray, custom_id="Info")
    async def Info(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Info", ephemeral=True)
        
    @discord.ui.button(label='♪ Resources', style=discord.ButtonStyle.gray, custom_id="Resources")
    async def Resources(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Resources", ephemeral=True)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="help", description="need help?")
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description="Bot under contruction 🤖"
        )
        await interaction.response.send_message(embed=embed)
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        banner = discord.File('bot/assets/Rules.png')
        rules_info_button = RulesInfo()
        channel_id = settings.RULES_INFO_ID
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            description="Help to you"
        )
        await channel.send(file=banner,embed=embed, view=rules_info_button)
         

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))