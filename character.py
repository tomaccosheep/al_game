from inventory import Inventory

class Character:
    """The Character class creates characters for our group game."""

    def __init__(self, name, description, loc, health=100):
        """
        Initiates a Character object.
        """
        self.location = loc
        self.description = description
        self.name = name
        self.inventory = Inventory(name)
        self.health = health

    def __str__(self):
        """
        Overloads print function.
        """
        return "{}".format(self.name)
        # this puts those values into a string, which you need

    def __repr__(self):
        """
        Determines what the representation will be when it's in a list.
        """
        return "{}".format(self.name)

