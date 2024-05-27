import pygame
from constants import *
import main_entity

class Movment_indicator(pygame.sprite.Sprite):
    """docstring for Curser."""

    def __init__(self, movment_range):
        super().__init__()
        self.movment_range = movment_range
        self.width = (BLOCK_SIZE * self.movment_range * 2) + BLOCK_SIZE
        self.height = (BLOCK_SIZE * self.movment_range * 2) + BLOCK_SIZE
        self.x, self.y = 0, 0
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.is_visible = False

        for i in range(self.movment_range):
            x = self.movment_range * BLOCK_SIZE + BLOCK_SIZE
            y = self.movment_range * BLOCK_SIZE
            rect = pygame.Rect(x + (BLOCK_SIZE * i), y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)

            x = self.movment_range * BLOCK_SIZE - BLOCK_SIZE
            y = self.movment_range * BLOCK_SIZE
            rect = pygame.Rect(x - (BLOCK_SIZE * i), y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)

            x = self.movment_range * BLOCK_SIZE
            y = self.movment_range * BLOCK_SIZE + BLOCK_SIZE
            rect = pygame.Rect(x, y  + (BLOCK_SIZE * i), BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)

            x = self.movment_range * BLOCK_SIZE
            y = self.movment_range * BLOCK_SIZE - BLOCK_SIZE
            rect = pygame.Rect(x, y  - (BLOCK_SIZE * i), BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)





    def update(self):
        pass
