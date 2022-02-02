# simplebot.py

from discord.ext import commands
import discord
import cogs

BOT_COLOR = 0x0D61B7

def run(discord_token):
    """ Create the bot, add the cogs and run it. """
    bot = commands.Bot(command_prefix=('!'), case_insensitive=True)
    bot.add_cog(cogs.ConsoleCog(bot))
    bot.add_cog(cogs.HelpCog(bot, BOT_COLOR))
    bot.add_cog(cogs.SimpleCog(bot))

    bot.run(discord_token)