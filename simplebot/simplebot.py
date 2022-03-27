# simplebot.py

from discord.ext import commands
import discord
import os

BOT_COLOR = 0x0D61B7

def run(discord_token):
    """ Create the bot, add the cogs and run it. """
    bot = commands.Bot(command_prefix=('!'), case_insensitive=True, debug_guilds=[881207955029110855], intents=discord.Intents.all())

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    bot.run(discord_token)