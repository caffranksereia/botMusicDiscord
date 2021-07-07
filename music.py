import discord
from discord.ext import commands


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send('nao esta em lugar algum')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_channel.disconnect()
    
    @commands.command()
    async def play(self, ctx, url):
        FFMPEG_OPTIONS = {

        }

    def setup(client):
        client.add_cog(music(client))