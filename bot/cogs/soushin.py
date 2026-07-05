import logging

import discord
from discord import app_commands
from discord.ext import commands

from ..services.outputformat import make_output

logger = logging.getLogger(__name__)
class Soushin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @app_commands.command(name="soushin", description="Say hello to Aiba")
    async def soushin_command(self, interaction: discord.Interaction):
        logging.info("Used Hello command")
        title = "🌸 こんにちは!"
        description = ("私は **AIBA**! 🌟\n"
                       "Kamu penasaran apa itu soushin?\n"
                        "Soushin adalah ........"
                        )
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="proker", description="proker yang ada di soushin")
    async def proker_command(self, interaction: discord.Interaction):
        title = "🌸 こんにちは!"
        description = ("⚠️ STILL DEVELOPMENT")
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="bph", description="bph di soushin")
    async def bph_command(self, interaction: discord.Interaction):
        title = "🌸 こんにちは!"
        description = ("⚠️ STILL DEVELOPMENT")
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="mascot", description="Mascot soushin")
    async def mascot_command(self, interaction: discord.Interaction):
        title = "🌸 こんにちは!"
        description = ("⚠️ STILL DEVELOPMENT")
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
        
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Soushin(bot))