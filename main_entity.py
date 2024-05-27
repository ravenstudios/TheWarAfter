import pygame
from constants import *

class Main_entity(pygame.sprite.Sprite):

    def __init__(self, x, y, sprite_index, movment_indicator):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.sprite_index = sprite_index
        self.spritesheet = pygame.image.load("images/TheWarAfter-Sheet.png").convert()

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)
        self.image = self.get_image_from_sprite_sheet(sprite_index)
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


        self.is_selected = False
        self.can_be_moved = True


        self.movment_range = 3
        self.movment_indicator = movment_indicator

    def update(self):
        # Redraw the image to ensure the border is applied freshly each update
        self.image = self.get_image_from_sprite_sheet(self.sprite_index)
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

        if self.is_selected:
            pygame.draw.rect(self.image, (255, 255, 0), self.image.get_rect(), 5)



    def set_is_selected(self):
        self.is_selected = not self.is_selected
        print(self.is_selected)


    def attack(self):
        print("Attack!")

    def move(self):
        self.is_selected = True
        self.movment_indicator.spread_pattern(self.rect.center, self.movment_range)



    def move_to_location(self, loc):
        self.rect.topleft = (loc)
        self.movment_indicator.is_visible = False
        self.is_selected = False



    def is_within_range(self, loc):
        test = {
            "loc": loc,
            "min x": self.rect.left - (BLOCK_SIZE * self.movment_range),
            "max x": self.rect.right + (BLOCK_SIZE * self.movment_range),
            "min y": self.rect.top - (BLOCK_SIZE * self.movment_range),
            "max y": self.rect.bottom + (BLOCK_SIZE * self.movment_range)
        }
        print(test)
        if loc[0] < self.rect.left - (BLOCK_SIZE * self.movment_range):
            return False

        if loc[0] > self.rect.right + (BLOCK_SIZE * self.movment_range):
            return False


        if loc[1] < self.rect.top - (BLOCK_SIZE * self.movment_range):
            return False


        if loc[1] > self.rect.bottom + (BLOCK_SIZE * self.movment_range):
            return False


        self.is_selected = True
        return True

    def get_menu_items(self):
        return[["Move", self.move], ["Attack", self.attack]]


    def get_image_from_sprite_sheet(self, sprite_index):
        row = sprite_index[0]
        col = sprite_index[1]
        if row < 0 or row > self.spritesheet.get_width():
            raise ValueError("row is either below 0 or larger than spritesheet")
        if col < 0 or col > self.spritesheet.get_height():
            raise ValueError("col is either below 0 or larger than spritesheet")

        image = pygame.Surface([BLOCK_SIZE // 2, BLOCK_SIZE // 2], pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), (row, col, BLOCK_SIZE, BLOCK_SIZE))
        #image.set_colorkey()
        return image
