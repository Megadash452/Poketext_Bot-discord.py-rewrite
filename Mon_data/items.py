class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Pokeball(Item):
    def __init__(self, name, type):
        super.__init__(name, type)


class Medicine(Item):
    def __init__(self, name, type):
        super.__init__(name, type)


class Berry(Item):
    def __init__(self, name, type):
        super.__init__(name, type)


class Battle_item(Item):
    def __init__(self, name, type):
        super.__init__(name, type)


class Hold_item(Item):
    def __init__(self, name, type):
        super.__init__(name, type)


class General_item(Item):
    def __init__(self, name, type):
        super.__init__(name, type)


class Machine(Item):
    def __init__(self, name, type):
        super.__init__(name, type)
