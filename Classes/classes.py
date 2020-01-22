# File to contain general classes (eg. "Room", "Enemy", "Weapon" etc.)
import pygame
from Functions import functions # All functions for major use. 

class Room(object): # Default Room class. Actual rooms will be located in a seperate filepygame.examples.aliens.main()
    def __init__(self): # Init
        pygame.sprite.Sprite.__init__(self)
        self.walls = [] # Wall Group. To be used for easier sprite management.
        self.enemies = [] # Enemy Group. As above.
        self.build_room() # Render the room map

    def build_room(self):
        level = ["                ", # The room layout will be designed using
                 "                ", # a system in which a space indicates
                 "                ", # a square area with no wall (a path or floor)
                 "                ", # and a "W" indicates a wall space. 
                 "        W       ", # More tiles will be added as the game 
                 "        W       ", # evolves in complexity.
                 "      WWWWW     ",
                 "        W       ", # This is basically a tilemap of size 16*16.
                 "        W       ",
                 "                ",
                 "                ",
                 "                ",
                 "                ",
                 "                ",
                 "                ",
                 "                "]
        for row in range(len(level)): # Seperate each row.
            for character in range(len(level[row])): # Seperate each character.
                if level[row][character] == "W": # If W in string:
                    # This function creates a wall at the correct location on the screen.
                    functions.create_wall(character * 30 + 15, row * 30 + 15, self)
                    # The "+15" places the center to the correct position so as not to displace the entire room.
                    # "self" will be to add the wall to the list of walls in the room.


class Wall(pygame.sprite.Sprite): # Default Wall class. To be used in rooms, dungeons etc.
    def __init__(self, xpos, ypos): # Init
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30]) # Size 30 wall. Arbitrary decision.
        self.image.fill((255, 255, 255)) # Temporary colour fill.
        self.rect = self.image.get_rect() # Rect to be able to place wall, and for moving walls.
        self.rect.center = ([xpos, ypos]) # Move wall to correct position
                    
