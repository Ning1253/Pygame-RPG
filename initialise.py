import pygame
from Classes import player # All classes (rooms, player, wall, enemies etc.)
import main

# Initialise
pygame.init()
running = True

# Main Settings
FPS = 60
screen_size = (480, 480)
clock = pygame.time.Clock()

# Display Setup
display = pygame.display.set_mode(screen_size)

# Main Groups Setup
all_sprites = pygame.sprite.Group()

# Main Loop
main.loop(running, pygame.time.Clock(), display, FPS, all_sprites)