class item:
    def __init__(self, name, type):
        self.name = name
        self.type = type


def get_type_color(Type, index=-1):
    type_colors = {
        'PokeText': (255, 216, 35),
        #color format: RGB
        #get color from: https://loucyoreviews.files.wordpress.com/2013/02/wpid-screenshot_2013-02-18-00-21-57-1.png
        'Normal': (168, 168, 120),
        'Fire': (240, 128, 48),
        'Fighting': (192, 48, 40),
        'Water': (104, 144, 240),
        'Flying': (168, 144, 240),
        'Grass': (120, 200, 80),
        'Poison': (160, 64, 160),
        'Electric': (248, 208, 48),
        'Ground': (224, 192, 104),
        'Psychic': (248, 88, 136),
        'Rock': (184, 160, 56),
        'Ice': (152, 216, 216),
        'Bug': (168, 184, 32),
        'Dragon': (112, 56, 248),
        'Ghost': (112, 88, 152),
        'Dark': (112, 88, 72),
        'Steel': (184, 184, 208),
        'Fairy': (238, 153, 172),
        '???': (),
    }

    if index == -1:
        return type_colors[Type]
    else:
        return type_colors[Type][index]


class pokemon:
    total_num_of_pokemon = 0

    def __init__(self, num, name, poke_specie, desc, types, abilities, stats):
        self.num = num
        self.name = name
        self.poke_specie = poke_specie + ' Pokémon'
        self.desc = desc
        self.types = types
        self.abilities = abilities
        self.stats = stats

        if not self.num == 0:
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
        else:
            self.sprite = {'big':{'url': 'https://raw.githubusercontent.com/Megadash452/Poketext_Bot-discord.py-rewrite/master/gen1pokemon_sprites.png'}}

        pokemon.total_num_of_pokemon += 1


    def attack(self):
        print(self.name + ' has attacked')

    def faint(self):
        print(self.name + ' has attacked')


# ------ Dictionary ------ ------ ------ ------ ------ ------ ------ ------ ------

Pokemon_dictionary = {
    0: pokemon(0, 'Generation 1', 'All',
                'Description',
                ('PokeText', None),# 'Fighting', 'Water', 'Flying', 'Grass', 'Poison', 'Electric', 'Ground', 'Psychic', 'Rock', 'Ice', 'Bug', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy'),
                'All Abilities', stats=None
            ),

    1: pokemon(1, 'Bulbasaur', 'Seed',
               'There is a plant seed on its back right from the day this is born. The seed slowly grows larger.',
               ('Grass', 'Poison'), ('Overgrow', None),
               
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    2: pokemon(2, 'Ivysaur', 'Seed',
               'When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.',
               ('Grass', 'Poison'), ('Overgrow', None),

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    3: pokemon(3, 'Venusaur', 'Seed',
               'Its plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.',
               ('Grass', 'Poison'), ('Overgrow', None),

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    4: pokemon(4, 'Charmander', 'Lizard',
               'It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.',
               ('Fire', None), ('Blaze', None),

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    5: pokemon(5, 'Charmeleon', 'Flame',
                'It has a barbaric nature. In battle, it whips its fiery tail around and slashes away with sharp claws.',
                ('Fire', None), ('Blaze', None),
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    6: pokemon(6, 'Charizard', 'Flame',
                'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.',
                ('Fire', 'Flying'), ('Blaze', None),
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    7: pokemon(7, 'Squirtle', 'Tiny turtle',
               'When it retracts its long neck into its shell, it squirts out water with vigorous force.',
               ('Water', None), ('Torrent', None),

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    8: pokemon(8, 'Wartortle', 'Turtle',
                'It is recognized as a symbol of longevity. If its shell has algae on it, that Wartortle is very old.',
                ('Water', None), ('Torrent', None),
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    9: pokemon(9, 'Blastoise', 'Shellfish',
                'It crushes its foe under its heavy body to cause fainting. In a pinch, it will withdraw inside its shell.', 
                ('Water', None), ('Torrent', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    10: pokemon(10, 'Caterpie', 'Worm',
                'For protection, it releases a horrible stench from the antenna on its head to drive away enemies.',
                ('Bug', None), ('Shield Dust', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    11: pokemon(11, 'Metapod', 'Cocoon',
                'It is waiting for the moment to evolve. At this stage, it can only harden, so it remains motionless to avoid attack.',
                ('Bug', None), ('Shed Skin', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    12: pokemon(12, 'Butterfree', 'Butterfly',
                'In battle, it flaps its wings at great speed to release highly toxic dust into the air.',
                ('Bug', 'Flying'), ('Compound Eyes', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    13: pokemon(13, 'Weedle', 'Hairy bug',
                'Beware of the sharp stinger on its head. It hides in grass and bushes where it eats leaves.',
                ('Bug', 'Poison'), ('Shield Dust', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    14: pokemon(14, 'Kakuna', 'Cocoon',
                'Able to move only slightly. When endangered, it may stick out its stinger and poison its enemy.',
                ('Bug', 'Poison'), ('Shed Skin', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    15: pokemon(15, 'Beedrill', 'Poison bee',
                'It has three poisonous stingers on its forelegs and its tail. They are used to jab its enemy repeatedly.',
                ('Bug', 'Poison'), ('Swarm', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    16: pokemon(16, 'Pidgey', 'Tiny bird',
                'Very docile. If attacked, it will often kick up sand to protect itself rather than fight back.',
                ('Normal', 'Flying'), ('Keen Eye', 'Tangled Feet'), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    17: pokemon(17, 'Pidgeotto', 'Bird',
                'This Pokémon is full of vitality. It constantly flies around its large territory in search of prey.',
                ('Normal', 'Flying'), ('Keen Eye', 'Tangled Feet'), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    18: pokemon(18, 'Pidgeot', 'Bird',
                'This Pokémon flies at Mach 2 speed, seeking prey. Its large talons are feared as wicked weapons.',
                ('Normal', 'Flying'), ('Keen Eye', 'Tangled Feet'), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    19: pokemon(19, 'Rattata', 'Mouse',
                'Will chew on anything with its fangs. If you see one, you can be certain that 40 more live in the area.',
                ('Normal', None), ('Run Away', 'Guts'), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    20: pokemon(20, 'Raticate', 'Mouse',
                'Its hind feet are webbed. They act as flippers, so it can swim in rivers and hunt for prey.',
                ('Normal', None), ('Run Away', 'Guts'), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    21: pokemon(21, 'Spearow', 'Tiny bird',
                'Inept at flying high. However, it can fly around very fast to protect its territory.',
                ('Normal', 'Flying'), ('Keen Eye', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    22: pokemon(22, 'Fearow', 'Beak',
                'A Pokémon that dates back many years. If it senses danger, it flies high and away, instantly.',
                ('Normal', 'Flying'), ('Keen Eye', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    23: pokemon(23, 'Ekans', 'Snake',
                'The older it gets, the longer it grows. At night, it wraps its long body around tree branches to rest.',
                ('Poison', None), ('Shed Skin', 'Intimidate'), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    24: pokemon(24, 'Arbok', 'Cobra',
                'The frightening patterns on its belly have been studied. Six variations have been confirmed.',
                ('Poison', None), ('Shed Skin', 'Intimidate'), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    25: pokemon(25, 'Pikachu', 'Mouse',
                'Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy.',
                ('Electric', None), ('Static', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    26: pokemon(26, 'Raichu', 'Mouse',
                'Its long tail serves as a ground to protect itself from its own high-voltage power.',
                ('Electric', None), ('Static', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    27: pokemon(27, 'Sandshrew', 'Mouse',
                'It loves to bathe in the grit of dry, sandy areas. By sand bathing, the Pokémon rids itself of dirt and moisture clinging to its body.',
                ('Ground', None), ('Sand Veil', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    28: pokemon(28, 'Sandslash', 'Mouse',
                'The drier the area Sandslash lives in, the harder and smoother the Pokémon’s spikes will feel when touched.',
                ('Ground', None), ('Sand Veil', None), 
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

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
    'all': 0,
    'bulbasaur': 1, 'ivysaur': 2, 'venusaur': 3,
    'charmander': 4, 'charmeleon': 5, 'charizard': 6,
    'squirtle': 7, 'wartortle': 8, 'blastoise': 9,
    'caterpie': 10, 'metapod': 11, 'butterfree': 12,
    'weedle': 13, 'kakuna': 14, 'beedrill': 15,
    'pidgey': 16, 'pidgeotto': 17, 'pidgeot': 18,
    'rattata': 19, 'raticate': 20,
    'spearow': 21, 'fearow':22,
    'ekans': 23, 'arbok': 24,
    'pikachu': 25, 'raichu': 26,
    'sandshrew': 27, 'sandslash': 28,
}