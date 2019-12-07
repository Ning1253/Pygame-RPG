# Inputs for frame
import pygame

def grab_inputs():
    global inputs
    global keys
    inputs = pygame.event.get() # To be run every frame
    keys = pygame.key.get_pressed()