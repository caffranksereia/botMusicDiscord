import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')#Token recebe o token criado no arquivo .env DISCORD_TOKEN
GUILD = os.getenv('DISCORD_GUILD')#Guild recebe o DISCORD_GUILD NO arquivo .env DISCORD_GUILD


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())










'''
for i in range(len(cogs)):
    cogs[i].setup(client)'''



@client.event
async def on_ready():
# print no cmd id_guild e id client_user
 for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(f'Entrei {client.user} para acabar com seus ouvidos \n {guild.name} (id:{guild.id})')


@client.command()
async def hey(ctx):
    await ctx.send('hey! dude')

@client.command()
async  def joined(ctx):
    await ctx.author.voice.channel.connect()
    await ctx.send("hey! im here")


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("bye")




client.run(TOKEN) #cliente roda recebendo o paramentro do TOKEN que foi recebido la em cima.
