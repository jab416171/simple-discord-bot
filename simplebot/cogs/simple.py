import discord
import random
import asyncio
from discord.ext import commands
from discord.commands import Option, slash_command

class SimpleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Display invite link')
    async def invite(self, ctx):
        await ctx.send(f"Invite link is https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands")

    @slash_command(name="roll", name_localizations={"fr": "roll_fr", "zh-CN": "滚动", "en-GB": "roll_gb"}, description_localizations={"fr": "roll in French"})
    async def roll(self, ctx, sides: Option(int, "Number of sides on the die", default=6, name_localizations={"fr": "sides_fr", "en-GB": "sides_gb", "zh-CN": "sides_cn"}, description_localizations={"fr": "sides in French"})):
        """roll a die"""
        try:
            print(ctx.interaction.locale)
        except:
            pass
        number = random.randint(1, sides)
        response = await ctx.respond("rolling ...")
        await asyncio.sleep(0.2)
        await response.edit_original_message(content="rolling 0..")
        await asyncio.sleep(0.2)
        await response.edit_original_message(content="rolling .0.")
        await asyncio.sleep(0.2)
        await response.edit_original_message(content="rolling ..0")
        await asyncio.sleep(0.2)
        await response.edit_original_message(content=f"You rolled a {number}")

    @slash_command(name="flip")
    async def flip(self, ctx: discord.ApplicationContext):
        """flip a coin"""
        number = random.randint(1, 2)
        response = await ctx.respond("flipping -")
        await asyncio.sleep(0.2)
        await response.edit_original_message(content="flipping |")
        await asyncio.sleep(0.2)
        await response.edit_original_message(content="flipping -")
        await asyncio.sleep(0.2)
        await response.edit_original_message(content="flipping |")
        await asyncio.sleep(0.2)
        number = "heads" if number == 1 else "tails"
        await response.edit_original_message(content=f"It's {number}")

    @slash_command(name="source")
    async def source(self, ctx: discord.ApplicationContext):
        """Shows the bot's source code"""
        embed=discord.Embed(title="Source code", description="My source code can be found here: [Link](https://github.com/jab416171/simple-discord-bot)")
        await ctx.respond(embed=embed, ephemeral=True)

    @slash_command(name="about")
    async def about(self, ctx: discord.ApplicationContext):
        """Tells you a bit about the bot"""
        embed=discord.Embed(title="About Me", description="I am a simple discord bot, written to showcase some features of pycord.")
        await ctx.respond(embed=embed, ephemeral=True)

    @slash_command(name="status")
    async def status(self, ctx: discord.ApplicationContext):
        """Checks your user status"""
        online = str(ctx.author.raw_status)
        if ctx.author.is_on_mobile():
            await ctx.respond(f"You are on mobile and you are {online}!")
        else:
            await ctx.respond(f"You are not on mobile and you are {online}!")

def setup(bot):
    bot.add_cog(SimpleCog(bot))