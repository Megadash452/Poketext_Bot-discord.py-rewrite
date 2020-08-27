import Mon_data.Mon_dictionaries
import random


class Pokemon(Mon_data.Mon_dictionaries.Mon):
    def __init__(self, number):
        self.number = number
        self.Mon = Mon_data.Mon_dictionaries.Mon_dictionary[self.number]
        self.name = self.Mon.name

        self.poke_specie = self.Mon.poke_specie
        self.desc = self.Mon.desc

        self.types = self.Mon.types
        self.strengths = self.Mon.strengths
        self.weaknesses = self.Mon.weaknesses

        self.ability = self.get_ability()

        self.stats = self.Mon.stats

        self.sprite = self.Mon.sprite

    def get_ability(self):
        if not self.Mon.abilities[1]:
            return self.Mon.abilities[0]
        else:
            return self.Mon.abilities[random.randrange(0, 2, 1)]


class Player:
    def __init__(self, user_name, user_id, backpack):
        self.user_name = user_name
        self.user_id = user_id
        self.team = {}

        for index in range(6):
            self.team[index] = Pokemon(random.randrange(1, 105+1, 1))

        self.backpack = backpack

def initiate_random(author, challenged):
    Player1 = Player(author.display_name, author.id,
        backpack = {

        }
    )