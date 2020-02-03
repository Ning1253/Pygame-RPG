import pygame
from Classes import classes
import current_rendered

def create_wall(xpos, ypos, room): # Wall Generation
    wall = classes.Wall(xpos, ypos)
    room.walls.append(wall) # Add wall to room wall list

def create_exit(x_or_y, pos1, pos2, room): # Room exit generation
    if x_or_y[0] == "x": # If the exit is "horizontal"
        exits = [(pos1, x_or_y[1] * 32), (pos2, x_or_y[1] * 32)] # Create a range of values for which if the player is between them they exit
    
    elif x_or_y[0] == "y": # If the exit is "vertical"
        exits = [(x_or_y[1] * 32, pos1), (x_or_y[1] * 32, pos2)] # Do the same but vertical
    
    room.exits.append(exits) # Add these exits to the room exits

def direction_collision(spr1, spr2): # Directional collision
    if spr1.rect.top == spr2.rect.bottom - 1 and spr1.rect.right > spr2.rect.left + 1 and spr1.rect.left < spr2.rect.right - 1: # If you are in the sprite in one direction
        return "Up Collision" # Return Up Coll
    if spr1.rect.bottom == spr2.rect.top + 1 and spr1.rect.right > spr2.rect.left + 1 and spr1.rect.left < spr2.rect.right - 1: # Repeat for all different directions
        return "Down Collision"
    if spr1.rect.left == spr2.rect.right - 1 and spr1.rect.top < spr2.rect.bottom - 1 and spr1.rect.bottom > spr2.rect.top + 1:
        return "Left Collision"
    if spr1.rect.right == spr2.rect.left + 1 and spr1.rect.top < spr2.rect.bottom - 1 and spr1.rect.bottom > spr2.rect.top + 1:
        return "Right Collision"

def change_room(room):
    current_rendered.all_sprites.empty() # Empty render list
    current_rendered.current_room = room # Change current room
    for wall in room.walls:
        current_rendered.all_sprites.add(wall) # Add each wall of room to render
    current_rendered.all_sprites.add(current_rendered.current_player) # Add player to render

def check_roomswitch(room, exit):
    player = current_rendered.current_player
    if (player.rect.x >= exit[0][0] and player.rect.x <= exit[1][0]) and (player.rect.y >= exit[0][1] and player.rect.y <= exit[1][1]):
        if exit[0][1] == 0 and exit[1][1] == 0:
            return "Up"
        elif exit[0][1] == 480 and exit [1][1] == 480:
            return "Down"
        elif exit[0][0] == 0 and exit[1][0] == 0:
            return "Left"
        elif exit[0][0] == 480 and exit[1][0] == 480:
            return "Right"
        
