import json
import discord
from discord.ext import commands

def read_token(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

prefix = '!'

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

bot_ping = '<@!725225223346978816>'


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

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

@client.command(aliases=['set prefix', 'set-prefix', 'setprefix'])
async def set_prefix(ctx, prefix=None):
    if prefix:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent = 4)

        await ctx.send('This server\'s prefix is now {}'.format(prefix))
        print('changed server {}\'s prefix to {}'.format(ctx.guild.id, prefix))
    else:
        await ctx.send('What would you like the prefix to be?')
        #add chain

@client.command()
async def purge(ctx, amount=6):
    await ctx.channel.purge(limit=amount + 1)
    print('deleted {} messages'.format(amount))

@client.command(aliases=['pokeban', 'poke-ban', 'poke ban'])
async def ban(ctx, member):
    print()

@client.command(aliases=['vote-pokeban', 'vote-poke-ban', 'vote pokeban', 'vote poke-ban'])
async def voteban(ctx, member=''):
    if member:
        await ctx.send(f'going to ban {member} :angry:')
    else:
        await ctx.send('Who you gonna ban thoe? Try again')

@client.command(aliases=['show all pokemon'])
async def showall(ctx):
    embed = discord.Embed(
        title='All 151 Pokemon (1st gen)',
        description='what',
        colour=discord.Colour.from_rgb(255, 216, 35)#ffd823
    )

    embed.set_footer(text='yes')
    embed.set_image(url='https://cdn.discordapp.com/attachments/691380666646003733/746089018747518996/gen1pokemon_sprites.png')

    await ctx.send(embed=embed)

@client.command()
async def say(ctx, *, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(message)
# --- ---


client.run(read_token('token.txt'))