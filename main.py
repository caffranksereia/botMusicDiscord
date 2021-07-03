import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()
client = discord.commands.Bot(command_prefix = "!")

@client.event
async def on_ready():


    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'Entrei {client.user} para acabar com seus ouvidos \n {guild.name} (id:{guild.id})')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hey'):
        await message.channel .send(f'hey, its me {client.user} vou acabar com seus ouvidos')

'''@client.event
async def join_us(message):
    if message.author == client.user:
        return
    if message.content.startswith('!join'):
        channel ='''

'''@client.event
async  def join_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('join'):'''
'''@client.commands
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await ctx.join_voice_channel(channel)
@client.commands()
async def leave(ctx):
    await ctx.voice_client.disconnect()'''

client.run(TOKEN)
