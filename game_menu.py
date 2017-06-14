
def create_character():
    """
    This function will go at the beginning of the game play.
    This function allows a user to choose a major player character from a menu.
    :return:
    """
    """
    :return: 
    """
    run_again = True
    while run_again == True:

        print("""
            Welcome to the game Danger Mouse!
            Your goal will be to avoid danger
            while gathering enough food from
            rooms in the castle to last a day.

            You will find various spells to
            aid you.  Keep an eye on your health,
            as you will need to eat throughout
            the day and also store food to bring
            home.

            Please choose a character to play:

            1. Mortimer - a wise mouse with a
            keen understanding of the rats
            and dogs who occupy the castle.

            2. Sydney - a clever mouse skilled
            at hiding and evasion from the rats,
            cats, dogs, and people who occupy
            the castle.

            3. Aster - a brave mouse quick to
            cause fright in cats and people
            who occupy the castle.

            """)

        try:
            choice = input("Do you choose character 1, 2, or 3?\n:")
            if choice == '1' or choice == '2' or choice == '3':
                run_again = False

        except KeyError:
            continue

    if choice == '1':
        """
            Creates character Mortimer.  
        """
        befriend_1 = item.Spell("befriend")
        befriend_2 = item.Spell("befriend")
        char_list = ['Mortimer', 'You are an elderly mouse who\'s body is worn, but who\'s smile is genuine.',
                     'library', [befriend_1, befriend_2]]

    elif choice == '2':
        """
            Creates character Sydney.
        """
        hide_1 = item.Spell("hide")
        hide_2 = item.Spell("hide")
        char_list = ['Sydney',
                     'You try to look at yourself, but you quickly dodge your own gaze and hide in the shadows.',
                     'nest', [hide_1, hide_2]]

    elif choice == '3':
        """
            Creates character Aster.
        """
        scare_1 = item.Spell("scare")
        scare_2 = item.Spell("scare")
        char_list = ['Aster',
                     'Your physical appearance is not notable, but you act with confidence that leaves others intimidated.',
                     'chapel', [scare_1, scare_2]]

    """
    Uses variable player to instantiate a Mouse character and call the needed list of attributes.
    Returns the Mouse character.  
    """
    player = character.Mouse(char_list[0], char_list[1], char_list[2])
    player.inventory.put_in_quiet(char_list[3][0])
    player.inventory.put_in_quiet(char_list[3][1])
    return player


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


game_over = False


def pretty_print_dict(dict):
    for k in dict:
        print('{}. {}'.format(k, dict[k]))


def check_win(player):
    score = 0
    for thing in player.inventory.bag_of_holding:
        if thing.type == 'food':
            score += thing.score
    if score >= 60:
        print('You win!')
        return True
    else:
        return False


def check_death(player):
    if player.health <= 0:
        print('You have died')
        return True

danger_mouse = create_character()

room_controller.characters.append(danger_mouse)

current_room = room_controller.room_dict[danger_mouse.location]

danger_dict = {'Danger mouse': danger_mouse}
current_room.look()
print("You are a 🐭")
while not game_over:
    print('HP: {}'.format(danger_mouse.health))
    room_controller.update_all()

    action_select = str(input('1. Look \n'
                              '2. Move \n'
                              '3. Peek through a door \n'
                              '4. Inventory \n'
                              '5. Interact\n')).lower()

    if '1' in action_select or 'look' in action_select:
        i = 1
        look_dict = {}
        look_dict[str(i)] = danger_dict['Danger mouse']
        i += 1
        for door in current_room.doors:
            look_dict[str(i)] = room_controller.door_dict[door]
            i += 1
        for item in current_room.inventory.bag_of_holding:
            look_dict[str(i)] = item
            i += 1
        for character in current_room.characters:
            look_dict[str(i)] = character
            i += 1
        valid_input = False
        while not valid_input:
            try:
                pretty_print_dict(look_dict)
                look_select = input('What do you want to look at?')
                look_dict[look_select].look()
                valid_input = True
            except KeyError:
                print("Not a valid input")

    elif '2' in action_select or 'move' in action_select:
        i = 1
        move_dict = {}
        for door in current_room.doors:
            move_dict[str(i)] = door
            i += 1
        valid_input = False
        while not valid_input:
            try:
                for k in move_dict:
                    print(k + '. ' + move_dict[k])
                move_select = input()
                current_room = current_room.open_door(room_controller.door_dict[move_dict[move_select]])
                danger_mouse.location = current_room.name
                current_room.look()
                valid_input = True
            except KeyError:
                print("Not a valid input")

    elif '3' in action_select or 'peek' in action_select:
        i = 1
        peek_dict = {}
        for door in current_room.doors:
            peek_dict[str(i)] = door
            i += 1

        valid_input = False
        while not valid_input:
            try:
                for k in peek_dict:
                    print(k + '. ' + peek_dict[k])
                peek_select = input()
                current_room.peek_room(room_controller.door_dict[peek_dict[peek_select]])
                valid_input = True
            except KeyError:
                print("Not a valid input")

    elif '4' in action_select or 'inventory' in action_select:
        # inv_dict = danger_mouse.inventory.list_inventory()
        # pretty_print_dict(inv_dict)
        item_dict = {}
        i = 1
        for item in danger_mouse.inventory.bag_of_holding:
            item_dict[str(i)] = item
            i += 1
        pretty_print_dict(item_dict)

        item_select = input('Enter the name of the item you wish to select: \n:')

        item_action = input('What do you wish to do with this item? \n'
                            '1. Look at item \n'
                            '2. Use item \n')  # '3. Drop item\n')

        if '1' in item_action:
            danger_mouse.inventory.look(item_select)
            print('\n')
        if '2' in item_action:
            item_dict[item_select].use_item(danger_mouse, room_controller.room_dict)
        if '3' in item_action:
            current_room.inventory.put_in(danger_mouse.inventory.poplar(item_select))

    elif '5' in action_select or 'interact' in action_select:
        action_dict = {}
        i = 1
        for door in current_room.doors:
            action_dict[str(i)] = room_controller.door_dict[door]
            i += 1
        for stuff in current_room.inventory.bag_of_holding:
            action_dict[str(i)] = stuff
            i += 1
        for character in current_room.characters:
            action_dict[str(i)] = character
            i += 1
        pretty_print_dict(action_dict)
        action_item = input('What do you want to interact with?\n')
        action_dict[action_item].action(current_room, danger_mouse)

    else:
        print('Please enter a valid menu option.')

    game_over = check_death(danger_mouse)
    if not game_over:
        game_over = check_win(danger_mouse)

print('Thanks for playing')
