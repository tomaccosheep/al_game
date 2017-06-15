
class Item:
    def __init__(self, name, description, mytype, attack=2, attacktype='throw'):
        """
        Instantiates new Item.
        """
        self.name = name
        self.description = description
        self.type = mytype

    def __str__(self):
        """
        Overloads print function.
        """
        return self.name

    def __repr__(self):
        """
        Determines what the representation will be when it's in a list.
        """
        return self.__str__()


# This creates a spell. The name produces a list of three elements, [description, damage, and status effect].
# {{
class Spell:
    def __init__(self, name):
        self.param = {"fire": ["Flames shoot from your fingertips", 15, 'onfire'], "love": ["As you look at the spell, you feel an overwhelming sense that people are good at heart", -1000, 'loved'], "magic missile":["You are able to shoot magic missiles at an enemy", 25, 'stunned'], 'healing water': ['This water feels warm, and you can feel life coursing through it', -20, 'wet'], 'electriticy': ['This spell shoots out an unpredictable bolt of electricity', 40, 'shocked']}
        self.status_change = self.param[name][2]
        super().__init__(name, self.param[name][0], 'spell', self.param[name][1], 'cast')
# }}


class Weapon:
    def __init__(self):
        self.param = {'dagger': ['A small dagger', 10, 'slash'], 'large sword': ['A large sword', 50, 'slash'], 'machine gun': ['This looks like some type of weapon from the future', 1000, 'shoot']}
        super().__init__(name, self.param[name][0], 'weapon', self.param[name][1], self.param[name][2])


# This creates a piece of furniture. Furniture can hold one item. Barrels start with gunpowder
# {{
class Furniture:
    def __init__(self, name):
        if name == 'barrel':
            gunpowder = Item('gunpowder', 'It looks explosive', 'barrel')
        self.param = {'drawer': [10, None], 'barrel': [10, gunpowder]}
        self.has = self.param[name][1]
# }}     
