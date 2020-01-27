import pygame
from Classes import player, classes, room_map # All classes (rooms, player, wall, enemies etc.)
from main_loop import loop
import current_rendered
# Initialise
pygame.init()
running = True

# Main Settings
FPS = 144
screen_size = (480, 480)
clock = pygame.time.Clock()

# Display Setup
display = pygame.display.set_mode(screen_size)

#Test Stuff
current_rendered.current_player = player.Player() # Create Player
current_rendered.current_room = room_map.room_map[0] # Add "room1" to the display
current_rendered.all_sprites.add(current_rendered.current_player) # Add player to all sprites

for wall in current_rendered.current_room.walls:
    current_rendered.all_sprites.add(wall) # Add each wall of room to the display

# Main Loop
loop(running, pygame.time.Clock(), display, FPS)
