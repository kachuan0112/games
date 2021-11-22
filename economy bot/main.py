
import discord
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
import os
import json
import random

client = commands.Bot(command_prefix='xuan.')

client.remove_command("help")

status = cycle(
    ['Try xuan.help','prefix : xuan.'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('token')