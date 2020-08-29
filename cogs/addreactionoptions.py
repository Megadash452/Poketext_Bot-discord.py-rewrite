import discord
from discord.ext import commands

class Random_battle(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.add_reaction_messages = {
            'bool': [', do you accept?']
        }
        self.battle_players = {}

        #self.challenged_players[str(ctx.guild.id)] = {str(ctx.channel): {'challenger': ctx.author.id, 'challenged': member.id}}

    
    @commands.Cog.listener()
    async def on_message(self, message):
        for alias in self.add_reaction_messages['bool']:
            if message.author.id == 725225223346978816 and alias in message.content:
                await message.add_reaction('✅')
                await message.add_reaction('❌')
                break

        
        await self.client.process_commands(message)

    """
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if not user.id == 725225223346978816:
            if user.id == self.battle_players[str(user.guild.id)][str(reaction.message.channel)]['challenged']:
                if reaction.emoji == '✅':
                    # --- When batlte ends --- del battle_players[str(user.guild.id)][str(reaction.message.channel)]
                    print(reaction.emoji)

                elif reaction.emoji == '❌':
                    if user.id in self.battle_players:
                        pass

                elif reaction.emoji == '😔':
                    print(user.guild.id)
                    print(reaction.message.channel)
    """


def setup(client):
    client.add_cog(Random_battle(client))