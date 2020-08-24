from type_data import type_data

class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Mon:
    total_num_of_pokemon = 0

    def __init__(self, number, name, poke_specie, desc, types, abilities, clategory, stats):
        self.number = number
        self.name = name
        self.poke_specie = poke_specie + ' Pokémon'
        self.desc = desc
        
        self.types = types
        self.weaknesses = type_data[self.types[1]]['weaknesses'] + type_data[self.types[2]]['weaknesses']
        self.strengths = type_data[self.types[1]]['strengths'] + type_data[self.types[2]]['strengths']

        self.abilities = abilities
        self.stats = stats

        if not self.number == 0:
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
            self.sprite = {'big':{'url': 'https://raw.githubusercontent.com/Megadash452/Poketext_Bot-discord.py-rewrite/master/pokemon-sprites/gen1pokemon_sprites(colored).png'},
                            'small':{'url': 'https://raw.githubusercontent.com/Megadash452/Poketext_Bot-discord.py-rewrite/master/pokemon-sprites/Transparent.png'}
            }

        if self.name == 'Mr. Mime':
            self.sprite['small']['url'] = 'https://raw.githubusercontent.com/Megadash452/Poketext_Bot-discord.py-rewrite/master/pokemon-sprites/gen1-small/Mr.%20Mime-small.png'
            self.sprite['big']['url'] = 'https://raw.githubusercontent.com/Megadash452/Poketext_Bot-discord.py-rewrite/master/pokemon-sprites/gen1-big/Mr.%20Mime-big.png'

        Mon.total_num_of_pokemon += 1


    def attack(self):
        print(self.name + ' has attacked')

    def faint(self):
        print(self.name + ' has attacked')


# ------ Dictionary ------ ------ ------ ------ ------ ------ ------ ------ ------

Pokemon_dictionary = {
    0: Mon(0, 'Generation 1', 'All',
                'Description',
                ('PokeText', None),# 'Fighting', 'Water', 'Flying', 'Grass', 'Poison', 'Electric', 'Ground', 'Psychic', 'Rock', 'Ice', 'Bug', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy'),
                'All Abilities', '', stats=None
            ),

    1: Mon(1, 'Bulbasaur', 'Seed',
               'There is a plant seed on its back right from the day this is born. The seed slowly grows larger.',
               ('Grass', 'Poison'), ('Overgrow', None), '',
               
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    2: Mon(2, 'Ivysaur', 'Seed',
               'When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.',
               ('Grass', 'Poison'), ('Overgrow', None), '',

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    3: Mon(3, 'Venusaur', 'Seed',
               'Its plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.',
               ('Grass', 'Poison'), ('Overgrow', None), '',

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    4: Mon(4, 'Charmander', 'Lizard',
               'It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.',
               ('Fire', None), ('Blaze', None), '',

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    5: Mon(5, 'Charmeleon', 'Flame',
                'It has a barbaric nature. In battle, it whips its fiery tail around and slashes away with sharp claws.',
                ('Fire', None), ('Blaze', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    6: Mon(6, 'Charizard', 'Flame',
                'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.',
                ('Fire', 'Flying'), ('Blaze', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    7: Mon(7, 'Squirtle', 'Tiny turtle',
               'When it retracts its long neck into its shell, it squirts out water with vigorous force.',
               ('Water', None), ('Torrent', None), '',

                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    8: Mon(8, 'Wartortle', 'Turtle',
                'It is recognized as a symbol of longevity. If its shell has algae on it, that Wartortle is very old.',
                ('Water', None), ('Torrent', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    9: Mon(9, 'Blastoise', 'Shellfish',
                'It crushes its foe under its heavy body to cause fainting. In a pinch, it will withdraw inside its shell.', 
                ('Water', None), ('Torrent', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    10: Mon(10, 'Caterpie', 'Worm',
                'For protection, it releases a horrible stench from the antenna on its head to drive away enemies.',
                ('Bug', None), ('Shield Dust', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    11: Mon(11, 'Metapod', 'Cocoon',
                'It is waiting for the moment to evolve. At this stage, it can only harden, so it remains motionless to avoid attack.',
                ('Bug', None), ('Shed Skin', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    12: Mon(12, 'Butterfree', 'Butterfly',
                'In battle, it flaps its wings at great speed to release highly toxic dust into the air.',
                ('Bug', 'Flying'), ('Compound Eyes', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    13: Mon(13, 'Weedle', 'Hairy bug',
                'Beware of the sharp stinger on its head. It hides in grass and bushes where it eats leaves.',
                ('Bug', 'Poison'), ('Shield Dust', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    14: Mon(14, 'Kakuna', 'Cocoon',
                'Able to move only slightly. When endangered, it may stick out its stinger and poison its enemy.',
                ('Bug', 'Poison'), ('Shed Skin', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    15: Mon(15, 'Beedrill', 'Poison bee',
                'It has three poisonous stingers on its forelegs and its tail. They are used to jab its enemy repeatedly.',
                ('Bug', 'Poison'), ('Swarm', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    16: Mon(16, 'Pidgey', 'Tiny bird',
                'Very docile. If attacked, it will often kick up sand to protect itself rather than fight back.',
                ('Normal', 'Flying'), ('Keen Eye', 'Tangled Feet'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    17: Mon(17, 'Pidgeotto', 'Bird',
                'This Pokémon is full of vitality. It constantly flies around its large territory in search of prey.',
                ('Normal', 'Flying'), ('Keen Eye', 'Tangled Feet'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    18: Mon(18, 'Pidgeot', 'Bird',
                'This Pokémon flies at Mach 2 speed, seeking prey. Its large talons are feared as wicked weapons.',
                ('Normal', 'Flying'), ('Keen Eye', 'Tangled Feet'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    19: Mon(19, 'Rattata', 'Mouse',
                'Will chew on anything with its fangs. If you see one, you can be certain that 40 more live in the area.',
                ('Normal', None), ('Run Away', 'Guts'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    20: Mon(20, 'Raticate', 'Mouse',
                'Its hind feet are webbed. They act as flippers, so it can swim in rivers and hunt for prey.',
                ('Normal', None), ('Run Away', 'Guts'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    21: Mon(21, 'Spearow', 'Tiny bird',
                'Inept at flying high. However, it can fly around very fast to protect its territory.',
                ('Normal', 'Flying'), ('Keen Eye', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    22: Mon(22, 'Fearow', 'Beak',
                'A Pokémon that dates back many years. If it senses danger, it flies high and away, instantly.',
                ('Normal', 'Flying'), ('Keen Eye', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    23: Mon(23, 'Ekans', 'Snake',
                'The older it gets, the longer it grows. At night, it wraps its long body around tree branches to rest.',
                ('Poison', None), ('Shed Skin', 'Intimidate'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    24: Mon(24, 'Arbok', 'Cobra',
                'The frightening patterns on its belly have been studied. Six variations have been confirmed.',
                ('Poison', None), ('Shed Skin', 'Intimidate'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    25: Mon(25, 'Pikachu', 'Mouse',
                'Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy.',
                ('Electric', None), ('Static', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    26: Mon(26, 'Raichu', 'Mouse',
                'Its long tail serves as a ground to protect itself from its own high-voltage power.',
                ('Electric', None), ('Static', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    27: Mon(27, 'Sandshrew', 'Mouse',
                'It loves to bathe in the grit of dry, sandy areas. By sand bathing, the Pokémon rids itself of dirt and moisture clinging to its body.',
                ('Ground', None), ('Sand Veil', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    28: Mon(28, 'Sandslash', 'Mouse',
                'The drier the area Sandslash lives in, the harder and smoother the Pokémon’s spikes will feel when touched.',
                ('Ground', None), ('Sand Veil', None),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    29: Mon(29, 'Nidoran♀', 'Poison pin',
                'A mild-mannered Pokémon that does not like to fight. Beware—its small horn secretes venom.',
                ('Poison', None), ('Poison Point', 'Rivalry'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    30: Mon(30, 'Nidorina', 'Poison pin',
                'When resting deep in its burrow, its barbs always retract. This is proof that it is relaxed.',
                ('Poison', None), ('Poison Point', 'Rivalry'), '',
    
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    31: Mon(31, 'Nidoqueen', 'Drill',
                'Tough scales cover the sturdy body of this Pokémon. It appears that the scales grow in cycles.',
                ('Poison', 'Ground'), ('Poison Point', 'Rivalry'), '',
            
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    32: Mon(32, 'Nidoran♂', 'Poison pin',
                'Its large ears are always kept upright. If it senses danger, it will attack with a poisonous sting.',
                ('Poison', None), ('Poison Point', 'Rivalry'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    33: Mon(33, 'Nidorino', 'Poison pin',
                'Its horn contains venom. If it stabs an enemy with the horn, the impact makes the poison leak out.',
                ('Poison', None), ('Poison Point', 'Rivalry'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    34: Mon(34, 'Nidoking', 'Drill',
                'Its steel-like hide adds to its powerful tackle. Its horns are so hard, they can pierce a diamond.',
                ('Poison', 'Ground'), ('Poison Point', 'Rivalry'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    35: Mon(35, 'Clefairy', 'Fairy',
                'It is said that happiness will come to those who see a gathering of Clefairy dancing under a full moon.',
                ('Fairy', None), ('Cute Charm', 'Magic Guard'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    36: Mon(36, 'Clefable', 'Fairy',
                'A timid fairy Pokémon that is rarely seen, it will run and hide the moment it senses people.',
                ('Fairy', None), ('Cute Charm', 'Magic Guard'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    37: Mon(37, 'Vulpix', 'Fox',
                'While young, it has six gorgeous tails. When it grows, several new tails are sprouted.',
                ('Fire', None), ('Flash Fire', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    38: Mon(38, 'Ninteales', 'Fox',
                'It is said to live 1,000 years, and each of its tails is loaded with supernatural powers.',
                ('Fire', None), ('Flash Fire', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    39: Mon(39, 'Jigglypuff', 'Balloon',
                'Jigglypuff has top-notch lung capacity, even by comparison to other Pokémon. It won\'t stop singing its lullabies until its foes fall asleep.',
                ('Normal', 'Fairy'), ('Cute Charm', 'Competitive'),  '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    40: Mon(40, 'Wigglytuff', 'Balloon',
                'The more air it takes in, the more it inflates. If opponents catch it in a bad mood, it will inflate itself to an enormous size to intimidate them.',
                ('Normal', 'Fairy'), ('Cute Charm', 'Competitive'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    41: Mon(41, 'Zubat', 'Bat',
                'Emits ultrasonic cries while it flies. They act as a sonar used to check for objects in its way.',
                ('Poison', 'Flying'), ('Inner Focus', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    42: Mon(42, 'Golbat', 'Bat',
                'It attacks in a stealthy manner, without warning. Its sharp fangs are used to bite and to suck blood.',
                ('Poison', 'Flying'), ('Inner Focus', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    43: Mon(43, 'Oddish', 'Weed',
                'If exposed to moonlight, it starts to move. It roams far and wide at night to scatter its seeds.',
                ('Grass', 'Poison'), ('Chlorophyl', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    44: Mon(44, 'Gloom', 'Weed',
                'Its pistils exude an incredibly foul odor. The horrid stench can cause fainting at a distance of 1.25',
                ('Grass', 'Poison'), ('Chlorophyl', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    45: Mon(45, 'Vileplume', 'Flower',
                'It has the world\'s largest petals. With every step, the petals shake out heavy clouds of toxic pollen.',
                ('Grass', 'Poison'), ('Chlorophyl', None), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    46: Mon(46, 'Paras', 'Mushroom',
                'Burrows under the ground to gnaw on tree roots. The mushrooms on its back absorb most of the nutrition.',
                ('Bug', 'Grass'), ('Effect Spore', 'Dry Skin'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    47: Mon(47, 'Parasect', 'Mushroom',
                'The bug host is drained of energy by the mushroom on its back. The mushroom appears to do all the thinking.',
                ('Bug', 'Grass'), ('Effect Spore', 'Dry Skin'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    48: Mon(48, 'Venonat', 'Insect',
                'Its large eyes act as radar. In a bright place, you can see that they are clusters of many tiny eyes.',
                ('Bug', 'Poison'), ('Compound Eyes', 'Tinted Lens'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    49: Mon(49, 'Venomoth', 'Poison Moth',
                'The powdery scales on its wings are hard to remove from skin. They also contain poison that leaks out on contact.',
                ('Bug', 'Poison'), ('Shield Dust', 'Tinted Lens'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    50: Mon(50, 'Diglett', 'Mole',
                'If a Diglett digs through a field, it leaves the soil perfectly tilled and ideal for planting crops.',
                ('Ground', None), ('Sand Veil', 'Arena Trap'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    51: Mon(51, 'Dugtrio', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    52: Mon(52, 'Meowth', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    53: Mon(53, 'Persian', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    54: Mon(54, 'Psyduck', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    55: Mon(55, 'Golduck', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    56: Mon(56, 'Mankey', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    57: Mon(57, 'Primeape', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    58: Mon(58, 'Growlithe', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    59: Mon(59, 'Arcanine', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    60: Mon(60, 'Poliwag', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    61: Mon(61, 'Poliwhirl', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    62: Mon(62, 'Poliwrath', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    63: Mon(63, 'Abra', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    64: Mon(64, 'Kadabra', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    65: Mon(65, 'Alakazam', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    66: Mon(66, 'Machop', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    67: Mon(67, 'Machoke', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    68: Mon(68, 'Machamp', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    69: Mon(69, 'Bellsprout', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    70: Mon(70, 'Weepinbell', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    71: Mon(71, 'Victreebel', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    72: Mon(72, 'Tentacool', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    73: Mon(73, 'Tentacruel', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    74: Mon(74, 'Geodude', 'Rock',
                'Commonly found near mountain trails and the like. If you step on one by accident, it gets angry.',
                ('Rock', 'Ground'), ('Rock Head', 'Sturdy'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),
                
    75: Mon(75, 'Graveler', 'Rock',
                'Often seen rolling down mountain trails. Obstacles are just things to roll straight over, not avoid.',
                ('Rock', 'Ground'), ('Rock Head', 'Sturdy'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    76: Mon(76, 'Golem', 'Megaton',
                'Once it sheds its skin, its body turns tender and whitish. Its hide hardens when it\'s exposed to air.',
                ('Rock', 'Ground'), ('Rock Head', 'Sturdy'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    77: Mon(77, 'Ponyta', 'Fire Horse',
                'It can\'t run properly when it’s newly born. As it races around with others of its kind, its legs grow stronger.',
                ('Fire', None), ('Run Away', 'Flash Fire'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    78: Mon(78, 'Rapidash', 'Fire Horse',
                'This Pokémon can be seen galloping through fields at speeds of up to 150 mph, its fiery mane fluttering in the wind.',
                ('Fire', None), ('Run Away', 'Flash Fire'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    79: Mon(79, 'Slowpoke', 'Dopey',
                'Slow-witted and oblivious, this Pokémon won\'t feel any pain if its tail gets eaten. It won\'t notice when its tail grows back, either.',
                ('Water', 'Psychic'), ('Oblivious', 'Own Tempo'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    80: Mon(80, 'Slowbro', 'Hermit Crab',
                'Slowpoke became Slowbro when a Shellder bit on to its tail. Sweet flavors seeping from the tail make the Shellder feel as if its life is a dream.',
                ('Water', 'Psychic'), ('Oblivious', 'Own Tempo'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    81: Mon(81, 'Magnemite', 'Magnet',
                'At times, Magnemite runs out of electricity and ends up on the ground. If you give batteries to a grounded Magnemite, it\'ll start moving again.',
                ('Electric', 'Steel'), ('Sturdy', 'Magnet Pull'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    82: Mon(82, 'Magneton', 'Magnet',
                'This Pokémon is three Magnemite that have linked together. Magneton sends out powerful radio waves to study its surroundings.',
                ('Electric', 'Steel'), ('Sturdy', 'Magnet Pull'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    83: Mon(83, 'Farfetch\'d', 'Wild Duck',
                'The stalk this Pokémon carries in its wings serves as a sword to cut down opponents. In a dire situation, the stalk can also serve as food.',
                ('Normal', 'Flying'), ('Keen Eye', 'Inner Focus'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    84: Mon(84, 'Doduo', 'Twin Bird',
                'Its short wings make flying difficult. Instead, this Pokémon runs at high speed on developed legs.',
                ('Normal', 'Flying'), ('Run Away', 'Early Bird'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    85: Mon(85, 'Dodrio', 'Triple Bird',
                'One of Doduo\'s two heads splits to form a unique species. It runs close to 40 mph in prairies.',
                ('Normal', 'Flying'), ('Run Away', 'Early Bird'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    86: Mon(86, 'Seel', 'Sea Lion',
                'Loves freezing-cold conditions. Relishes swimming in a frigid climate of around 14 degrees Fahrenheit.',
                ('Water', None), ('Thick Fat', 'Hydration'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    87: Mon(87, 'Dewgong', 'Sea Lion',
                'Its entire body is a snowy white. Unharmed by even intense cold, it swims powerfully in icy waters.',
                ('Water', 'Ice'), ('Thick Fat', 'Hydration'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    88: Mon(88, 'Grimer', 'Sludge',
                'Made of congealed sludge. It smells too putrid to touch. Even weeds won\'t grow in its path.',
                ('Poison', None), ('Stench', 'Sticky Hold'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    89: Mon(89, 'Muk', 'Sludge',
                'Smells so awful, it can cause fainting. Through degeneration of its nose, it lost its sense of smell.',
                ('Poison', None), ('Stench', 'Sticky Hold'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    90: Mon(90, 'Shellder', 'Bivalve',
                'It swims facing backward by opening and closing its two-piece shell. It is surprisingly fast.',
                ('Water', None), ('Shell Armor', 'Skill Link'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    91: Mon(91, 'Cloyster', 'Bivalve',
                'Its shell is extremely hard. It cannot be shattered, even with a bomb. The shell opens only when it is attacking.',
                ('Water', 'Ice'), ('Shell Armor', 'Skill Link'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    92: Mon(92, 'Gastly', 'Gas',
                'Born from gases, anyone would faint if engulfed by its gaseous body, which contains poison.',
                ('Ghost', 'Poison'), ('Gen 3-5: Levitate', 'Gen 6+: Cursed Body'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    93: Mon(93, 'Haunter', 'Gas',
                'Its tongue is made of gas. If licked, its victim starts shaking constantly until death eventually comes.',
                ('Ghost', 'Poison'), ('Gen 3-5: Levitate', 'Gen 6+: Cursed Body'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    94: Mon(94, 'Gengar', 'Shadow',
                'On the night of a full moon, if shadows move on their own and laugh, it must be Gengar\'s doing.',
                ('Ghost', 'Poison'), ('Gen 3-5: Levitate', 'Gen 6+: Cursed Body'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    95: Mon(95, 'Onix', 'Rock Snake',
                'As it digs through the ground, it absorbs many hard objects. This is what makes its body so solid.',
                ('Rock', 'Ground'), ('Rock Head', 'Sturdy'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    96: Mon(96, 'Drowzee', 'Hypnosis',
                'If you sleep by it all the time, it will sometimes show you dreams it had eaten in the past.',
                ('Psychic', None), ('Insomnia', 'Forewarn'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    97: Mon(97, 'Hypno', 'Hypnosis',
                'Avoid eye contact if you come across one. It will try to put you to sleep by using its pendulum.',
                ('Psychic', None), ('Insomnia', 'Forewarn'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    98: Mon(98, 'Krabby', 'River Crab',
                'It can be found near the sea. The large pincers grow back if they are torn out of their sockets.',
                ('Water', None), ('Shell Armor', 'Hyper Cutter'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    99: Mon(99, 'Kingler', 'Pincer',
                'Its large and hard pincer has 10,000-horsepower strength. However, being so big, it is unwieldy to move.',
                ('Water', None), ('Shell Armor', 'Hyper Cutter'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    100: Mon(100, 'Voltorb', 'Ball',
                 'It is said to camouflage itself as a Poké Ball. It will self-destruct with very little stimulus.',
                 ('Electric', None), ('Static', 'Soundproof'), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    101: Mon(101, 'Electrode', 'Ball',
                 'Stores electrical energy inside its body. Even the slightest shock could trigger a huge explosion.',
                 ('Electric', None), ('Static', 'Soundproof'), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    102: Mon(102, 'Exeggcute', 'Egg',
                 'Though it may look like it\'s just a bunch of eggs, it’s a proper Pokémon. Exeggcute communicates with others of its kind via telepathy, apparently.',
                 ('Grass', 'Psychic'), ('Chlorophyll', None), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    103: Mon(103, 'Exeggutor', 'Coconut',
                 'Each of Exeggutor\'s three heads is thinking different thoughts. The three don\'t seem to be very interested in one another.',
                 ('Grass', 'Psychic'), ('Chlorophyll', None), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    104: Mon(104, 'Cubone', 'Lonely',
                 'When the memory of its departed mother brings it to tears, its cries echo mournfully within the skull it wears on its head.',
                 ('Ground', None), ('Rock Head', 'Lightning Rod'), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    105: Mon(105, 'Marowak', 'Bone Keeper',
                 'This Pokémon overcame its sorrow to evolve a sturdy new body. Marowak faces its opponents bravely, using a bone as a weapon.',
                 ('Ground', None), ('Rock Head', 'Lightning Rod'), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    106: Mon(106, 'Hitmonlee', 'Kicking',
                 'This amazing Pokémon has an awesome sense of balance. It can kick in succession from any position.',
                 ('Fighting', None), ('Limber', 'Reckless'), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    107: Mon(107, 'Hitmonchan', 'Punching',
                 'Its punches slice the air. They are launched at such high speed, even a slight graze could cause a burn.',
                 ('Fighting', None), ('Keen Eye', 'Iron Fist'), '',                 
                 stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    108: Mon(108, 'Lickitung', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    109: Mon(109, 'Koffing', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    110: Mon(110, 'Weezing', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    111: Mon(111, 'Rhyhorn', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    112: Mon(112, 'Rhydon', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    113: Mon(113, 'Chansey', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    114: Mon(114, 'Tangela', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    115: Mon(115, 'Kangaskhan', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    116: Mon(116, 'Horsea', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    117: Mon(117, 'Seadra', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    118: Mon(118, 'Goldeen', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    119: Mon(119, 'Seaking', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    120: Mon(120, 'Staryu', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    121: Mon(121, 'Starmie', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    122: Mon(122, 'Mr. Mime', 'Barrier',
                'The broadness of its hands may be no coincidence—many scientists believe its palms became enlarged specifically for pantomiming.',
                ('Psychic', 'Fairy'), ('Soundproof', 'Filter'), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': '' 
                }),

    123: Mon(123, 'Scyther', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    124: Mon(124, 'Jynx', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    125: Mon(125, 'Electabuzz', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    126: Mon(126, 'Magmar', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    127: Mon(127, 'Pinsir', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    128: Mon(128, 'Tauros', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    129: Mon(129, 'Magikarp', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    130: Mon(130, 'Gyarados', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    131: Mon(131, 'Lapras', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    132: Mon(132, 'Ditto', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    133: Mon(133, 'Eevee', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    134: Mon(134, 'Vaporeon', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    135: Mon(135, 'Jolteon', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    136: Mon(136, 'Flareon', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    137: Mon(137, 'Porygon', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    138: Mon(138, 'Omanyte', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    139: Mon(139, 'Omastar', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    140: Mon(140, 'Kabuto', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    141: Mon(141, 'Kabutops', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    142: Mon(142, 'Aerodactyl', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    143: Mon(143, 'Snorlax', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    144: Mon(144, 'Articuno', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    145: Mon(145, 'Zapdos', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    146: Mon(146, 'Moltres', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    147: Mon(147, 'Dratini', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    148: Mon(148, 'Dragonair', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    149: Mon(149, 'Dragonite', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    150: Mon(150, 'Mewtwo', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),

    151: Mon(151, 'Mew', '',
                '',
                ('', None), ('', ''), '',
                
                stats = {
                    'hp': '',
                    'attack': '',
                    'defense': '',
                    'special attack': '',
                    'special defense': '',
                    'speed': ''
               }),
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
    'nidoran♀': 29, 'nidorina': 30, 'nidoqueen': 31,
    'nidoran♂': 32, 'nidorino': 33, 'nidoking': 34,
    'clefairy': 35, 'clefable': 36,
    'vulpix': 37, 'ninetales': 38,
    'jigglypuff': 39, 'wigglytuff': 40,
    'zubat': 41, 'golbat': 42,
    'oddish': 43, 'gloom': 44, 'vileplume': 45,
    'paras': 46, 'parasect': 47,
    'venonat': 48, 'venomoth': 49,
    'diglett': 50, 'dugtrio': 51,
    'meowth': 52, 'persian': 53,
    'psyduck': 54, 'golduck': 55,
    'mankey': 56, 'primeape': 57,
    'growlithe': 58, 'arcanine': 59,
    'poliwag': 60, 'poliwhirl': 61, 'poliwrath': 62,
    'abra': 63, 'kadabra': 64, 'alakazam': 65,
    'machop': 66, 'machoke': 67, 'machamp': 68,
    'bellsprout': 69, 'weepinbell': 70, 'victreebel': 71,
    'tentacool': 72, 'tentacruel': 73,
    'geodude': 74, 'graveler': 75, 'golem': 76,
    'ponyta': 77, 'rapidash': 78,
    'slowpoke': 79, 'slowbro': 80,
    'magnemite': 81, 'magneton': 82,
    'farfetch\'d': 83,
    'doduo': 84, 'dodrio': 85,
    'seel': 86, 'dewdong': 87,
    'grimer': 88, 'muk': 89,
    'shellder': 90, 'cloyster': 91,
    'gastly': 92, 'haunter': 93, 'gengar': 94,
    'onix': 95,
    'drowzee': 96, 'hypno': 97,
    'krabby': 98, 'kingler': 99,
    'voltorb': 100, 'electrode': 101,
    'exeggcute': 102, 'exeggutor': 103,
    'cubone': 104, 'marowak': 105,
    'hitmonlee': 106, 'hitmonchan': 107,
    'lickitung': 108,
    'koffing': 109, 'weezing': 110,
    'rhyhorn': 111, 'rhydon': 112,
    'chansey': 113,
    'tangela': 114,
    'kangaskhan': 115,
    'horsea': 116, 'seadra': 117,
    'goldeen': 118, 'seaking': 119,
    'staryu': 120, 'starmie': 121,
    'mr. mime': 122,
    'scyther': 123,
    'jynx': 124,
    'electabuzz': 125,
    'magmar': 126,
    'pinsir': 127,
    'tauros': 128,
    'magikarp': 129, 'gyarados': 130,
    'lapras': 131,
    'ditto': 132,
    'eevee': 133, 'vaporeon': 134, 'jolteon': 135, 'flareon': 136,
    'porygon': 137,
    'omanyte': 138, 'omastar': 139,
    'kabuto': 140, 'kabutops': 141,
    'aerodactyl': 142,
    'snorlax': 143,
    'articuno': 144, 'zapdos': 145, 'moltres': 146,
    'dratini': 147, 'dragonair': 148, 'dragonite': 149,
    'mewtwo': 150, 'mew': 151
}
