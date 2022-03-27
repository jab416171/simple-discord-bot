# simplebot.py

from discord.ext import commands
import discord

BOT_COLOR = 0x0D61B7

def run(discord_token):
    """ Create the bot, add the cogs and run it. """
    bot = commands.Bot(command_prefix=('!'), case_insensitive=True, debug_guilds=[881207955029110855], intents=discord.Intents.all())

    bot.run(discord_token)