import pygame
import Classes.classes as classes
import current_rendered
from Functions import functions

class room1(classes.Room):
    def __init__(self):
        self.level = ["WWWWEEEEEEEWWWWW", # The room layout will be designed using
                      "W              W", # a system in which a space indicates
                      "W              W", # a square area with no wall (a path or floor)
                      "W              W", # and a "W" indicates a wall space. 
                      "W              W", # More tiles will be added as the game 
                      "W      W       W", # evolves in complexity.
                      "W      W       W",
                      "W    WWWWW     W", # This is basically a tilemap of size 16*16.
                      "W      W       W",
                      "W      W       W",
                      "W              W",
                      "W              W",
                      "W              W",
                      "W              W",
                      "W              W",
                      "WWWWWWWWWWWWWWWW"]
        super().__init__()


class room2(classes.Room):
    def __init__(self):
        self.level = ["WWWWWWWWWWWWWWWW", # The room layout will be designed using
                      "W              W", # a system in which a space indicates
                      "W              W", # a square area with no wall (a path or floor)
                      "W              W", # and a "W" indicates a wall space. 
                      "W              W", # More tiles will be added as the game 
                      "W      W       W", # evolves in complexity.
                      "W      W       W",
                      "W              W", # This is basically a tilemap of size 16*16.
                      "W      W       W",
                      "W      W       W",
                      "W              W",
                      "W              W",
                      "W              W",
                      "W              W",
                      "W              W",
                      "WWWWEEEEEEEEWWWW"]
        super().__init__()
