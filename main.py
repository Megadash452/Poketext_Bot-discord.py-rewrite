import discord, json, random
from discord.ext import commands
from discord.utils import get

from Mon_data.Pokemon_dictionaries import Pokemon_dictionary as Pokemon_dic
from Mon_data.type_data import type_data

def read_token(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

bot_ping = '<@!725225223346978816> '

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return (prefixes[str(message.guild.id)], bot_ping)

client = commands.Bot(command_prefix = get_prefix)
client.remove_command('help')


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
    print('{} has joined server "{}"'.format(member, member.guild))

@client.event
async def on_member_remove(member):
    print('{} member has server "{}"'.format(member, member.guild))
    #delete the member's pokemon data


# --- Commands ---
@client.command(aliases=[bot_ping])
async def help(ctx):
    prefix = client.command_prefix(ctx.guild, ctx.message)[0]

    embed = discord.Embed(title='Help', description='Ping me or use my prefix (` {} `) to use a Command\n\n\n'.format(prefix), colour=int(type_data['PokeText']['color']['hex'], 16))

    embed.add_field(
        name='My Commands are:', 
        value='\n\t-  **setprefix <prefix>**: Changes the default prefix (*you can make the prefix pinging the bot if you want*)' +
            '\n\n\t-  **say <message>**: I will say whatever you tell me to (the message you sedn will be deleted)' +
            '\n\n\t-  **purge <message count>**: I will delete a certain number of messages' +
            '\n\n\t-  **invite**: The dewfault link to use to invite me to one of your servers'
    )
    embed.add_field(
        name='Game Commands:',
        value='\n\n\t-  **randombattle <user>**: Starts a Pokemon match with a random team against the person you want to battle' +
            '\n\n\t-  **teambattle <user>**: Starts a Pokemon match with your current team against the person you want to battle' +
            '\n\n\t-  **teaminit**- if this is your first time using the bot, do this command to make a team'
            '\n\n\t-  **team <user>**: show a person\'s team (leave empty to see your own team)' +
            '\n\n\t-  **random**: show a random pokemon' +
            '\n\n\t-  **info <pokemon>**: show the information of a certain pokemon (you can also do {}info random to show a random Pokémon'.format(prefix)
    )
    embed.add_field(
        name='Game Management Commands:',
        value='\n\n\t-  **ban**:' +
            '\n\n\t-  **voteban**:'
    )

    await ctx.send(embed=embed)


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
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=725225223346978816&permissions=37584704&scope=bot')


# --- Game Commands ---


@client.command(aliases=['random-battle', 'randbattle', 'rand-battle'])
async def randombattle(ctx, member : discord.Member):
    await ctx.send('starting Random Battle with {}'.format(member.mention))
    print('starting Random Battle with {}'.format(member.mention))


@client.command(aliases=['team-battle'])
async def teambattle(ctx, member):
    pass

@client.command()
async def team(ctx, member):
    pass

@client.command(aliases=['random'])
async def rand(ctx):
    random_num = random.randrange(1, 50+1, 1)

    embed = discord.Embed(title=Pokemon_dic[random_num].name, colour=int(type_data[Pokemon_dic[random_num].types[0]]['color']['hex'], 16))

    embed.add_field(name=Pokemon_dic[random_num].poke_specie, value=Pokemon_dic[random_num].desc)

    if not Pokemon_dic[random_num].types[1]:
        embed.add_field(name='Type', value=Pokemon_dic[random_num].types[0], inline=False)
    else:
        embed.add_field(name='Types', value=f'{Pokemon_dic[random_num].types[0]}\n{Pokemon_dic[random_num].types[1]}', inline=False)

    embed.set_image(url=Pokemon_dic[random_num].sprite['big']['url'])
    embed.set_thumbnail(url=Pokemon_dic[random_num].sprite['small']['url'])

    embed.set_footer(text='weaknesses: \n \n\nstrengths: \n ')
    

    await ctx.send(embed=embed)


@client.command()
async def info(ctx, *, mon):
    if not mon == 'random':
        try:
            int(mon) + 1
            call = int(mon)
        except:
            from Mon_data.Pokemon_dictionaries import Number_dictionary as Dic
            call = int(Dic[mon.lower()])
    else:
        call = random.randrange(1, 50+1, 1)

    embed = discord.Embed(title=Pokemon_dic[call].name, colour=int(type_data[Pokemon_dic[call].types[0]]['color']['hex'], 16))

    embed.add_field(name=Pokemon_dic[call].poke_specie, value=Pokemon_dic[call].desc)

    if not Pokemon_dic[call].types[1]:
        embed.add_field(name='Type', value=Pokemon_dic[call].types[0], inline=False)
    else:
        embed.add_field(name='Types', value=f'{Pokemon_dic[call].types[0]}\n{Pokemon_dic[call].types[1]}', inline=False)

    embed.set_image(url=Pokemon_dic[call].sprite['big']['url'])
    embed.set_thumbnail(url=Pokemon_dic[call].sprite['small']['url'])

    embed.set_footer(text=f'weaknesses: \n{Pokemon_dic[call].get_w_s_str("weaknesses")}\n\nstrengths: \n{Pokemon_dic[call].get_w_s_str("strengths")}')
    

    await ctx.send(embed=embed)
    #await ctx.send(' <a:1717_Crab_Rave:626579304049803294> ')


# --- Game Management Commands ---


@client.command(aliases=['pokeban', 'poke-ban', 'poke ban'])
async def ban(ctx, member):
    print()


@client.command(aliases=['vote-pokeban', 'vote-poke-ban'])
async def voteban(ctx, member=''):
    if member:
        await ctx.send(f'going to ban {member} from playing :angry:')
    else:
        await ctx.send('Who you gonna ban thoe? Try again')

# --- ---


client.run(read_token('token.txt'))