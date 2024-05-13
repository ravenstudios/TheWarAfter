from constants import *
import pygame
import main_biom
import random

class Map_manager():
    def __init__(self):

        self.biom = pygame.sprite.Group()
        self.types = ["Lava", "Acid", "Water", "Dirt"]



    def make_map(self):
        for r in range(ROWS):
            for c in range(COLS):
                type = self.types[random.randint(0, len(self.types) - 1)]
                x = r * BLOCK_SIZE
                y = c * BLOCK_SIZE
                self.biom.add(main_biom.Main_biom(x, y, type))

        return self.biom
