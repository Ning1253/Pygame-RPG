import pygame
from Classes import player, classes, rooms # All classes (rooms, player, wall, enemies etc.)
from main_loop import loop
import current_rendered
# Initialise
pygame.init()
running = True

# Main Settings
FPS = 60
screen_size = (480, 480)
clock = pygame.time.Clock()

# Display Setup
display = pygame.display.set_mode(screen_size)

# Main Loop
loop(running, pygame.time.Clock(), display, FPS, current_rendered.all_sprites)
