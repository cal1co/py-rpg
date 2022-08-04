import pygame
from settings import *

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface 
        
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    # __init__()
    def create_map(self):
        for row in WORLD_MAP:
            print(row)
    # create_map()
    def run(self):
        pass
    # run()