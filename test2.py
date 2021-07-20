from discord.ext import commands
from pyfade import Fade, Colors
from pycenter import center

text ="""
███╗   ██╗ █████╗ ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗     
████╗  ██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔██╗ ██║███████║███████╗███████╗   ██║   ██║   ██║██║   ██║██║     
██║╚██╗██║██╔══██║╚════██║╚════██║   ██║   ██║   ██║██║   ██║██║     
██║ ╚████║██║  ██║███████║███████║   ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"""
print(Fade.Vertical(Colors.red_to_blue, center(text)))




bot = commands.Bot(command_prefix= "", self_bot=True)



entree = "Ton token beau gosse:  "

try:
    TOKEN = input("\033[1;31;40m Token : \033")
except:
    print("\033[1;31;40m Entre ton token je vais t'enculer ! \033")
    TOKEN = input("\033[1;31;40m Token : \033")





@bot.event
async def on_ready():
    print("\033[1;31;40m C'est prêt mon reuf va t'amuser\033")

@bot.command()
async def test(ctx):
    await ctx.send("oof")





bot.run(TOKEN, bot=False)