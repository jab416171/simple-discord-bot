# simplebot.py

from discord.ext import commands
import discord
import os
import logging
import sys

BOT_COLOR = 0x0D61B7

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler1 = logging.FileHandler("bot.log")
handler2 = logging.StreamHandler(sys.stdout)
logger.addHandler(handler1)
logger.addHandler(handler2)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_extension("jishaku")

    async def on_connect(self):
        await self.sync_commands(force=True)

def run(discord_token):
    """ Create the bot, add the cogs and run it. """
    bot = Bot(command_prefix=('s!'), case_insensitive=True, debug_guilds=[881207955029110855], intents=discord.Intents.all())

    for filename in os.listdir('simplebot/cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    bot.run(discord_token)