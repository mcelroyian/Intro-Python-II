# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def move(self, dir):
        if (dir == "n") and (not self.room.n_to == None):
            self.room = self.room.n_to
        elif (dir == "e") and (not self.room.e_to == None):
            self.room = self.room.e_to
        elif (dir == "s") and (not self.room.s_to == None):
            self.room = self.room.s_to
        elif (dir == "w") and (not self.room.w_to == None):
            self.room = self.room.w_to
        else:
            print("Whoops, that doesn't lead anywhere.")