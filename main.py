import json
import Discord
from Discord.ext import commands 

with open("config.json") as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefix = infos['prefix']

client = commands.Bot(command_prefix = prefix, 
                        intents = Discord.Intents.all())

client.run(TOKEN)