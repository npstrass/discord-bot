import os
import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='.', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

my_secret = os.environ['NEW_TOKEN']

client.run(my_secret)
