import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Entrei como in as {0.user}'.format(client))


@client.command(name='hey')
async def _hey(ctx, arg):
    await ctx.send('hey')




client.run('')
