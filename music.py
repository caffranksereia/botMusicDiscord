import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.is_playing = False

        self.music_queue = []
        self. YDL_OPTIONS = {'format':'bestaudio','noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}

        self.vc = ""

    def yt_search(self,item):
        with YoutubeDL(self.YDL_OPTIONS)as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s"% item,download=False)['entries'][0]
            except Exception:
                return False

        return {'source':info['formats'][0]['url'],'title':info['title']}
    def nextp(self):
        if len(self.music_queue)>0:
            self.music_queue = True

            m_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after = lambda e : self.nextp())
        else:
            self.is_playing = False


    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']



            if self.vc =="" or not self.vc.is_connect() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                self.vc = await self.client.move_to(self.music_queue[0][1])

            print(self.music_queue)

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.nextp())
        else:
            self.is_playing = False

    @commands.command(name="play", help="Plays a selected song from youtube")
    async def m(self,ctx,*args):
        query = "".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send('Precisar estar em um voice')
        else:
            song = self.yt_search(query)
            if type(song) == type(True):
                await ctx.send("not download")
            else:
                await ctx.send("add queue")
                self.music_queue.append([song,voice_channel])

                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="queue", help="Displays the current songs in queue")
    async def q(self,ctx):
        retval = ""
        for i in range(0,len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] +"\n"
        print(retval)
        if retval !="":
            await ctx.send(retval)
        else:
            await ctx.send("no music in queue")

    @commands.command(name="skip", help="Skips the current song being played")
    async def skip(self,ctx):
        if self.vc !="" and self.vc:
            self.vc.stop()
            await self.play_music()

    '''while i < client:
        music = input("music:")
        i += 1
'''

    

def setup(client):
        client.add_cog(music(client))