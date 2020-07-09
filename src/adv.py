from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items = [Item("Sword", "a rusty sword"), Item("Pile of garbage", "Yuk... Its full of garbage.")]
room['foyer'].items = [Item("Helmet", "A shiny guards helmet, not worth much, but it will protect ya neck")]



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("The Hero", room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    print(f"Player is currently: {player.room.name}")
    print(f"{player.room.description}")
            #remove item from room
            #add item to player inventory
    dir = input("\n[n] North [e] East [s] South [w] West i[View Items] [q] Quit\n")
    if dir == "i":
        if len(player.room.items) > 0:
            print("Items in the room: ")
            for i in player.room.items:
                print(f"{i.name}")
            hands = input("To pick up item [get] [itemname] To ignore items [l] leave ")
            args = hands.split(" ")
            if args[0] == "get":
                for i in player.room.items:
                    if i.name == args[1]:
                        my_item = i
                        break
                    else:
                        my_item = None
                print(my_item)
                if my_item is not None:
                    player.room.remove_item(my_item)
                    player.add_item(my_item)
                    print(f"You picked up {my_item.name}")
                else:
                    print("That item doesn't exist")
    elif dir == "n" or dir == "e" or dir == "w" or dir == "s":
        player.move(dir)
    elif dir == "q":
        print("Thanks for playing. See you next time.")
        break
    else:
        print("Please select a valid direction or exit program\n")

#check user input
# split into array based on spacekey
# if length 1 user wants to move
# else check 1st if matches action
# 