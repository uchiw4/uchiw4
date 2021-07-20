from discord.ext import commands
from pyfade import Fade, Colors
from pycenter import center
import discord
import time



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
    TOKEN = input("\033[1;31;40m Ton token : \033")
except:
    print("\033[1;31;40m [!]Entre un token valide ! \033")
    TOKEN = input("\033[1;31;40m Token : \033")


statuslist = []
quest = input("\033[1;31;40m Combien de statuts veux-tu (max. 5) ?\033")
if quest == 1:
    status1 = input("\033[1;31;40m Statut 1: \033")
    statuslist.append(status1)
elif quest == 2:
    status2 = input("\033[1;31;40m Statut 2: \033")
    statuslist.append(status2)
elif quest == 3:
    status3 = input("\033[1;31;40m Statut 3: \033")
    statuslist.append(status3)
elif quest == 4:
    status4 = input("\033[1;31;40m Statut 4: \033")
    statuslist.append(status4)
elif quest == 5:
    status5 = input("\033[1;31;40m Statut 5: \033")






@bot.event
async def on_ready():
    print("\033[1;31;40m C'est bon, tu peux maintenant profiter de ton nouveau statut animé !\033")
    
    while True:
        await bot.change_presence(activity=discord.Game(name=status1))
        time.sleep(5)
        await bot.change_presence(activity=discord.Game(name=status2))
        time.sleep(5)
        await bot.change_presence(activity=discord.Game(name=status3))
        time.sleep(5)
        await bot.change_presence(activity=discord.Game(name=status4))
        time.sleep(5)
        await bot.change_presence(activity=discord.Game(name=status5))
        time.sleep(5)










bot.run(TOKEN, bot=False)
