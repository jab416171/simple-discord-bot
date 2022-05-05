# help.py

import traceback
import sys
import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    """ Handles everything related to the help menu. """

    def __init__(self, bot):
        """ Set attributes and remove default help command. """
        self.bot = bot
        self.bot.remove_command('help')

    def help_embed(self, title):
        embed = discord.Embed(title=title)
        prefix = self.bot.command_prefix
        prefix = prefix[0] if prefix is not str else prefix

        for cog in self.bot.cogs:  # Uset bot.cogs instead of bot.commands to control ordering in the help embed
            for cmd in self.bot.get_cog(cog).get_commands():
                if cmd.brief:
                    if cmd.usage:  # Command has usage attribute set
                        embed.add_field(name=f'**{prefix}{cmd.usage}**', value=f'_{cmd.brief}_', inline=True)
                    else:
                        embed.add_field(name=f'**{prefix}{cmd.name}**', value=f'_{cmd.brief}_', inline=True)

        return embed

    @commands.Cog.listener()
    async def on_ready(self):
        """ Set presence to let users know the help command. """
        activity = discord.Activity(type=discord.ActivityType.listening, name="I am a simple discord bot")
        await self.bot.change_presence(activity=activity)

    async def cog_before_invoke(self, ctx):
        """ Trigger typing at the start of every command. """
        await ctx.trigger_typing()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """ Send help message when a mis-entered command is received. """

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        if type(error) is commands.CommandNotFound:
            in_cmd = ctx.invoked_with
            bot_cmds = list(self.bot.commands)

            # Prep help message title
            embed_title = f'**```{ctx.message.content}```** is not valid!'
            prefix = self.bot.command_prefix
            prefix = prefix[0] if prefix is not str else prefix

            embed_title += f' Use `{prefix}help` for a list of commands'

            embed = discord.Embed(title=embed_title)
            await ctx.send(embed=embed)

    @commands.command(brief='Display the help menu')  # TODO: Add 'or details of the specified command'
    async def help(self, ctx):
        """ Generate and send help embed based on the bot's commands. """
        embed = self.help_embed('__Simple Bot Commands__')
        await ctx.send(embed=embed, delete_after=30)
        try:
            await ctx.message.delete()
        except:
            pass


def setup(bot):
    bot.add_cog(HelpCog(bot))