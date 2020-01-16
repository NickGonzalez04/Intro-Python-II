# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        #gets the next room the player goes in
        new_room = self.current_room.get_next_room(direction)
        if new_room is not None:
            #if player enters that room the current new room is displayed
            self.current_room = new_room
            print(self.current_room)
            #if there is no room in the direction then error message
        else:
            print("Try another direction")





