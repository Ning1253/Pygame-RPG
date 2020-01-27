# File to contain general classes (eg. "Room", "Enemy", "Weapon" etc.)
import pygame, current_rendered
from Functions import functions # All functions for major use. 
import Classes

class Room(object): # Default Room class. Actual rooms will be located in a seperate file
    def __init__(self): # Init
        self.walls = [] # Wall Group. To be used for easier sprite management.
        self.enemies = [] # Enemy Group. As above.
        self.exits = [] # Exits group
        self.build_room() # Render the room map

    def build_room(self):
        for row in range(len(self.level)): # Seperate each row.
            for character in range(len(self.level[row])): # Seperate each character.
                if self.level[row][character] == "W": # If W in string:
                    # This function creates a wall at the correct location on the screen.
                    functions.create_wall(character * 30 + 15, row * 30 + 15, self)
                    # The "+15" places the center to the correct position so as not to displace the entire room.
                    # "self" will be to add the wall to the list of walls in the room.
                if self.level[row][character] == "E": # If E in string:
                    if row == 0:
                        functions.create_exit(["x", 0], character * 30, (character + 1) * 30, self) # If you are on top row create exit on that row
                    elif row == 15:
                        functions.create_exit(["x", 15], character * 30, (character + 1) * 30, self) # If on bottom row
                    elif character == 0:
                        functions.create_exit(["y", 0], row * 30, (row + 1) * 30, self) # If on left column
                    elif character == 15:
                        functions.create_exit(["y", 15], row * 30, (row + 1) * 30, self) # If on right column
    
    def update(self):
        for exit in self.exits:
            if functions.check_roomswitch(self, current_rendered.current_player, exit) != None: # Check to see if should switch rooms
                functions.change_room(Classes.room_map.room_map[1])

class Wall(pygame.sprite.Sprite): # Default Wall class. To be used in rooms, dungeons etc.
    def __init__(self, xpos, ypos): # Init
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30]) # Size 30 wall. Arbitrary decision.
        self.image.fill((255, 255, 255)) # Temporary colour fill.
        self.rect = self.image.get_rect() # Rect to be able to place wall, and for moving walls.
        self.rect.center = ([xpos, ypos]) # Move wall to correct position
                    
