import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')#Token recebe o token criado no arquivo .env DISCORD_TOKEN
GUILD = os.getenv('DISCORD_GUILD')#Guild recebe o DISCORD_GUILD NO arquivo .env DISCORD_GUILD

client = discord.Client()
client = discord.commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
# print no cmd id_guild e id client_user
 for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(f'Entrei {client.user} para acabar com seus ouvidos \n {guild.name} (id:{guild.id})')

@client.event
#async função é ativado com !hey no discord
async def on_message(message):#assincronia mensagem recebe o paramentro message
    if message.author == client.user: #message autor é igual ao mensagem cliente
        return #retorna nada
    if message.content.startswith('!hey'):#message começa com !hey
        await message.channel .send(f'hey, its me {client.user} vou acabar com seus ouvidos')#retorna essa frase.

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

client.run(TOKEN) #cliente roda recebendo o paramentro do TOKEN que foi recebido la em cima.
