from config import configuratie
import discord
from discord.ext import commands
from JsonParser import JsonParser

Client = discord.Client()
bot = commands.Bot(command_prefix="!")
json_parser = JsonParser()

# log voor als de bot geladen is
@bot.event
async def on_ready():
    print("Bot is klaar voor gebruik")



@bot.event
async def on_message(message):
    # print het hanzeXperience logo in de chat als iemand een variatie van !HanzeXperience typt
    if message.content.upper().startswith('!HANZEXPERIENCE'):
        await bot.send_message(message.channel, "https://i.imgur.com/msv9liC.gif")

    # print de versienummer van de bot in de chat
    if message.content.upper().startswith('!VERSIE'):
        await bot.send_message(message.channel, "De huidige versie van Hanze Meme Machine is: v" + configuratie["versienummer"])

    # print een willekeurig meme in de chat waar hij aangeroepen in
    if message.content.upper().startswith('!MEME'):
        await bot.send_message(message.channel, json_parser.zoek_meme_willekeurig())


bot.run(configuratie["discord_api_sleutel"])
