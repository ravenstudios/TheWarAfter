from constants import *
import pygame

class Grid():

    def __init__(self):
        pass


    def draw(self, surface):
        for r in range(GAME_HEIGHT // BLOCK_SIZE):
            pygame.draw.line(surface, WHITE, (0, r * BLOCK_SIZE), (GAME_WIDTH, r * BLOCK_SIZE), 1)
        for c in range(GAME_HEIGHT // BLOCK_SIZE):
            pygame.draw.line(surface, WHITE, (c * BLOCK_SIZE, 0), (c * BLOCK_SIZE, GAME_HEIGHT), 1)
