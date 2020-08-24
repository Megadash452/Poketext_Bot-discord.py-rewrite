type_data = {
    #get color from: https://loucyoreviews.files.wordpress.com/2013/02/wpid-screenshot_2013-02-18-00-21-57-1.png
    #can't have NoneType as a weakness/strength, so use an empty string isntead
    'PokeText': {
        'color': {
            'rgb': (255, 216, 35),
            'hex': 'ffd823'
        },
        'strengths': [None],
        'weaknesses': [None]
    },
    'Normal': {
        'color': {
            'rgb': (168, 168, 120),
            'hex': 'a8a878'
        },
        'strengths': [
            None
        ],
        'weaknesses': [
            'Fighting'
        ]
    },
    'Fire': {
        'color': {
            'rgb': (240, 128, 48),
            'hex': 'f08030'
        },
        'strengths': [
            'Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy'
        ],
        'weaknesses': [
            'Water', 'Ground', 'Rock'
        ]
    },
    'Fighting': {
        'color': {
            'rgb': (192, 48, 40),
            'hex': 'c03028'
        },
        'strengths': [
            'Bug', 'Rock', 'Dark'
        ],
        'weaknesses': [
            'Flying', 'Psychic', 'Fairy'
        ]
    },
    'Water': {
        'color': {
            'rgb': (104, 144, 240),
            'hex': '6890f0'
        },
        'strengths': [
            'Fire', 'Water', 'Ice', 'Steel'
        ],
        'weaknesses': [
            'Electric', 'Grass'
        ]
    },
    'Flying': {
        'color': {
            'rgb': (168, 144, 240),
            'hex': 'a890f0'
        },
        'strengths': [
            'Grass', 'Fighting', 'Bug'
        ],
        'weaknesses': [
            'Electric', 'Ice', 'Rock'
        ]
    },
    'Grass': {
        'color': {
            'rgb': (120, 200, 80),
            'hex': '78c850'
        },
        'strengths': [
            'Water', 'Electric', 'Grass', 'Ground'
        ],
        'weaknesses': [
            'Fire', 'Ice', 'Poison', 'Flying', 'Bug'
        ]
    },
    'Poison': {
        'color': {
            'rgb': (160, 64, 160),
            'hex': 'a040a0'
        },
        'strengths': [
            'Grass', 'Fighting', 'Poison', 'Bug', 'Fairy'
        ],
        'weaknesses': [
            'Ground', 'Psychic'
        ]
    },
    'Electric': {
        'color': {
            'rgb': (248, 208, 48),
            'hex': 'f8d030'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Ground': {
        'color': {
            'rgb': (224, 192, 104),
            'hex': 'e0c068'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Psychic': {
        'color': {
            'rgb': (248, 88, 136),
            'hex': 'f85888'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Rock': {
        'color': {
            'rgb': (184, 160, 56),
            'hex': 'b8a038'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Ice': {
        'color': {
            'rgb': (152, 216, 216),
            'hex': '98d8d8'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Bug': {
        'color': {
            'rgb': (168, 184, 32),
            'hex': 'a8b820'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Dragon': {
        'color': {
            'rgb': (112, 56, 248),
            'hex': '7038f8'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Ghost': {
        'color': {
            'rgb': (112, 88, 152),
            'hex': '705898'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Dark': {
        'color': {
            'rgb': (112, 88, 72),
            'hex': '705848'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Steel': {
        'color': {
            'rgb': (184, 184, 208),
            'hex': 'b8b8d0'
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    'Fairy': {
        'color': {
            'rgb': (238, 153, 172),
            'hex': 'ee99ac'
        },
        'strengths': [
            'Fighting', 'Bug', 'Dark'
        ],
        'weaknesses': [
            'Poison', 'Steel'
        ]
    },
    '???': {
        'color': {
            'rgb': (),
            'hex': ''
        },
        'strengths': [

        ],
        'weaknesses': [

        ]
    },
    None: {'strengths': [''], 'weaknesses': ['']}
}

#for later
"""def get_weaknesses(self):
        type_1w = type_data[self.types[0]]['weaknesses']
        type_2w = type_data[self.types[1]]['weaknesses']
        strengths = type_data[self.types[0]]['strengths'].append(type_data[self.types[1]]['strengths'])
        weaknesses_list = []

        try:
            for weakness in type_1w:
                if not weakness in type_2w:
                    if not weakness in strengths:
                        weaknesses_list.append(weakness)
        except:
            pass

        weaknesses_list.append(type_2w)

        return weaknesses_list

    def get_strengths(self):
        type_1s = type_data[self.types[0]]['strengths']
        type_2s = type_data[self.types[1]]['strengths']
        weaknesses = type_data[self.types[0]]['weaknesses'].append(type_data[self.types[1]]['weaknesses'])
        strengths_list = []

        try:
            for strength in type_1s:
                if not strength in type_2s:
                    if not strength in weaknesses:
                        strengths_list.append(strength)
        except:
            pass

        strengths_list.append(type_2s)

        return strengths_list

    def get_weaknesses_str(self):
        return_str = ''
        weaknesses_str = str(self.get_weaknesses())

        for char in weaknesses_str:
            if not char in '[]\'':
                return_str += char
            
        return return_str

    def get_strengths_str(self):
        return_str = ''
        strengths_str = str(self.get_strengths())

        for char in strengths_str:
            if not char in '[]\'':
                return_str += char
            
        return return_str

    def attack(self):
        print(self.name + ' has attacked')

    def faint(self):
        print(self.name + ' has attacked')
"""