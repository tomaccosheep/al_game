import room, item, curses
from time import sleep
from random import randint



# This will look up the visual character representation based on the
# inputed item's name
# {{
def get_visual_character(item):
    visual_char_dict = {'barrel': '🛢', 'desk': '🛋'}
    return visual_char_dict[item.name]
# }}


# This function prints the room to the screen. It checks the z0 value
# of every room coordinate (which is whatever is on the floor), and
# if there's nothing there then it will print a period. Otherwise it
# uses the get_visual_character() function to figure out what to place
# in the coordinates, based on the z0 item's name
# {{
def print_room(in_room):
    for i in in_room.room_coord:
        if in_room.coord_dict[i].z0 == None:
            myscreen.addstr(i[0], i[1] * 2, '.')
        else:
            visual_char = in_room.coord_dict[i].z0
            myscreen.addstr(i[0], i[1] * 2, get_visual_character(visual_char))
    myscreen.refresh()
# }}


# This allows you to place an item with map coordinates instead of
# room coordinates. The default is to randomly choose a set of
# coordinates from the 5 by 5 group that are referred to by one set
# of map coordinates
# {{
def place_with_map_coords(in_room, in_item, in_coords, adjust=(randint(0,4), randint(0,4))):
    x = in_coords[0] * 5 + adjust[0]
    y = in_coords[1] * 5 + adjust[1]
    in_room.coord_dict[(x, y)].place(in_item)
# }}




# If any character has more than 300 health, they get turned into a puppy
# {{
def change_to_puppy(character):
    pass
# }}

def check_win(player):
    pass

def check_death(player):
    pass

def update_player(player):
    check_win(player)
    check_death(player)
    

def update_characters(characters):
    for i in characters:
        if i.health > 300:
            change_to_puppy(i)
        elif i.health < 0:
            pass #kill them here
    pass

def update_room(in_room):
    for i in in_room.room_coord:
        i.update

def update(player, in_room, characters):
    update_player(player)
    update_characters(characters)
    update_room(in_room)

def build_rooms():
    coordinate_builder = []
    iterate_x = 3
    iterate_y = 3
    for i in range(iterate_x - 2, iterate_x + 2):
        for j in range(iterate_y - 2, iterate_y + 2):
            coordinate_builder.append((i, j))
    room1 = room.Room([], coordinate_builder)
    return room1
    


players = []
rooms = []

# The game is not over, and the player has not yet done anything to
# use up their turn
# {{
game_over = False
turn_finished = False
# }}

# Establish a screen {{
myscreen = curses.initscr()
# }}


# Establish a test room, and place items into that test room
# {{
test_room = build_rooms()
item1 = item.Item('barrel', 'barrel', 'furniture')
item2 = item.Item('desk', 'desk', 'furniture')
place_with_map_coords(test_room, item1, (0, 1))
place_with_map_coords(test_room, item2, (2, 3))
# }}

print_room(test_room)
sleep(3)
curses.endwin()


# This while-loop will run throughout the game
# {{
while not game_over:
    pass
# }}


