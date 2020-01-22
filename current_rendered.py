import pygame

global all_sprites
global current_room

# This will be filled in to match the room currently rendered,
# to allow access from player and collisions to walls, enemies etc.
current_room = ""
current_player = ""

# Main Groups Setup
all_sprites = pygame.sprite.Group()