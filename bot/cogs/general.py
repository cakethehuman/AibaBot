import textwrap
import logging

import discord
from discord import app_commands
from discord.ext import commands

from bot.core.config import settings

logger = logging.getLogger(__name__)

class RulesInfo(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        
    @discord.ui.button(label='𑣲 Rules', style=discord.ButtonStyle.gray, custom_id="Rules")
    async def Rules(self, interaction: discord.Interaction, button: discord.ui.Button):
        banner = discord.File('bot/assets/Rules.png')
        embed = discord.Embed(
            description=(
                "## 1. BE RESPECTFUL\n"
                "**Jaga kesopanan dan saling menghormati** member lain. Make sure to be kind to each other! Jika ada masalah personal, tolong selesaikan secara private.\n"
                "## 2. NO NSFW & POLITICS\n"
                "Diperbolehkan membahas apapun di dalam server discord yang sudah disediakan selama **tidak mengandung politik, unsur SARA, pornografi, heavy gore dan semacamnya** yang dapat mengganggu kenyamanan bersama.\n"
                "-#  (light gore diperbolehkan asal tidak terlalu sering).\n"
                "## 3. USE CHANNELS APPROPRIATELY\n"
                "Dimohon untuk membahas chat/topik yang **sesuai dengan channel**.\n"
                "## 4. NO SPAMMING\n"
                "Dimohon untuk **tidak melakukan spam secara berlebihan**. Chat/pesan yang berpotensi untuk mengganggu aliran chat adalah spam.\n"
                "## 5. NO INVITES\n"
                "Hanya BPH/I Soushin yang diperbolehkan melakukan Invite di server discord ini.\n\n"
                "- Teman-teman dimohon untuk **mengubah nama discord menjadi nama panggilan atau nama asli** agar lebih gampang dikenal kami saat diadakan event/hangout dalam server ini.\n"
                "- Dimohon untuk **meninggalkan jejak berupa reaction** pada chat ini sebagai tanda bahwa kalian sudah membacanya.\n"
                "- **Masih bingung atau mau nanya**? Silahkan klick button \"About & Contact Us\" untuk menanyakan informasi lebih lanjut!"),
            color=15496822
        )
        embed.set_footer(text="This message is manmade by Soushin: Bot Devs and NOT by AI. Thank you for reading! >u<")
        await interaction.response.send_message(file=banner, embed=embed, ephemeral=True)
    
    @discord.ui.button(label='✦ Info', style=discord.ButtonStyle.gray, custom_id="Info")
    async def Info(self, interaction: discord.Interaction, button: discord.ui.Button):
        banner = discord.File('bot/assets/Information.png')
        info_buttons = Info()
        embed = discord.Embed(
            description="Click the buttons below to learn more about the server!",
            color=15496822
        )
        embed.set_footer(text="This message is manmade by Soushin: Bot Devs and NOT by AI. Thank you for reading! >u<")
        await interaction.response.send_message(file=banner, embed=embed, ephemeral=True, view=info_buttons)
        
    @discord.ui.button(label='♪ About & Contact Us', style=discord.ButtonStyle.gray, custom_id="About&contact")
    async def Resources(self, interaction: discord.Interaction, button: discord.ui.Button):
        banner = discord.File('bot/assets/About & Contact.png')
        embed = discord.Embed(description=("## 「Soushin」とは？\n\n"
                                           "Soushin (相信): Tarumanagara Nihon Bu adalah Unit Kegiatan Mahasiswa (UKM) di Universitas Tarumanagara yang bergerak di bidang Jejepangan dengan tujuan menjadi wadah untuk menampung serta menyalurkan hobi, bakat, dan minat mahasiswa-mahasiswi Universitas Tarumanagara dalam bidang tersebut. Soushin didirikan pada tahun 2016 menjadikannya UKM termuda Universitas Tarumanagara yang kini telah menginjak usia 10 tahun. Di UKM ini, mahasiswa juga dapat mengembangkan keterampilan berorganisasi yang profesional, mandiri, dan berintegritas dengan landasan kekeluargaan.\n\n"
                                           "Nama Soushin sendiri juga memiliki arti yang berasal dari gabungan dua kata yaitu: Sou (相) yang berarti “Bersama” dan Shin (信) yang berarti “Kepercayaan, Kejujuran, dan Kesetiaan”. Oleh karena itu, nama Soushin menjadi pedoman tersendiri bagi organisasi ini untuk selalu berasaskan kepercayaan dan kekeluargaan yang berorientasi pada budaya Jepang.\n\n"
                                           "brief explanation about what soushin is. like Soushin: tarumanagara nihon bu adalah sebuah ukm dalam blablabla\n\n"
                                           "## Contact Us!\n> - <@&1149358801397485699> member dengan role ini adalah seorang BPH. Badan Pengurus Harian adalah struktur inti atau eksekutif yang bertanggung jawab menjalankan kegiatan dan operasional organisasi sehari-hari.\n"
                                           "> - <@&1546148492458856468> member dengan role ini merupakan member yang membantu dengan perkembangan bot dan server soushin.\n"
                                           "**Jika mempunyai pertanyaan atau masalah**, diharapkan untuk contact member yang memiliki role diatas :D"),
                              color=15496822)
        await interaction.response.send_message(file=banner, embed=embed, ephemeral=True)


class Info(discord.ui.View): 
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(label='✿ Kelas', style=discord.ButtonStyle.gray, custom_id="Kelas")
    async def Kelas(self, interaction: discord.Interaction, button: discord.ui.Button):
        banner = discord.File('bot/assets/Kelas.png')
        embed = discord.Embed(
            description=("## DIVISI COSPLAY\n"
                         "> Di kelas cosplay ini, kamu akan menerima pengetahuan seputar dunia Cosplay; mulai dari styling wig, makeup, hingga pembuatan prop yang mendukung cosplay kamu!\n\n"
                         "## DIVISI MANGA\n"
                         "> Di kelas manga, kamu akan diajarkan beberapa hal teknis; seperti komposisi, shading, perspektif, panelling, color theory, dan masih banyak lagi!\n\n"
                         "## DIVISI BAHASA\n"
                         "> Sesuai dengan namanya sendiri, di Kelas Bahasa kamu akan mempelajari seputar bahasa Jepang, mulai dari huruf-huruf (Hiragana, Katakana, dan yang paling ditakuti yaitu Kanji), kosa kata (单語), partikel, pola kalimat, dan masih banyak lagi!\n"
                         "────────────────────────\n"
                         "You've scrolled this far? Keren banget! Here are some funfacts for you!\n"
                         "### Funfacts Kelas Soushin!\n\n"
                         "1. Divisi Manga terkadang mengadakan kegiatan yang berkaitan dengan seni, seperti Gartic Phone, art collab, hingga art competition, lho!\n"
                         "2. Selain mengadakan berbagai program kerja, Soushin juga sering mengadakan kegiatan bonding di luar kampus yang tidak kalah seru!\n"
                         "3. Kelas Divisi Bahasa tidak hanya membahas teori bahasa Jepang, tetapi juga sering mengadakan praktik atau hands-on learning agar pembelajaran terasa lebih interaktif!\n"
                         "4. Ulang tahun Soushin, atau Soushin no Tanjoubi, diperingati setiap tanggal 24 Juni!\n"
                         "5. Dalam kelas Divisi Cosplay, kamu akan diajarkan cara menggunakan berbagai macam bahan dan teknik untuk mewujudkan cosplay-mu menjadi nyata!\n"
                         "6. Soushin didirikan pada tahun 2016, menjadikannya UKM termuda di UNTAR!\n"
                         "7. Maskot utama Soushin memiliki nama lengkap, yaitu Aiba Makoto!\n"
                         "8. Setiap tahun, Soushin menerbitkan majalah Papercrane yang merangkum berbagai kenangan dan perjalanan yang telah kami lalui bersama!\n"
                         "9. Harukaze Festival merupakan program kerja terbesar Soushin. Jadi, jangan lupa untuk ikut memeriahkannya pada volume berikutnya, ya!\n"
                         "10. Nama Soushin merupakan gabungan dari Sou (相), yang memiliki makna “bersama”, dan Shin (信), yang bermakna “kepercayaan, kejujuran, dan kesetiaan."),
            color=15496822
        )
        embed.set_footer(text="This message is manmade by Soushin: Bot Devs and NOT by AI. Thank you for reading! >u<")
        await interaction.response.send_message(file=banner, embed=embed, ephemeral=True)


    @discord.ui.button(label='✿ Proker', style=discord.ButtonStyle.gray, custom_id="Proker")
    async def Proker(self, interaction: discord.Interaction, button: discord.ui.Button):
        banner = discord.File('bot/assets/Proker.png')
        embed = discord.Embed(
            description=("## WELCOMING PARTY\n"
                         "> Acara pembuka Soushin sebagai penyambut anggota baru dan memperkenalkan Soushin: Tarumanagara: Nihon Bu. \n\n"
                         "## GASSHUKU CAMP\n"
                         "> Program yang diadakan untuk mempererat ikatan serta membangun kebersamaan antara anggota selama tiga hari dan dua malam di luar kampus. \n\n"
                         "## NIHONGO CONTEST\n"
                         "> Ajang perlombaan yang berfokus pada Bahasa Jepang yang terdiri dari 3 lomba, yaitu Anime Dubbing, J-Song, dan Cerdas Cermat. \n\n"
                         "## PELATIHAN DASAR KEORGANISASIAN\n"
                         "> Pelatihan bagi anggota kepengurusan sebagai wadah pembekalan Badan Pengurus Harian (BPH) baru agar bisa lebih matang dan siap menjalankan roda organisasi.\n\n"
                         "## COMPANY VISIT\n"
                         "> Kunjungan ke instansi eksternal di luar kampus dengan tujuan memperkaya pengetahuan peserta kunjungan. \n\n"
                         "## BAKTI SOSIAL\n"
                         "> Timbal-balik kepada masyarakat melalui program pelestarian lingkungan dan donasi secara sukarela. \n\n"
                         "## PHOTOBOOK COSPLAY\n"
                         "> Kegiatan dokumentasi yang dilakukan pada studio in-house oleh anggota bagian dari divisi cosplay, hasil foto akan dipublikasikan dalam bentuk dokumentasi dan dijilid dalam satu buku. \n\n"
                         "## PAPERCRANE\n"
                         "> Majalah yang merangkum seluruh kegiatan UKM Soushin: Tarumanagara Nihon Bu ke dalam artikel lalu dipublikasikan secara fisik dan digital.\n\n"
                         "## HARUKAZE FESTIVAL\n"
                         "> Puncak program kerja Soushin yang terdiri dari berbagai jenis perlombaan serta art market, menjadi wadah bagi para creative talent dari berbagai fandom dan komunitas penggemar budaya Jepang lainnya."),
            color=15496822)
        embed.set_footer(text="This message is manmade by Soushin: Bot Devs and NOT by AI. Thank you for reading! >u<")
        await interaction.response.send_message(file=banner, embed=embed, ephemeral=True)
        

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
        channel_id = settings.RULES_INFO_ID
        channel = self.bot.get_channel(channel_id)
        async for message in channel.history(limit=500):
            if message.author == self.bot.user:
                try:
                    await message.delete()
                    logger.info("Message was delete success")
                except discord.HTTPException as e:
                    logger.info(f"Error because of {e}")
        
        logger.info("Made the Rules and Info")
        banner = discord.File('bot/assets/Rules & Info.png')
        rules_info_button = RulesInfo()
        await channel.send(file=banner, view=rules_info_button)
         

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))