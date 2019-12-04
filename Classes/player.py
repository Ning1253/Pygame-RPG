# File to contain Player and Inventory Classes
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Init Sprite
        self.image = pygame.Surface([20, 20]) # Temporary White square for image. Will be replaced with player at later date
        self.image.fill([255, 255, 255])
        self.rect = self.image.get_rect() # Player hitbox will be a rectangle around their image
    
    def update(self): # Update function, to be run every frame
        return True # Empty for now