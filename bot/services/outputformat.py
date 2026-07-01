import random
from datetime import datetime

import discord

def make_output(title, description):
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.dark_red()
    )
    quotes = ['Be who you are and say what you feel', "Do you know who made this bot?", 
              "ketika pintu ditutup, masih ada jendela - BPH soushin", "ya udah lah ya",
              "UMAAAAAAAAA"]
    random_quotes = random.choice(quotes)
    waktu_message = datetime.now().strftime("%H:%M")
    embed.set_footer(text = f"{random_quotes} • {waktu_message} WIB")
    return embed