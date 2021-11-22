import discord
from discord.ext import commands

class Check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Check Status Loaded Succesfully')

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong {ctx.author.mention}')



def setup(bot):
    bot.add_cog(Check(bot))