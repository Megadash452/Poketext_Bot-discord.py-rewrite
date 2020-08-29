import discord
from discord.ext import commands

class Random_battle(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.add_reaction_messages = [', do you accept?', 'yee haw']
        self.challenged_players = {}

        #self.challenged_players[str(ctx.guild.id)] = {str(ctx.channel): {'challenger': ctx.author.id, 'challenged': member.id}}

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 725225223346978816:
            await message.add_reaction('✅')
            await message.add_reaction('❌')

        await self.client.process_commands(message)


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if not user.id == 725225223346978816:
            if reaction.emoji == '✅':
                if user.id in self.challenged_players:
                    print(reaction.emoji)

            elif reaction.emoji == '❌':
                if user.id in self.challenged_players:
                    print(reaction.emoji)


def setup(client):
    client.add_cog(Random_battle(client))