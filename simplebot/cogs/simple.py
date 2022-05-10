import discord
import random
import asyncio
import os
from discord.ext import commands, pages
from discord.commands import Option, slash_command
from discord.ui import InputText

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
        member = ctx.guild.get_member(ctx.author.id)
        online = str(member.raw_status)
        if member.is_on_mobile():
            await ctx.respond(f"You are on mobile and you are {online}!")
        else:
            await ctx.respond(f"You are not on mobile and you are {online}!")

    @commands.slash_command(name="pagtest")
    async def pagtest(self, ctx):
        """ephemeral paginator test"""
        try:
            await ctx.response.defer(ephemeral=True)
        except:
            pass
        page_list=["page 1", "page 2"]
        paginator = pages.Paginator(pages=page_list)
        await paginator.respond(ctx.interaction, ephemeral=True)

    @commands.slash_command(name="chantest")
    async def chantest(self, ctx, channel: Option(discord.TextChannel)):
        """channel test"""
        await ctx.respond(f"You selected {channel.name}")

    @commands.slash_command(name="version")
    async def version(self, ctx):
        """ display pycord version """
        await ctx.respond(f"pycord: {discord.__version__}", ephemeral=True)

    @commands.slash_command(
        name="purging_thread",
        description="Deletes all messages from this bot in a thread.",
    )
    async def purging_thread(self, ctx):
        await ctx.channel.purge(limit=5)

    @commands.slash_command(name="ping")
    async def ping(self, ctx):
        """Reponds with Pong!"""
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.slash_command(name="tulagang")
    async def tulagang(self, ctx):
        """TULAGANG"""
        await ctx.respond(":regional_indicator_t: :regional_indicator_u: :regional_indicator_l: :a: :regional_indicator_g: :regional_indicator_a: :regional_indicator_n: :regional_indicator_g:", delete_after=15)

    @commands.slash_command(name="poll")
    async def poll(self, ctx, question: Option(str), option1: Option(str), option2: Option(str, required=False), option3: Option(str, required=False), option4: Option(str, required=False), option5: Option(str, required=False), option6: Option(str, required=False), option7: Option(str, required=False), option8: Option(str, required=False), option9: Option(str, required=False), option10: Option(str, required=False)):
        """Creates a poll with reactions for each question"""
        if not await check_access(ctx, "/poll"):
            return
        options = [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10]
        numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        new_options = []
        for option in options:
            if option:
                new_options.append(option)
        message = f"{question}\n"
        response = await ctx.respond(message)
        for i, option in enumerate(new_options):
            emoji = numbers[i]
            # real_emoji = discord.utils.get(ctx.guild.emojis, name=emoji.replace(":",""))
            # if not real_emoji:
            #     real_emoji = emoji
            message += f"{i+1}: {option}\n"
            await response.edit_original_message(content=message)
            m = await response.original_message()
            await m.add_reaction(emoji)

    @commands.slash_command(name="roll")
    async def roll(self, ctx, sides: Option(int, "Number of sides on the die", default=6, min_value=1)):
        """roll a die"""
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

    @commands.slash_command(name="flip")
    async def flip(self, ctx):
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

    @commands.slash_command(name="check_invite")
    async def check_invite(self, ctx, invite_url):
        """Prints out information about the given invite"""
        invite = await self.bot.fetch_invite(invite_url)
        member_count = invite.approximate_member_count
        online_count = invite.approximate_presence_count
        name = invite.guild.name
        expiration = invite.max_age
        if not expiration:
            expiration = "Never"
        max_uses = invite.max_uses
        if not max_uses:
            max_uses = "Unlimited"
        uses = invite.uses
        await ctx.respond(f"""Invite is for {name}
    Members: {member_count}, online: {online_count}, uses {uses}/{max_uses}, invite expires at {expiration}""")

    @commands.slash_command(name="modaltest")
    async def modaltest(self, ctx):
        """Shows an example of a modal dialog being invoked from a slash command."""
        modal = MyModal(title="Slash Command Modal")
        await ctx.send_modal(modal)

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(InputText(label="Short Input", placeholder="Placeholder Test"))

        self.add_item(
            InputText(
                label="Longer Input",
                value="Longer Value\nSuper Long Value",
                style=discord.InputTextStyle.long,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Your Modal Results", color=discord.Color.random())
        embed.add_field(name="First Input", value=self.children[0].value, inline=False)
        embed.add_field(name="Second Input", value=self.children[1].value, inline=False)
        await interaction.response.send_message(embeds=[embed])

def setup(bot):
    bot.add_cog(SimpleCog(bot))