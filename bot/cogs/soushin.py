import discord
from discord import app_commands
from discord.ext import commands

from ..services.outputformat import make_output

class Soushin(commands.cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot
        
    @app_commands.command(name="soushin", description="Say hello to Aiba")
    async def soushin_command(self, interaction: discord.Interaction):
        title = "🌸 こんにちは!"
        description = ("私は **AIBA**! 🌟\n"
                       "Aku maskot utama soushin yang siap membantu kamu di sever ini\n"
                        "Gunnakan command /help untuk liat semua command pada server"
                        )
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="proker", description="Say hello to Aiba")
    async def proker_command(self, interaction: discord.Interaction):
        title = "🌸 こんにちは!"
        description = ("私は **AIBA**! 🌟\n"
                       "Aku maskot utama shoushin yang siap membantu kamu di sever ini\n"
                        "Gunnakan command /help untuk liat semua command pada server"
                        )
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="bph", description="Say hello to Aiba")
    async def bph_command(self, interaction: discord.Interaction):
        title = "🌸 こんにちは!"
        description = ("私は **AIBA**! 🌟\n"
                       "Aku maskot utama shoushin yang siap membantu kamu di sever ini\n"
                        "Gunnakan command /help untuk liat semua command pada server"
                        )
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
        
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Soushin(bot))