import random
import discord
import Pokemon_dictionaries
from Pokemon_dictionaries import pokemon

pok_num = Pokemon_dictionaries.total_num_of_pokemon - 1


class player:
    def __init__(self, team, items, badges, pokemon):
        self.team = team
        self.items = items
        self.badges = badges
        self.pokemon = pokemon


def post():
    print('PokeText random game: Function post() found and executed')


def start():
    print('random game will start')
    # --- Write game code HERE ---


user1_team = [
    Pokemon_dictionaries.Pokemon_dictionary[random.randint(1, Pokemon_dictionaries.pokemon.total_num_of_pokemon)],
    Pokemon_dictionaries.Pokemon_dictionary[random.randint(1, Pokemon_dictionaries.pokemon.total_num_of_pokemon)],
    Pokemon_dictionaries.Pokemon_dictionary[random.randint(1, Pokemon_dictionaries.pokemon.total_num_of_pokemon)],
    Pokemon_dictionaries.Pokemon_dictionary[random.randint(1, Pokemon_dictionaries.pokemon.total_num_of_pokemon)],
    Pokemon_dictionaries.Pokemon_dictionary[random.randint(1, Pokemon_dictionaries.pokemon.total_num_of_pokemon)],
    Pokemon_dictionaries.Pokemon_dictionary[random.randint(1, Pokemon_dictionaries.pokemon.total_num_of_pokemon)],
]

player1 = player(user1_team, 'items will be assigned', 'you currently have no badges', 'you have no pokemon')

print(player1.team)


def num_for_ran_gen():
    return random.randint(1, Pokemon_dictionaries.pokemon.total_num_of_pokemon)


def random_generator():
    num_for_ran_gen()
    return Pokemon_dictionaries.Pokemon_dictionary[num_for_ran_gen()]


def end_battle(winner):
    message = winner + 'has won'


end_battle('cbt')

print(user1_team)
