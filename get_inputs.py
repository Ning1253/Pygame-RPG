# Inputs for frame
import pygame

global inputs

def grab_inputs():
    global inputs
    inputs = pygame.event.get() # To be run every frame
