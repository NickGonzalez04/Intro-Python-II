# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None 
        self.s_to = None 
        self.e_to = None 
        self.w_to = None 
        

    def __str__(self):
        #return the room and description of room entered and see exits
        return f"Room: {self.name}\n \n{self.description}\n, Items in that here: \n{self.get_all_exits()}"
        # gets the next room when player enters
    def get_next_room(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")    
        return None

    def room_exit(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits 
    
    def get_all_exits(self):
        return f"Exits: {','.join(self.room_exit())}"
    
    def get_items(self):
        pass

