# File to contain Player and Inventory Classes
import pygame
import get_inputs as list_inputs
from Functions import functions
import current_rendered

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Init Sprite
        self.image = pygame.Surface([20, 20]) # Temporary White square for image. Will be replaced with player at later date
        self.image.fill([255, 255, 255])
        self.rect = self.image.get_rect() # Player hitbox will be a rectangle around their image
    
    def update(self): # Update function, to be run every frame
        self.get_inputs() # Get inputs
        for wall in current_rendered.current_room.walls: # Check direction collision for each wall
            if pygame.sprite.collide_rect(self, wall):   # Only if there is actually a collision ongoing
                self.wall_collision(wall) # Doing this therefore reduces lag
        
    def get_inputs(self):
        if list_inputs.keys[pygame.K_w]: # If pressing "w"
            self.rect.y -= 1 # Move Up
        if list_inputs.keys[pygame.K_s]: # Same for other "asd" below
            self.rect.y += 1
        if list_inputs.keys[pygame.K_a]:
            self.rect.x -= 1
        if list_inputs.keys[pygame.K_d]:
            self.rect.x += 1
    
    def wall_collision(self, wall):
            if functions.direction_collision(self, wall) == "Up Collision": # If Up Collision returned,
                self.rect.y += 1 # Move down out of the collision
            if functions.direction_collision(self, wall) == "Down Collision": # Same for other collisions below
                self.rect.y -= 1
            if functions.direction_collision(self, wall) == "Left Collision":
                self.rect.x += 1
            if functions.direction_collision(self, wall) == "Right Collision":
                self.rect.x -= 1
