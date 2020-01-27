import pygame
import Classes.classes as classes
import current_rendered
from Functions import functions

class room1(classes.Room):
    def __init__(self):
        self.level = ["      EEEEE     ", # The room layout will be designed using
                      "                ", # a system in which a space indicates
                      "                ", # a square area with no wall (a path or floor)
                      "                ", # and a "W" indicates a wall space. 
                      "                ", # More tiles will be added as the game 
                      "E      W        ", # evolves in complexity.
                      "E      W       E",
                      "E    WWWWW     E", # This is basically a tilemap of size 16*16.
                      "E      W       E",
                      "E      W       E",
                      "E              E",
                      "                ",
                      "                ",
                      "                ",
                      "                ",
                      "       EEEE     "]
        super().__init__()


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
