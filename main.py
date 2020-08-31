import discord, json, random
from discord.ext import commands
from discord.utils import get
import os

from Prandom import Prandom

from Mon_data.Mon_dictionaries import Mon_dictionary as Mon_dic
from Mon_data.type_data import type_data

def read_token(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

def get_prefix(client, message):
    with open('server&user_data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return (prefixes[str(message.guild.id)], bot_ping)

client = commands.Bot(command_prefix = get_prefix)
client.remove_command('help')


# --- Global Variables ---
bot_ping = '<@!725225223346978816> '
#ban_count = {} ---goes with voteban---

battle_players = {}


# --- --- Game Functions --- ---
# --- ---


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


@client.event
async def on_reaction_add(reaction, user):
    if not user.id == 725225223346978816:
        if user.id == battle_players[str(reaction.guild.id)][str(reaction.message.channel)]['challenged']:
            if reaction.emoji == '✅':
                client.unload_extension('cogs.addreactionoptions')
                # --- When battle ends --- del battle_players[str(user.guild.id)][str(reaction.message.channel)]
                print(reaction.emoji)
                # Start battle

            elif reaction.emoji == '❌':
                if user.id in battle_players:
                    client.unload_extension('cogs.addreactionoptions')
                    print(reaction.emoji)


# --- Commands ---


# --- --- vBeta Commands (to be deleted on release) --- ----
@client.command(aliases=['forece_random', 'force_random_battle'])
async def randominit(ctx, challenged_member: discord.Member):
    Battle = Prandom(ctx.author, challenged_member)


    P1_starter = discord.Embed(title=Battle.P1.team[0].name, colour=int(type_data[Battle.P1.team[0].types[0]]['color']['hex'], 16))
    P1_starter.add_field(name=Battle.P1.team[0].poke_specie, value=Battle.P1.team[0].desc)
    if not Battle.P1.team[0].types[1]:
        P1_starter.add_field(name='Type', value=f'- {Battle.P1.team[0].types[0]}', inline=False)
    else:
        P1_starter.add_field(name='Types', value=f'{Battle.P1.team[0].types[0]}\n{Battle.P1.team[0].types[1]}', inline=False)
    P1_starter.set_image(url=Battle.P1.team[0].sprite['big']['url'])
    P1_starter.set_thumbnail(url=Battle.P1.team[0].sprite['small']['url'])

    P2_starter = discord.Embed(title=Battle.P2.team[0].name, colour=int(type_data[Battle.P2.team[0].types[0]]['color']['hex'], 16))
    P2_starter.add_field(name=Battle.P2.team[0].poke_specie, value=Battle.P2.team[0].desc)
    if not Battle.P2.team[0].types[1]:
        P2_starter.add_field(name='Type', value=f'- {Battle.P2.team[0].types[0]}', inline=False)
    else:
        P2_starter.add_field(name='Types', value=f'{Battle.P2.team[0].types[0]}\n{Battle.P2.team[0].types[1]}', inline=False)
    P2_starter.set_image(url=Battle.P2.team[0].sprite['big']['url'])
    P2_starter.set_thumbnail(url=Battle.P2.team[0].sprite['small']['url'])


    await ctx.send(f'{ctx.author.mention}\'s starter Pokemon')
    await ctx.send(embed=P1_starter)

    await ctx.send(f'{challenged_member.mention}\'s starter Pokemon')
    await ctx.send(embed=P2_starter)
# --- --- --- ---


@client.command(aliases=[bot_ping])
async def help(ctx):
    prefix = client.command_prefix(ctx.guild, ctx.message)[0]

    embed = discord.Embed(title='Help', description='Ping me or use my prefix (` {} `) to use a Command\n\n\n'.format(prefix), colour=int(type_data['PokeText']['color']['hex'], 16))

    embed.add_field(
        name='My Commands are:', 
        value='\n\t-  **setprefix <prefix>**: Changes the default prefix (*you can make the prefix pinging the bot if you want*)' +
            '\n\n\t-  **addgamechannel <channel>**: add a channel to have battles in (could be an existent or non existent channel). If there are no channels set to have battles in, the bot will just start battles in the current channel, possibly making the battle unconfortable.' +
            '\n\n\t-  **gamechannels**: a list of all game channels in the server'
            '\n\n\t-  **say <message>**: I will say whatever you tell me to (the message you send will be deleted)' +
            '\n\n\t-  **purge <message count>**: I will delete a certain number of messages' +
            '\n\n\t-  **invite**: The default link to use to invite me to one of your servers'
    )
    embed.add_field(
        name='Game Commands:',
        value='\n\n\t-  **randombattle <user>**: Starts a Pokemon match with a random team against the person you want to battle' +
            '\n\n\t-  **teambattle <user>**: Starts a Pokemon match with your current team against the person you want to battle' +
            '\n\n\t-  **teaminit**: if this is your first time using the bot, do this command to make a team (no need to do this if you already have a team in another server, as it will be automatically carried here)'
            '\n\n\t-  **team <user>**: show a person\'s team (leave empty to see your own team)' +
            '\n\n\t-  **random**: show a random pokemon' +
            '\n\n\t-  **info <pokemon>**: show the information of a certain pokemon (you can also do {}info random to show a random Pokémon)'.format(prefix)
    )
    embed.add_field(
        name='Game Management Commands:',
        value='\n\n\t-  **ban <user> <reason(optional)>**: Will delete an user\'s team data and will prevent them from creating a team (undo with *`{}`unban*)'.format(prefix) +
            #'\n\n\t-  **voteban <user>**: If a total of `10` members use this command, the specified user will be banned from usign this bot' +
            '\n\n\t-  **banlist**: See all the users that have been banned'
    )

    await ctx.send(embed=embed)


@client.command(aliases=['set-prefix', 'set_prefix'])
@commands.has_permissions(administrator=True)
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


@client.command(aliases=['add_game_channel', 'add-game-channel', 'add_gamechannel', 'add-gamechannel'])
@commands.has_permissions(manage_channels=True)
async def addgamechannel(ctx, channel=None):
    with open('server&user_data/game_channels.json', 'r') as f:
        game_channels = json.load(f)

    guild_channels = []

    if not channel:
        chann = str(ctx.channel)
    else:
        chann = channel

    for chan in ctx.guild.channels:
        guild_channels.append(chan.name)

    if chann in game_channels[str(ctx.guild.id)]:
        await ctx.send('This channel has already been added to game channels')

    elif chann in guild_channels:
        if not str(ctx.guild.id) in game_channels:
            game_channels[str(ctx.guild.id)] = [chann]
        else:
            game_channels[str(ctx.guild.id)].append(chann)

        with open('server&user_data/game_channels.json', 'w') as f:
            json.dump(game_channels, f, indent=4)

        await ctx.send('Added **{}** to game channels'.format(chann))
    
    elif not chann in ctx.guild.channels:
        await ctx.send('creating channel **{}**'.format(chann))
        print('create channel')


@client.command()
@commands.has_permissions(manage_messages=True)
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


@client.command(aliases=['random-battle', 'random_battle', 'randbattle', 'rand-battle'])
async def randombattle(ctx, member : discord.Member):
    with open('server&user_data/game_channels.json', 'r') as f:
        game_channels = json.load(f)
    
    if str(ctx.channel) in game_channels[str(ctx.guild.id)]:
        if not str(ctx.guild.id) in battle_players:
            battle_players[str(ctx.guild.id)] = {str(ctx.channel): {'challenger': '', 'challenged': ''}}

            if not member in battle_players[str(ctx.guild.id)][str(ctx.channel)]['challenged']:
                if not ctx.author.id == member.id:
                    await ctx.send('Starting Random Battle with {}'.format(member.display_name))
                    print('Starting Random Battle with <@{}> in server --{}--'.format(member.id, ctx.guild))

                    client.load_extension('cogs.addreactionoptions')

                    #battle_players[str(ctx.guild.id)] = {str(ctx.channel): {'challenger': ctx.author, 'challenged': member}}

                    await ctx.channel.send('{}, do you accept?'.format(member.mention))

                    print(battle_players)
                
                else:
                    await ctx.send('You can\'t battle yourself')
            else:
                await ctx.send('This person is already in battle with someone else. Please wait until they are finished')
        else:
            await ctx.send('People are already battling here. Please use another channel')

    elif not str(ctx.channel) in game_channels[str(ctx.guild.id)]:
        await ctx.send('Cannot have a battle in this channel. Please go to a channel designated for battles (you can check what those channels are by using command `{}`gamechannels)'.format(client.command_prefix(ctx.guild, ctx.message)[0]))



@client.command(aliases=['team-battle'])
async def teambattle(ctx, member):
    pass


@client.command(aliases=['team-init', 'team_init'])
async def teaminit(ctx):
    pass


@client.command()
async def team(ctx, member):
    pass


@client.command(aliases=['random'])
async def rand(ctx):
    random_num = random.randrange(1, 50+1, 1)

    embed = discord.Embed(title=Mon_dic[random_num].name, colour=int(type_data[Mon_dic[random_num].types[0]]['color']['hex'], 16))

    embed.add_field(name=Mon_dic[random_num].poke_specie, value=Mon_dic[random_num].desc)

    if not Mon_dic[random_num].types[1]:
        embed.add_field(name='Type', value=f'{Mon_dic[random_num].types[0]}', inline=False)
    else:
        embed.add_field(name='Types', value=f'{Mon_dic[random_num].types[0]}\n{Mon_dic[random_num].types[1]}', inline=False)

    embed.set_image(url=Mon_dic[random_num].sprite['big']['url'])
    embed.set_thumbnail(url=Mon_dic[random_num].sprite['small']['url'])

    embed.set_footer(text=f'weaknesses: \n{Mon_dic[random_num].get_w_s_str("weaknesses")}\n\nstrengths: \n{Mon_dic[random_num].get_w_s_str("strengths")}')
    

    await ctx.send(embed=embed)


@client.command()
async def info(ctx, *, mon):
    if not mon == 'random':
        try:
            int(mon) + 1
            call = int(mon)
        except:
            from Mon_data.Mon_dictionaries import Number_dictionary as Dic
            call = int(Dic[mon.lower()])
    else:
        call = random.randrange(1, 50+1, 1)

    embed = discord.Embed(title=Mon_dic[call].name, colour=int(type_data[Mon_dic[call].types[0]]['color']['hex'], 16))

    embed.add_field(name=Mon_dic[call].poke_specie, value=Mon_dic[call].desc)

    if not Mon_dic[call].types[1]:
        embed.add_field(name='Type', value=f'- {Mon_dic[call].types[0]}', inline=False)
    else:
        embed.add_field(name='Types', value=f'{Mon_dic[call].types[0]}\n{Mon_dic[call].types[1]}', inline=False)

    embed.set_image(url=Mon_dic[call].sprite['big']['url'])
    embed.set_thumbnail(url=Mon_dic[call].sprite['small']['url'])

    embed.set_footer(text=f'strengths: \n{Mon_dic[call].get_w_s_str("strengths")}\n\nweaknesses: \n{Mon_dic[call].get_w_s_str("weaknesses")}')
    

    await ctx.send(embed=embed)
    #await ctx.send(' <a:1717_Crab_Rave:626579304049803294> ')


# --- Game Management Commands ---


@client.command(aliases=['pokeban', 'poke-ban', 'poke ban'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, banmember=None, *, reason=None):
    with open('server&user_data/user_banlist.json', 'r') as f:
        user_banlist = json.load(f)

    member = ''

    for char in banmember:
        if not char in '!&':
            member += char

    if not member:
        await ctx.send('Who are you going to ban? Try again')

    elif not member in user_banlist:
        user_banlist.append(member)

        with open('server&user_data/user_banlist.json', 'w') as f:
            json.dump(user_banlist, f, indent = 4)

        #delete their team
        
        await ctx.send(f'{member}\'s team has been deleted and they will no longer be able to create another one')
        print(f'banmember: {banmember}')
        print(f'member: {member}')
    
    else:
        await ctx.send('This user has already been banned from playing, silly')


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, banmember=None):
    with open('server&user_data/user_banlist.json', 'r') as f:
        user_banlist = json.load(f)

    member = ''

    for char in banmember:
        if not char in '!&':
            member += char

    if not member:
        await ctx.send('Who are you going to unban? Try again')

    elif not member in user_banlist:
        await ctx.send('This user hasn\'t been banned, silly')

    else:
        user_banlist.remove(member)

        with open('server&user_data/user_banlist.json', 'w') as f:
            json.dump(user_banlist, f, indent = 4)

        await ctx.send(f'unbanned {member}. You can now create a new team and start on a new slate')
        print(f'banmember: {banmember}')
        print(f'member: {member}')

"""
@client.command(aliases=['vote-pokeban', 'vote-poke-ban'])
async def voteban(ctx, banmember=None):
    with open('server&user_data/user_banlist.json', 'r') as f:
            user_banlist = json.load(f)

    member = ''
    author = ''
    voters = []

    for char in banmember:
        if not char in '!&':
            member += char

    if not member:
        await ctx.send('Who are you voting to ban? Try again')

    elif not member in user_banlist:
        try:
            ban_count[str(ctx.guild.id)][member]
        except:
            ban_count[str(ctx.guild.id)] = {}
            ban_count[str(ctx.guild.id)][member] = 0

        ban_count[str(ctx.guild.id)][member] += 1
        voters.append(str(ctx.author.id))

        await ctx.send(f'{ban_count[str(ctx.guild.id)][member]} users have voted to ban {member}. Let\'s get to 10!')
        print(voters)

        if ban_count[str(ctx.guild.id)][member] == 10:
            user_banlist.append(member)

            with open('server&user_data/user_banlist.json', 'w') as f:
                json.dump(user_banlist, f, indent = 4)

            #delete their team

            await ctx.send(f'{member}\'s team has been deleted and they will no longer be able to create another one')

    elif member in user_banlist:
        await ctx.send('This user has already been banned from playing, silly')
        print(member)
"""

@client.command()
async def banlist(ctx):
    with open('server&user_data/user_banlist.json', 'r') as f:
            user_banlist = json.load(f)

    return_str = ''

    for char in user_banlist:
        if not char in '<>[]\'':
            return_str += char

    await ctx.send(user_banlist)
# --- ---

"""
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
"""

client.run(read_token('token.txt'))