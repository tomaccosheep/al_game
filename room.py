class Coord():
    def __init__(self, in_coord, item=None):
        # Every set of coordinates has 3 points on the z-axis to place
        # items
        # {{
        self.coord = in_coord
        self.z0 = item
        self.z1 = None
        self.z2 = None
        self.status = None
        # }}

    def __str__(self):
        return str(self.coord)

    def fall(self):
        # Stuff falls down when there's nothing below it
        # {{
        if not (self.z0 == None and self.z1 == None and self.z2 == None):
            if self.z0 == None and self.z1 == None:
                self.z0 = self.z2
                self.z2 = None
            if self.z0 == None:
                if self.z1 != None:
                    self.z0 = self.z1
                    self.z1 = None
            if self.z1 == None:
                if self.z2 != None:
                    self.z1 = self.z1
                    self.z2 = None
        # }}

    def place(self, item_in):
        # Place something on top of the lowest level of coordinates
        # available.
        # {{
        if self.z0 != None:
            if self.z1 != None:
                if self.z2 != None:
                    print("This space is occupied")
                else:
                    self.z2 = item_in
            else:
                self.z1 = item_in
        else:
            self.z0 = item_in
        # }}

    def announce(self):
        # This will print the stack on a space. First it checks if the space is empty. If it isn't, it builds a list of objects
        # that exist on the space. It adjusts the output based on how many objects are on the space.
        # {{
        if self.z0 == None and self.z1 == None and self.z2 == None:
            return "The space is empty."
        else:
            not_empty = []
            for i in [self.z0, self.z1, self.z2]:
                if i != None:
                    not_empty.append(i)
            if len(not_empty) == 3:
                return "The {} is on the {}, which is on the {}".format(not_empty[2], not_empty[1], not_empty[0])
            elif len(not_empty) == 2:
                return "The {} is on the {}".format(not_empty[1], not_empty[0])
            else:
                return "The {} is on the ground".format(not_empty[0])
        # }}
            
    def take(self, myitem):
        # Take the item from it's z-coordinate, and 
        # let everythinge else fall one space
        # {{
        if str(z0) == myitem:
            returnie = z0
            z0 = z1
            z1 = z2
            z2 = None
            return returnie
        elif str(z1) == myitem:
            returnie = z1
            z1 = z2
            z2 = None
            return returnie
        elif str(z2) == myitem:
            returnie = z2
            z2 = None
            return returnie
        # }}


    def update():
        pass

# This creates a room with basic conditions, and it also gives the room map_coord and room_coord
# Room_coord is zoomed in relative to map_coord at a scale of 5 to 1
# {{
class Room():

    def __init__(self, characters, coordinates):
        self.characters = characters
        self.map_coord = coordinates
        self.room_coord = []

        # First this runs through all coordinates to get the
        # smallest x coordinate and the smallest y coordinate.
        # Then it creates a list of tuples that are the coordinates
        # for the room. All x and y coordinates are shifted based on the
        # smallest x and the smallest y, so that the top left corner is
        # (0,0)
        # {{
        x_smallest = self.map_coord[0][0]
        y_smallest = self.map_coord[0][1]
        for i in coordinates:
            if i[0] < x_smallest:
                x_smallest = i[0]
            if i[1] < y_smallest:
                y_smallest = i[1]
        for i in coordinates:
            x = (i[0] - x_smallest) * 5
            y = (i[1] - y_smallest) * 5
            for j in [ 0, 1, 2, 3, 4]:
                for k in [ 0, 1, 2, 3, 4]:
                    self.room_coord.append((x + j, y + k))
        # }}

        self.coord_dict = {}
        for i in self.room_coord:
            self.coord_dict[i] = Coord(i)
        

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def update_characters(self, characters):
        self.characters = list(characters)

# }}



class Door():
    def __init__(self, name, description, room1, room2, is_locked):
        self.name = name
        self.description = description
        self.front = room1
        self.back = room2
        self.is_locked = is_locked

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def look(self):
        print(self.name + '\n' + self.description)

    def unlock(self, key):
        if key.name == self.name:
            self.is_locked = False
        else:
            print('You couldn\'t unlock the door')
            
