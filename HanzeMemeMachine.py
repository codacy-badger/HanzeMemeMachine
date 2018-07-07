from config import configuratie
import discord
from discord.ext import commands
from JsonParser import JsonParser

Client = discord.Client()
bot = commands.Bot(command_prefix="!")
json_parser = JsonParser()

# als je een nieuwe commando maakt zet hem ook in deze dict. Deze wordt uitgelezen door !help
commandos = {
    "!HANZEXPERIENCE": "Post het HanzeXperience logo in de chat waar deze is aangevraagd",
    "!VERSIE": "Toont de versienummer van de bot in de chat waar deze is aangevraagd",
    "!MEME": "Geeft een willekeurige meme van HanzeMemes in de chat waar deze is aangevraagd",
    "!HELP": "Geeft een lijst terug met alle commando's"
}


@bot.event
async def on_ready():
    print("Bot is klaar voor gebruik")


@bot.event
async def on_message(message):
    if message.content.upper().startswith('!HANZEXPERIENCE'):
        await bot.send_message(message.channel, "https://i.imgur.com/msv9liC.gif")

    if message.content.upper().startswith('!VERSIE'):
        await bot.send_message(message.channel,
                               "De huidige versie van Hanze Meme Machine is: v" + configuratie["versienummer"])

    if message.content.upper().startswith('!MEME'):
        await bot.send_message(message.channel, json_parser.zoek_meme_willekeurig())

    if message.content.upper().startswith('!HELP'):
        commando_string = ""
        for commando in commandos:
            commando_string += commando + "\n"
        await bot.send_message(message.channel, "Je kan de volgende commando's gebruiken: \n\n" + commando_string)



bot.run(configuratie["discord_api_sleutel"])
