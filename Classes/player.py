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
        self.get_inputs()
<<<<<<< Updated upstream
        self.wall_collision()
=======
        for wall in current_rendered.current_room.walls:
            if pygame.sprite.collide_rect(self, wall):
                self.wall_collision(wall)
>>>>>>> Stashed changes
        
    def get_inputs(self):
        if list_inputs.keys[pygame.K_w]:
            self.rect.y -= 1
        if list_inputs.keys[pygame.K_s]:
            self.rect.y += 1
        if list_inputs.keys[pygame.K_a]:
            self.rect.x -= 1
        if list_inputs.keys[pygame.K_d]:
            self.rect.x += 1
<<<<<<< Updated upstream
    def wall_collision(self):
        for wall in current_rendered.current_room.walls:
            if functions.direction_collision(self, wall) == "Up Collision":
                self.rect.y += 1
            if functions.direction_collision(self, wall) == "Down Collision":
                self.rect.y -= 1
            if functions.direction_collision(self, wall) == "Left Collision":
                self.rect.x += 1
            if functions.direction_collision(self, wall) == "Right Collision":
                self.rect.x -= 1
=======
    
    def wall_collision(self, wall):
        if functions.direction_collision(self, wall) == "Up Collision":
            self.rect.y += 1
        if functions.direction_collision(self, wall) == "Down Collision":
            self.rect.y -= 1
        if functions.direction_collision(self, wall) == "Left Collision":
            self.rect.x += 1
        if functions.direction_collision(self, wall) == "Right Collision":
            self.rect.x -= 1
>>>>>>> Stashed changes
