import discord
import random
import time
from discord.ext import commands
from discord.commands import Option

class SimpleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.startup())

    async def startup(self):
        await self.bot.wait_until_ready()

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            self.sessions[guild.id] = []
            for channel in guild.channels:
                if channel.name == "bot-log":
                    await channel.send("Bot is online. v3.0.0")

    @commands.command(brief='Display invite link')
    async def invite(self, ctx):
        await ctx.send(f"Invite link is https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands")

    @commands.slash_command(name="roll")
    async def roll(self, ctx, sides: Option(int, "Number of sides on the die", default=6)):
        """roll a die"""
        number = random.randint(1, sides)
        response = await ctx.respond("rolling ...")
        time.sleep(0.2)
        await response.edit_original_message(content="rolling 0..")
        time.sleep(0.2)
        await response.edit_original_message(content="rolling .0.")
        time.sleep(0.2)
        await response.edit_original_message(content="rolling ..0")
        time.sleep(0.2)
        await response.edit_original_message(content=f"You rolled a {number}")

    @commands.slash_command(name="flip")
    async def flip(self, ctx):
        """flip a coin"""
        number = random.randint(1, 2)
        response = await ctx.respond("flipping -")
        time.sleep(0.2)
        await response.edit_original_message(content="flipping |")
        time.sleep(0.2)
        await response.edit_original_message(content="flipping -")
        time.sleep(0.2)
        await response.edit_original_message(content="flipping |")
        time.sleep(0.2)
        number = "heads" if number == 1 else "tails"
        await response.edit_original_message(content=f"It's {number}")