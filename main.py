import discord
from discord.ext import commands

def read_token(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token('token.txt')

client = commands.Bot(command_prefix = '!')

bot_ping = '<@!725225223346978816>'

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

client.run()