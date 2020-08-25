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
        'strengths': [None],
        'weaknesses': ['Fighting']
    },
    'Fire': {
        'color': {
            'rgb': (240, 128, 48),
            'hex': 'f08030'
        },
        'strengths': ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy'],
        'weaknesses': ['Water', 'Ground', 'Rock']
    },
    'Fighting': {
        'color': {
            'rgb': (192, 48, 40),
            'hex': 'c03028'
        },
        'strengths': ['Bug', 'Rock', 'Dark'],
        'weaknesses': ['Flying', 'Psychic', 'Fairy']
    },
    'Water': {
        'color': {
            'rgb': (104, 144, 240),
            'hex': '6890f0'
        },
        'strengths': ['Fire', 'Water', 'Ice', 'Steel'],
        'weaknesses': ['Electric', 'Grass']
    },
    'Flying': {
        'color': {
            'rgb': (168, 144, 240),
            'hex': 'a890f0'
        },
        'strengths': ['Grass', 'Fighting', 'Bug'],
        'weaknesses': ['Electric', 'Ice', 'Rock']
    },
    'Grass': {
        'color': {
            'rgb': (120, 200, 80),
            'hex': '78c850'
        },
        'strengths': ['Water', 'Electric', 'Grass', 'Ground'],
        'weaknesses': ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']
    },
    'Poison': {
        'color': {
            'rgb': (160, 64, 160),
            'hex': 'a040a0'
        },
        'strengths': ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy'],
        'weaknesses': ['Ground', 'Psychic']
    },
    'Electric': {
        'color': {
            'rgb': (248, 208, 48),
            'hex': 'f8d030'
        },
        'strengths': ['Electric', 'Flying', 'Steel'],
        'weaknesses': ['Ground']
    },
    'Ground': {
        'color': {
            'rgb': (224, 192, 104),
            'hex': 'e0c068'
        },
        'strengths': ['Poison', 'Rock'],
        'weaknesses': ['Water', 'Grass', 'Ice']
    },
    'Psychic': {
        'color': {
            'rgb': (248, 88, 136),
            'hex': 'f85888'
        },
        'strengths': ['Fighting', 'Psychic'],
        'weaknesses': ['Bug', 'Ghost', 'Dark']
    },
    'Rock': {
        'color': {
            'rgb': (184, 160, 56),
            'hex': 'b8a038'
        },
        'strengths': ['Normal', 'Fire', 'Poison', 'Flying'],
        'weaknesses': ['Water', 'Grass', 'Fighting', 'Ground', 'Steel']
    },
    'Ice': {
        'color': {
            'rgb': (152, 216, 216),
            'hex': '98d8d8'
        },
        'strengths': ['Ice'],
        'weaknesses': ['Fire', 'Fighting', 'Rock', 'Steel']
    },
    'Bug': {
        'color': {
            'rgb': (168, 184, 32),
            'hex': 'a8b820'
        },
        'strengths': ['Grass', 'Fighting', 'Ground'],
        'weaknesses': ['Fire', 'Flying', 'Rock']
    },
    'Dragon': {
        'color': {
            'rgb': (112, 56, 248),
            'hex': '7038f8'
        },
        'strengths': ['Fire', 'Water', 'Electric', 'Grass'],
        'weaknesses': ['Ice', 'Dragon', 'Fairy']
    },
    'Ghost': {
        'color': {
            'rgb': (112, 88, 152),
            'hex': '705898'
        },
        'strengths': ['Poison', 'Bug'],
        'weaknesses': ['Ghost', 'Dark']
    },
    'Dark': {
        'color': {
            'rgb': (112, 88, 72),
            'hex': '705848'
        },
        'strengths': ['Ghost', 'Dark'],
        'weaknesses': ['Fighting', 'Bug']
    },
    'Steel': {
        'color': {
            'rgb': (184, 184, 208),
            'hex': 'b8b8d0'
        },
        'strengths': ['Normal', 'Grass', 'Ice', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy'],
        'weaknesses': ['Fire', 'Fighting', 'Ground']
    },
    'Fairy': {
        'color': {
            'rgb': (238, 153, 172),
            'hex': 'ee99ac'
        },
        'strengths': ['Fighting', 'Bug', 'Dark'],
        'weaknesses': ['Poison', 'Steel']
    },
    '???': {
        'color': {
            'rgb': (),
            'hex': ''
        },
        'strengths': [],
        'weaknesses': []
    },
    None: {'strengths': [''], 'weaknesses': ['']}
}