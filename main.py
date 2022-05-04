import asyncio
import os 

import discord
from discord import Intents

from dotenv import load_dotenv
from random import randint
from variables import Whitelisted_Guilds
load_dotenv()

bot_token = os.getenv('BOT_1_TOKEN')

intents = Intents().default()
intents.presences = True
intents.members = True

bot = discord.Bot(intents=intents) #rg bot

@bot.event
async def on_ready():
    activity = discord.Game(name='Bot', type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Logged in as {bot.user}')

for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])


bot.run(bot_token)
