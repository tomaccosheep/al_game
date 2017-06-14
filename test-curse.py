import curses
from time import sleep
import room
from random import randint
import item


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


# Establish a screen {{
myscreen = curses.initscr()
# }}


# Establish a test room, and place items into that test room
# {{
test_room = room.Room('al', 'its als room', [], [], [(0, 1), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)])
item1 = item.Item('barrel', 'barrel', 'furniture')
item2 = item.Item('desk', 'desk', 'furniture')
place_with_map_coords(test_room, item1, (0, 1))
place_with_map_coords(test_room, item2, (2, 3))
# }}

print_room(test_room)
sleep(3)
curses.endwin()

exit()
