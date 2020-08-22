import json
import discord
from discord.ext import commands

from Pokemon_dictionaries import Pokemon_dictionary as Pokemon
from type_colors import get_type_color

def read_token(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)
client.remove_command('help')

bot_ping = '<@!725225223346978816>'


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '/'

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
async def help(ctx):
    prefix = client.command_prefix(ctx.guild, ctx.message)

    #embed = discord.Embed(title='Help' colour=discord.Colour.from_rgb(get_type_color['PokeText'][0], get_type_color['PokeText'][1], get_type_color['PokeText'][2]),
                            #)

    await ctx.send('Ping me or use my prefix ({}) to use a Command\n'.format(prefix)+
                'My Commands are:'+
                '\n\t-  **setprefix <prefix>**: Changes the default prefix (*you can make the prefix pinging the bot if you want*)'+
                '\n\t-  **say <message>**: I will say whatever you tell me to (the message you sedn will be deleted)'+
                '\n\t-  **purge <message count>**: I will delete a certain number of messages'+

                'Game commands:'+
                '\n\t-  **random battle <user>**: Starts a Pokemon match with a random team against '+
                'the person you want to battle'+
                '\n\t-  **random**: show a random pokemon'+
                '\n\t-  **team battle <user>**: Starts a Pokemon match with your current team against '+
                'the person you want to battle'+
                '\n\t-  **team**: show your current team'+
                '\n\t-  **info <pokemon>**: show the information of a certain pokemon'+

                'Game management commands:'+
                '\n\t-  ****:'+
                '\n\t-  ****:'+
                '\n\t-  ****:'+
                '\n\t-  ****:'+
                '\n\t-  ****:')


@client.command(aliases=['set-prefix', 'set_prefix'])
async def setprefix(ctx, prefix=None):
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


@client.command()
async def say(ctx, *, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(message)


@client.command()
async def invite(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=725225223346978816&permissions=104161089&scope=bot')


@client.command()
async def info(ctx, *, mon):
    try:
        int(mon) + 1
        call = int(mon)
    except:
        from Pokemon_dictionaries import Number_dictionary as Dic
        call = int(Dic[mon.lower()])

    embed = discord.Embed(title=Pokemon[call].name, colour=int(get_type_color(Pokemon[call].types[0], 'hex'), 16))

    embed.add_field(name=Pokemon[call].poke_specie, value=Pokemon[call].desc)

    if not Pokemon[call].types[1]:
        embed.add_field(name='Type', value=Pokemon[call].types[0], inline=False)
    else:
        embed.add_field(name='Types', value=f'{Pokemon[call].types[0]}\n{Pokemon[call].types[1]}', inline=False)

    embed.set_image(url=Pokemon[call].sprite['big']['url'])
    #embed.set_thumbnail(url=Pokemon[call].sprite['small']['url'])
    

    await ctx.send(embed=embed)


@client.command(aliases=['pokeban', 'poke-ban', 'poke ban'])
async def ban(ctx, member):
    print()


@client.command(aliases=['vote-pokeban', 'vote-poke-ban'])
async def voteban(ctx, member=''):
    if member:
        await ctx.send(f'going to ban {member} :angry:')
    else:
        await ctx.send('Who you gonna ban thoe? Try again')

# --- ---


client.run(read_token('token.txt'))