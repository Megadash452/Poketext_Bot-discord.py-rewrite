class item:
    def __init__(self, name, type):
        self.name = name
        self.type = type


def get_type_color(Type, index=-1):
    type_colors = {
        #color format: RGB
        #get color from: 
        'Normal': (),
        'Fire': (253, 125, 36),
        'Fighting': (),
        'Water': (),
        'Flying': (),
        'Grass': (155, 204, 80),
        'Poison': (),
        'Electric': (),
        'Ground': (),
        'Psychic': (),
        'Rock': (),
        'Ice': (),
        'Bug': (),
        'Dragon': (),
        'Ghost': (),
        'Dark': (),
        'Steel': (),
        'Fairy': (),
        '???': (),
    }

    if index == -1:
        return type_colors[Type]
    else:
        return type_colors[Type][index]


class pokemon:
    total_num_of_pokemon = 0

    def __init__(self, num, name, poke_specie, desc, types, ability, stats):
        self.num = num
        self.name = name
        self.poke_specie = poke_specie
        self.desc = desc
        self.types = types
        self.ability = ability
        self.stats = stats

        self.sprite = {
                    'small': {
                        'url': 'https://raw.githubusercontent.com/Megadash452/Poketext_Bot-discord.py-rewrite/master/pokemon-sprites/gen1-small/{}-small.png'.format(self.name),
                        'path': 'pokemon-sprites/gen1-small/{}-small.png'.format(self.name)
                   },

                   'big': {
                       'url': 'https://raw.githubusercontent.com/Megadash452/Poketext_Bot-discord.py-rewrite/master/pokemon-sprites/gen1-big/{}-big.png'.format(self.name),
                       'path': 'pokemon-sprites/gen1-big/{}-big.png'.format(self.name)
                   }
        }

        pokemon.total_num_of_pokemon += 1


    def attack(self):
        print(self.name + ' has attacked')

    def faint(self):
        print(self.name + ' has attacked')


# ------ Dictionary ------ ------ ------ ------ ------ ------ ------ ------ ------

Pokemon_dictionary = {
    1: pokemon(1, 'Bulbasaur', 'Seed Pokémon',
               'There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger.',
               ('Grass', 'Poison'), 'Overgrowth',
               
               stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    2: pokemon(2, 'Ivysaur', 'Seed Pokémon',
               'When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.',
               ('Grass', 'Poison'), 'Overgrowth',

               stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    3: pokemon(3, 'Venusaur', 'Seed Pokémon',
               'Its plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.',
               ('Grass', 'Poison'), 'Overgrowth',

               stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    4: pokemon(4, 'Charmander', 'Lizard Pokémon',
               'It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.',
               ('Fire'), 'Blaze',

               stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    5: 'Charmeleon',

    6: 'Charizard',

    7: 'Squirtle',

    8: 'Wartotle',

    9: 'Blastoise',

    10: 'Caterpie',

    11: 'Metapod',

    12: 'Butterfree',

    13: 'Weedle',

    14: 'Kakuna',

    15: 'Beedrill',

    16: 'Pidgey',

    17: 'Pidgeotto',

    18: 'Pidgeot',

    19: 'Rattata',

    20: 'Raticate',

    21: 'Spearow',

    22: 'Fearow',

    23: 'Ekans',

    24: 'Arbok',

    25: 'Pikachu',

    26: 'Raichu',

    27: 'Sandshrew',

    28: 'Sandslash',

    29: 'Nidoran♀',

    30: 'Nidorina',

    31: 'Nidoqueen',

    32: 'Nidoran♂',

    33: 'Nidorino',

    34: 'Nidoking',

    35: 'Clefairy',

    36: 'Clefable',

    37: 'Vulpix',

    38: 'Ninteales',

    39: 'Jigglypuff',

    40: 'Wigglytuff',

    41: 'Zubat',

    42: 'Golbat',

    43: 'Oddish',

    44: 'Gloom',

    45: 'Vileplume',

    46: 'Paras',

    47: 'Parasect',

    48: 'Venonat',

    49: 'Venomoth',

    50: 'Diglett',

    51: 'Dugtrio',

    52: 'Meowth',

    53: 'Persian',

    54: 'Psyduck',

    55: 'Golduck',

    56: 'Mankey',

    57: 'Primeape',

    58: 'Growlithe',

    59: 'Arcanine',

    60: 'Poliwag',

    61: 'Poliwhirl',

    62: 'Poliwrath',

    63: 'Abra',

    64: 'Kadabra',

    65: 'Alakazam',

    66: 'Machop',

    67: 'Machoke',

    68: 'Machamp',

    69: 'Bellsprout',

    70: 'Weepinbell',

    71: 'Victreebel',

    72: 'Tentacool',

    73: 'Tentacruel',

    74: 'Geodude',

    75: 'Graveler',

    76: 'Golem',

    77: 'Ponyta',

    78: 'Rapidash',

    79: 'Slowpoke',

    80: 'Slowbro',

    81: 'Magnemite',

    82: 'Magneton',

    83: 'Farfetch\'d',

    84: 'Doduo',

    85: 'Dodrio',

    86: 'Seel',

    87: 'Dewgong',

    88: 'Grimer',

    89: 'Muk',

    90: 'Shellder',

    91: 'Cloyster',

    92: 'Gastly',

    93: 'Haunter',

    94: 'Gengar',

    95: 'Onix',

    96: 'Drowzee',

    97: 'Hypno',

    98: 'Krabby',

    99: 'Kingler',

    100: 'Voltorb',

    101: 'Electrode',

    102: 'Exeggcute',

    103: 'Exeggutor',

    104: 'Cubone',

    105: 'Marowak',

    106: 'Hitmonlee',

    107: 'Hitmonchan',

    108: 'Lickitung',

    109: 'Koffing',

    110: 'Weezing',

    111: 'Rhyhorn',

    112: 'Rhydon',

    113: 'Chansey',

    114: 'Tangela',

    115: 'Kangaskhan',

    116: 'Horsea',

    117: 'Seadra',

    118: 'Goldeen',

    119: 'Seaking',

    120: 'Staryu',

    121: 'Starmie',

    122: 'Mr. Mime',

    123: 'Scyther',

    124: 'Jynx',

    125: 'Electabuzz',

    126: 'Magmar',

    127: 'Pinsir',

    128: 'Tauros',

    129: 'Magikarp',

    130: 'Gyarados',

    131: 'Lapras',

    132: 'Ditto',

    133: 'Eevee',

    134: 'Vaporeon',

    135: 'Jolteon',

    136: 'Flareon',

    137: 'Porygon',

    138: 'Omanyte',

    139: 'Omastar',

    140: 'Kabuto',

    141: 'Kabutops',

    142: 'Aerodactyl',

    143: 'Snorlax',

    144: 'Articuno',

    145: 'Zapdos',

    146: 'Moltres',

    147: 'Dratini',

    148: 'Dragonair',

    149: 'Dragonite',

    150: 'Mewtwo',

    151: 'Mew',
}

Number_dictionary = {
    'bulbasaur': 1,
    'ivysaur': 2,
    'venusaur': 3,
    'charmander': 4,
}