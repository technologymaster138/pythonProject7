import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'r!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Gurou's tail"))
    print('Bot is ready.')

client.run('')
