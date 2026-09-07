import logging

import discord
from discord import app_commands
from discord.ext import commands

from bot.core.config import settings

logger = logging.getLogger(__name__)


async def toggle_roles(interaction: discord.Interaction, role_id:int):
    role = interaction.guild.get_role(role_id)
    
    if not role:
        await interaction.response.send_message("Role was not found", ephemeral=True)
        
    if role in interaction.user.roles:
        await interaction.user.remove_roles(role)
        await interaction.response.send_message(f"Removed {role.name} role", ephemeral=True)
    else:
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"Added {role.name} role", ephemeral=True)

class KelasRolesButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label='🎎', style=discord.ButtonStyle.grey, custom_id="Bahasa Button")
    async def bahasaButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.BAHASA_ROLE)
        
    @discord.ui.button(label='👘', style=discord.ButtonStyle.grey, custom_id="Cosplay Button")
    async def cosplayButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.COSPLAY_ROLE)
        
    @discord.ui.button(label='🎐', style=discord.ButtonStyle.grey, custom_id="Manga Button")
    async def mangaButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.MANGA_ROLE)
        
     
class AngkatanButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label='1️⃣', style=discord.ButtonStyle.grey, custom_id="2020")
    async def ang20Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ANG_2020_ROLE)
        
    @discord.ui.button(label='2️⃣', style=discord.ButtonStyle.grey, custom_id="2021")
    async def ang21Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ANG_2021_ROLE)
    
    @discord.ui.button(label='3️⃣', style=discord.ButtonStyle.grey, custom_id="2022")
    async def ang22Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ANG_2022_ROLE)
        
    @discord.ui.button(label='4️⃣', style=discord.ButtonStyle.grey, custom_id="2023")
    async def ang23Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ANG_2023_ROLE)
        
    @discord.ui.button(label='5️⃣', style=discord.ButtonStyle.grey, custom_id="2024")
    async def ang24Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ANG_2024_ROLE)
        
    @discord.ui.button(label='6️⃣', style=discord.ButtonStyle.grey, custom_id="2025")
    async def ang25Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ANG_2025_ROLE)
        
    @discord.ui.button(label='7️⃣', style=discord.ButtonStyle.grey, custom_id="2026")
    async def ang26Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ANG_2026_ROLE)
        
        
class FakultasButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label='💵', style=discord.ButtonStyle.grey, custom_id="FEB")
    async def febButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FEB_ROLE)

    @discord.ui.button(label='⚖️', style=discord.ButtonStyle.grey, custom_id="FH")
    async def fhButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FH_ROLE)

    @discord.ui.button(label='🛠️', style=discord.ButtonStyle.grey, custom_id="FT")
    async def ftButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FT_ROLE)

    @discord.ui.button(label='💉', style=discord.ButtonStyle.grey, custom_id="FK")
    async def fkButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FK_ROLE)

    @discord.ui.button(label='🧠', style=discord.ButtonStyle.grey, custom_id="FPSI")
    async def fpsiButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FPSI_ROLE)

    @discord.ui.button(label='🎨', style=discord.ButtonStyle.grey, custom_id="FSRD")
    async def fsrdButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FSRD_ROLE)

    @discord.ui.button(label='💻', style=discord.ButtonStyle.grey, custom_id="FTI")
    async def ftiButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FTI_ROLE)

    @discord.ui.button(label='🎙️', style=discord.ButtonStyle.grey, custom_id="FIKOM")
    async def fikomButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.FIKOM_ROLE)

class DmButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='✅', style=discord.ButtonStyle.grey, custom_id="dms_open")
    async def dmsOpenButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.DMS_OPEN_ROLE)

    @discord.ui.button(label='❌', style=discord.ButtonStyle.grey, custom_id="dms_closed")
    async def dmsClosedButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.DMS_CLOSED_ROLE)

    @discord.ui.button(label='👍', style=discord.ButtonStyle.grey, custom_id="ask_to_dm")
    async def askToDmButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ASK_TO_DM_ROLE)


class PronounsButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label='🩷', style=discord.ButtonStyle.grey, custom_id="she_her")
    async def sheHerButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.SHE_HER_ROLE)

    @discord.ui.button(label='💛', style=discord.ButtonStyle.grey, custom_id="he_him")
    async def heHimButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.HE_HIM_ROLE)

    @discord.ui.button(label='💙', style=discord.ButtonStyle.grey, custom_id="they_them")
    async def theyThemButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.THEY_THEM_ROLE)

    @discord.ui.button(label='❤️‍🔥', style=discord.ButtonStyle.grey, custom_id="ask_pronouns")
    async def askPronounsButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await toggle_roles(interaction, settings.ASK_PRONOUNS_ROLE)


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="kelas-roles", description="Role kelas")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def kelasRoles(self, interaction: discord.Interaction):
        if not interaction.guild.me.guild_permissions.manage_roles:
            logger.info("Bot does not have permission")
            
        roles = KelasRolesButton()
        embed = discord.Embed(
            description=("## KELAS \n"
                         f"🎎 :: <@&{settings.BAHASA_ROLE}>\n" 
                         f"👘 :: <@&{settings.COSPLAY_ROLE}>\n" 
                         f"🎐 :: <@&{settings.MANGA_ROLE}>"),
            color=15496822
        )
        
        await interaction.channel.send(embed=embed, view=roles)
    
    @app_commands.command(name="angkatan-roles", description="Role angkatan")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def angkatanRoles(self, interaction: discord.Interaction):
        if not interaction.guild.me.guild_permissions.manage_roles:
            logger.info("Bot does not have permission")
            
        tahunMasuk = AngkatanButton()
        embed = discord.Embed(
            description=("## ANGKATAN\n"
                        f"1️⃣ :: <@&{settings.ANG_2020_ROLE}>\n"
                        f"2️⃣ :: <@&{settings.ANG_2021_ROLE}>\n"
                        f"3️⃣ :: <@&{settings.ANG_2022_ROLE}>\n"
                        f"4️⃣ :: <@&{settings.ANG_2023_ROLE}>\n"
                        f"5️⃣ :: <@&{settings.ANG_2024_ROLE}>\n"
                        f"6️⃣ :: <@&{settings.ANG_2025_ROLE}>\n"
                        f"7️⃣ :: <@&{settings.ANG_2026_ROLE}>"
            ),
            color=15496822
        )
        
        await interaction.channel.send(embed=embed, view=tahunMasuk)
        
        
    @app_commands.command(name="fakultas-roles", description="Role fakultas")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def fakultasRoles(self, interaction: discord.Interaction):
        if not interaction.guild.me.guild_permissions.manage_roles:
            logger.info("Bot does not have permission")
            
        fakultas = FakultasButton()
        embed = discord.Embed(
            description=("## FAKULTAS\n"
            f"💵 :: <@&{settings.FEB_ROLE}>\n"
            f"⚖️ :: <@&{settings.FH_ROLE}>\n"
            f"🛠️ :: <@&{settings.FT_ROLE}>\n"
            f"💉 :: <@&{settings.FK_ROLE}>\n"
            f"🧠 :: <@&{settings.FPSI_ROLE}>\n"
            f"🎨 :: <@&{settings.FSRD_ROLE}>\n"
            f"💻 :: <@&{settings.FTI_ROLE}>\n"
            f"🎙️ :: <@&{settings.FIKOM_ROLE}>"
            ),
            color=15496822
        )
        
        await interaction.channel.send(embed=embed, view=fakultas)
        
    @app_commands.command(name="pronouns-roles", description="Role pronouns")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def pronounsRoles(self, interaction: discord.Interaction):
        if not interaction.guild.me.guild_permissions.manage_roles:
            logger.info("Bot does not have permission")
            
        pronouns = PronounsButton()
        embed = discord.Embed(
            description=("## PRONOUNS\n"
            f"🩷 :: <@&{settings.SHE_HER_ROLE}>\n"
            f"💛 :: <@&{settings.HE_HIM_ROLE}>\n"
            f"💙 :: <@&{settings.THEY_THEM_ROLE}>\n"
            f"❤️‍🔥 :: <@&{settings.ASK_PRONOUNS_ROLE}>"
            ),
            color=15496822
        )
        
        await interaction.channel.send(embed=embed, view=pronouns)
        
    @app_commands.command(name="dm-roles", description="Role dms")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    async def genderRoles(self, interaction: discord.Interaction):
        if not interaction.guild.me.guild_permissions.manage_roles:
            logger.info("Bot does not have permission")
            
        dm = DmButton()
        embed = discord.Embed(
            description=("## DM PREFERENCES\n"
            f"✅ :: <@&{settings.DMS_OPEN_ROLE}>\n"
            f"❌ :: <@&{settings.DMS_CLOSED_ROLE}>\n"
            f"👍 :: <@&{settings.ASK_TO_DM_ROLE}>"
            ),
            color=15496822
        )
        
        await interaction.channel.send(embed=embed, view=dm)
async def setup(bot: commands.Bot):
    await bot.add_cog(Roles(bot))