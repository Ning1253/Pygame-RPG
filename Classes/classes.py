# File to contain general classes (eg. "Room", "Enemy", "Weapon" etc.)
import pygame

class Room(object): # Default Room class. Actual rooms will be located in a seperate filepygame.examples.aliens.main()
    def __init__(self): # Init
        pygame.sprite.Sprite.__init__(self)
        self.walls = []
        self.enemies = []
        