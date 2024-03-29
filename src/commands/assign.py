import discord
from discord.ext import commands
from locals import *


class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def assign(self, ctx, subject: str):
        if (
            subject.upper() in TUTOR_ROLES.keys()
            and ctx.guild.get_role(BANNED_ASSIGN_TUTOR_ROLE) not in ctx.author.roles
        ):
            if ctx.guild.get_role(MAIN_TUTOR_ROLE) not in ctx.author.roles:
                await ctx.author.add_roles(ctx.guild.get_role(MAIN_TUTOR_ROLE))

            await ctx.author.add_roles(ctx.guild.get_role(TUTOR_ROLES[subject.upper()]))
            await ctx.send(f"You became a {subject} tutor!")
        elif ctx.guild.get_role(BANNED_ASSIGN_TUTOR_ROLE) in ctx.author.roles:
            await ctx.send("It seems that you're not allowed to become a tutor.")
        else:
            await ctx.send(
                f"That's an invalid tutor role\nHere are the avaliable roles: ``{', '.join(TUTOR_ROLES.keys())}``"
            )


def setup(bot):
    bot.add_cog(sessions(bot))
