from inventory import Inventory

class Character:
    def __init__(self, name, description, loc, health=100):
        self.location = loc
        self.description = description
        self.name = name
        self.inventory = Inventory(name)
        self.health = health

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)


class Player(Character):
    def __init__(self, name, description):
        super().__init__(name, description, (0, 3), 250) 
        self.inventory = []
        
