import pygame
from Classes import classes

def create_wall(xpos, ypos, room): # Wall Generation
    wall = classes.Wall(xpos, ypos)
    room.walls.append(wall) # Add wall to room wall list
