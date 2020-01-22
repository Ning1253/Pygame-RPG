import pygame
from Classes import classes
import current_rendered

def create_wall(xpos, ypos, room): # Wall Generation
    wall = classes.Wall(xpos, ypos)
    room.walls.append(wall) # Add wall to room wall list

def direction_collision(spr1, spr2):
    if spr1.rect.top == spr2.rect.bottom - 1 and spr1.rect.right > spr2.rect.left + 1 and spr1.rect.left < spr2.rect.right - 1:
        return "Up Collision"
    if spr1.rect.bottom == spr2.rect.top + 1 and spr1.rect.right > spr2.rect.left + 1 and spr1.rect.left < spr2.rect.right - 1:
        return "Down Collision"
    if spr1.rect.left == spr2.rect.right - 1 and spr1.rect.top < spr2.rect.bottom - 1 and spr1.rect.bottom > spr2.rect.top + 1:
        return "Left Collision"
    if spr1.rect.right == spr2.rect.left + 1 and spr1.rect.top < spr2.rect.bottom - 1 and spr1.rect.bottom > spr2.rect.top + 1:
        return "Right Collision"

def change_room(room):
    current_rendered.all_sprites.empty()
    current_rendered.current_room = room
    for wall in room.walls:
        current_rendered.all_sprites.add(wall)
    current_rendered.all_sprites.add(current_rendered.current_player)