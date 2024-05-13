import pygame
from constants import *


class Main_biom(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.type = type


        if type == "Lava":
            self.image.fill((255, 0, 0))

        if type == "Acid":
            self.image.fill((0, 255, 0))

        if type == "Water":
            self.image.fill((0, 0, 255))

        if type == "Dirt":
            self.image.fill((210,180,140))



        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass
