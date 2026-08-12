import logging
import asyncio

import discord
from discord import app_commands
from discord.ext import commands

from bot.services.outputformat import make_output

logger = logging.getLogger(__name__)
class Soushin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="soushin", description="Perkenalan tentang soushin")
    async def soushin_command(self, interaction: discord.Interaction):
        logging.info("Used Hello command")
        title = "🌸 ヤフー!"
        description = ("私は **AIBA**! 🌟\n"
                       "Kamu penasaran apa itu soushin?\n"
                        "Soushin adalah ........"
                        )
    
        embed = make_output(title,description)
        await interaction.response.send_message(embed=embed)
    
    # Development
    # @app_commands.command(name="proker", description="proker yang ada di soushin")
    # async def proker_command(self, interaction: discord.Interaction):
    #     title = "🌸 ヤフー!"
    #     description = ("⚠️ STILL DEVELOPMENT")
    
    #     embed = make_output(title,description)
    #     await interaction.response.send_message(embed=embed)
        
    # Development
    # @app_commands.command(name="kelas", description="Mascot soushin")
    # async def kelas_command(self, interaction: discord.Interaction):
    #     title = "🌸 ヤフー!"
    #     description = ("⚠️ STILL DEVELOPMENT")
    
    #     embed = make_output(title,description)
    #     await interaction.response.send_message(embed=embed)
    #     message = await interaction.original_response()
    #     await message.add_reaction("1️⃣")
    #     await message.add_reaction("2️⃣")
    #     await message.add_reaction("3️⃣") 
        
        
    #     def check(reaction, user):
    #         return (user == interaction.user and reaction.message.id == message.id and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣"])
            
    #     try:
    #         reaction, user = await self.bot.wait_for("reaction_add", timeout = 30, check=check)
    #     except asyncio.TimeoutError:
    #         return await interaction.followup.send("Waktu habis, gak ada pilihan yang dipilih.")

    #     match str(reaction.emoji): 
    #         case "1️⃣":
    #             kelas_embed = make_output("Kelas Bahasa", "Isi materi kelas bahasa di sini.")
    #             await interaction.followup.send(embed=kelas_embed)
    #         case "2️⃣":
    #             kelas_embed = make_output("Manga here")
    #             await interaction.followup.send(embed=kelas_embed)
    #         case "3️⃣":
    #             kelas_embed = make_output("Cosplay")
    #             await interaction.followup.send(embed=kelas_embed)
    #         case _:
    #             gagal_embed = make_output("Tidak bisa")
    #             await interaction.followup.send(embed=gagal_embed)
                
async def setup(bot: commands.Bot):
    await bot.add_cog(Soushin(bot))