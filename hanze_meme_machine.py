import os

# in config.py moet een enviroment variabele met je eigen reddit bot token
import self as self

import config

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


bot.run(os.environ["HANZEMEMEMACHINETOKEN"])
