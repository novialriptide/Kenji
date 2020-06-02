import discord
import time
from discord.ext import commands
from vars import *

class ban_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str):
        if ctx.message.author.id in MEMBERS_WITH_PERMS or ctx.message.author == ctx.message.guild.owner:
            channel = ctx.message.channel
            embed=discord.Embed(
                color=0xff0000, 
                title=f"Ban Executed: [{member}] by {ctx.message.author}",
                description=f"Reason: {reason}"
            )
            await channel.send(embed=embed)
            channel = self.client.get_channel(JOIN_LEAVE_CHANNEL)
            await channel.send(embed=embed)

            embed=discord.Embed(
                color=0xff0000, 
                title=f"You have been banned by {ctx.message.author} in {ctx.message.guild}",
                description=f"Reason: {reason}"
            )
            await member.send(embed=embed)
            await member.ban(delete_message_days=0, reason=reason)

            channel = self.client.get_channel(LOGGING_CHANNEL)
            await channel.send(embed=embed)
        else:
            channel = ctx.message.channel
            await channel.send(f"You do not have permission to do that, {ctx.message.author}...")
            channel = self.client.get_channel(LOGGING_CHANNEL)
            embed=discord.Embed(
                color=0xff0000, 
                title=f"Ban Attempt: [{member}] by {ctx.message.author}",
                description=f"Reason: {reason}"
            )
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ban_cmd(bot))