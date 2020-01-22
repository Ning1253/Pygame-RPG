import pygame
from Classes import classes
import current_rendered
from Functions import functions

class room1(classes.Room):
    def __init__(self):
        self.level = ["                ", # The room layout will be designed using
                      "                ", # a system in which a space indicates
                      "                ", # a square area with no wall (a path or floor)
                      "                ", # and a "W" indicates a wall space. 
                      "                ", # More tiles will be added as the game 
                      "       W        ", # evolves in complexity.
                      "       W        ",
                      "     WWWWW      ", # This is basically a tilemap of size 16*16.
                      "       W        ",
                      "       W        ",
                      "                ",
                      "                ",
                      "                ",
                      "                ",
                      "                ",
                      "                "]
        super().__init__()
    
    def update(self):
        if current_rendered.current_player.rect.y < 0:
            functions.change_room(room2())

class room2(classes.Room):
    def __init__(self):
        self.level = ["                ", # The room layout will be designed using
                      "                ", # a system in which a space indicates
                      "                ", # a square area with no wall (a path or floor)
                      "                ", # and a "W" indicates a wall space. 
                      "                ", # More tiles will be added as the game 
                      "       W        ", # evolves in complexity.
                      "       W        ",
                      "                ", # This is basically a tilemap of size 16*16.
                      "       W        ",
                      "       W        ",
                      "                ",
                      "                ",
                      "                ",
                      "                ",
                      "                ",
                      "                "]
        super().__init__()
