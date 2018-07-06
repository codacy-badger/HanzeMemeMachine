from config import configuratie
import discord
from discord.ext import commands
from JsonParser import JsonParser

Client = discord.Client()
bot = commands.Bot(command_prefix="!")

# log voor als de bot geladen is
@bot.event
async def on_ready():
    print("Bot is klaar voor gebruik")


# print print het hanzeXperience logo in de chat als iemand een variatie van !HanzeXperience typt
@bot.event
async def on_message(message):
    if message.content.upper().startswith('!HANZEXPERIENCE'):
        await bot.send_message(message.channel, "https://i.imgur.com/msv9liC.gif")
    if message.content.upper().startswith('!VERSIE'):
        await bot.send_message(message.channel, "De huidige versie van Hanze Meme Machine is: v" + configuratie["versienummer"])

bot.run(configuratie["discord_api_sleutel"])
