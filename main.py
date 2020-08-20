import json
import discord
from discord.ext import commands

def read_token(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

prefix = '!'

print(read_token('token.txt'))

client = commands.Bot(command_prefix = prefix)

bot_ping = '<@!725225223346978816>'

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print('{} has joined one of the servers'.format(member))

@client.event
async def on_member_remove(member):
    print('{} member has left a server'.format(member))
    #delete the member's pokemon data


# --- Commands ---
@client.command(aliases=[bot_ping])
async def ping(ctx):
    await ctx.send('Hello there, (my prefix is ' + prefix + '). Do ' + prefix + 'help to see what you can do')
# --- ---


client.run(read_token('token.txt'))