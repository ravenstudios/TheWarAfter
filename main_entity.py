import pygame
from constants import *

class Main_entity(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.is_selected = True
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        pass
