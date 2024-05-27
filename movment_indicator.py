import pygame
from constants import *
import main_entity

class Movment_indicator(pygame.sprite.Sprite):
    """docstring for Curser."""

    def __init__(self, ):
        super().__init__()

        self.width = 0
        self.height = 0
        self.x, self.y = 0, 0
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.is_visible = False

    def cross_pattern(self, loc, movment_range):
        self.is_visible = True
        self.width = (BLOCK_SIZE * movment_range * 2) + BLOCK_SIZE
        self.height = (BLOCK_SIZE * movment_range * 2) + BLOCK_SIZE
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = loc


        for i in range(movment_range):
            x = movment_range * BLOCK_SIZE + BLOCK_SIZE
            y = movment_range * BLOCK_SIZE
            rect = pygame.Rect(x + (BLOCK_SIZE * i), y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)

            x = movment_range * BLOCK_SIZE - BLOCK_SIZE
            y = movment_range * BLOCK_SIZE
            rect = pygame.Rect(x - (BLOCK_SIZE * i), y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)

            x = movment_range * BLOCK_SIZE
            y = movment_range * BLOCK_SIZE + BLOCK_SIZE
            rect = pygame.Rect(x, y  + (BLOCK_SIZE * i), BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)

            x = movment_range * BLOCK_SIZE
            y = movment_range * BLOCK_SIZE - BLOCK_SIZE
            rect = pygame.Rect(x, y  - (BLOCK_SIZE * i), BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.image, (255, 255, 255, 225), rect)




    def spread_pattern(self, loc, movment_range):
        self.is_visible = True
        self.width = (BLOCK_SIZE * movment_range * 2) + BLOCK_SIZE
        self.height = (BLOCK_SIZE * movment_range * 2) + BLOCK_SIZE
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = loc


        for r in range(movment_range * movment_range):
            for c in range(movment_range * movment_range):
                pygame.draw.rect(self.image, (255, 255, 255, 225), (r * BLOCK_SIZE, c * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            # x = movment_range * BLOCK_SIZE + BLOCK_SIZE
            # y = movment_range * BLOCK_SIZE
            # rect = pygame.Rect(x + (BLOCK_SIZE * i), y, BLOCK_SIZE, BLOCK_SIZE)
            # pygame.draw.rect(self.image, (255, 255, 255, 225), rect)
            #
            # x = movment_range * BLOCK_SIZE - BLOCK_SIZE
            # y = movment_range * BLOCK_SIZE
            # rect = pygame.Rect(x - (BLOCK_SIZE * i), y, BLOCK_SIZE, BLOCK_SIZE)
            # pygame.draw.rect(self.image, (255, 255, 255, 225), rect)
            #
            # x = movment_range * BLOCK_SIZE
            # y = movment_range * BLOCK_SIZE + BLOCK_SIZE
            # rect = pygame.Rect(x, y  + (BLOCK_SIZE * i), BLOCK_SIZE, BLOCK_SIZE)
            # pygame.draw.rect(self.image, (255, 255, 255, 225), rect)
            #
            # x = movment_range * BLOCK_SIZE
            # y = movment_range * BLOCK_SIZE - BLOCK_SIZE
            # rect = pygame.Rect(x, y  - (BLOCK_SIZE * i), BLOCK_SIZE, BLOCK_SIZE)
            # pygame.draw.rect(self.image, (255, 255, 255, 225), rect)



    def update(self):
        pass
