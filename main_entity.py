from constants import *
import pygame

class Main_entity(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        # self.spritesheet = pygame.image.load(SPRITESHEET).convert()
        # self.y_sprite_sheet_index = y_sprite_sheet_index

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        # self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # self.frame = 0
        # self.max_frame = (self.spritesheet.get_width() // BLOCK_SIZE) - 1
        # self.animation_speed = TICK_RATE / self.max_frame / 100
        #
        # self.coords = pygame.math.Vector2(self.rect.x, self.rect.y)

        print(self.rect)

    def update(self):

        pass
