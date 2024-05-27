import pygame
from constants import *
import main_entity

class Cursor(pygame.sprite.Sprite):
    """docstring for Curser."""

    def __init__(self, popup_menu):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)

        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, WHITE, self.rect, 3)

        self.rect.topleft = (BLOCK_SIZE * 5, BLOCK_SIZE * 5)
        self.is_selected = True
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.object_highlighted = None


        self.selected_item = None

        self.popup_menu = popup_menu

    def update(self, sprites):
        if self.is_selected:
            self.move()

        collisions = pygame.sprite.spritecollide(self, sprites, False)
        if collisions:
            self.object_highlighted = collisions[0].type


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and not self.moving_left:
            self.rect.x -= BLOCK_SIZE
            self.moving_left = True

        elif not keys[pygame.K_LEFT]:
            self.moving_left = False

        if keys[pygame.K_RIGHT] and not self.moving_right:
            self.rect.x += BLOCK_SIZE
            self.moving_right = True

        elif not keys[pygame.K_RIGHT]:
            self.moving_right = False

        if keys[pygame.K_UP] and not self.moving_up:
            self.rect.y -= BLOCK_SIZE
            self.moving_up = True

        elif not keys[pygame.K_UP]:
            self.moving_up = False

        if keys[pygame.K_DOWN] and not self.moving_down:
            self.rect.y += BLOCK_SIZE
            self.moving_down = True

        elif not keys[pygame.K_DOWN]:
            self.moving_down = False



        self.rect.x = max(0, min(self.rect.x, GAME_WIDTH - BLOCK_SIZE))
        self.rect.y = max(0, min(self.rect.y, GAME_HEIGHT - BLOCK_SIZE))



    def select(self, sprites):

        if self.selected_item:

            self.popup_menu.is_visible = True
            self.popup_menu.add_menu_items(self.selected_item.get_menu_items(), self.rect.topleft)
            self.popup_menu.resize((self.rect.x + BLOCK_SIZE, self.rect.y))


        else:
            collisions = pygame.sprite.spritecollide(self, sprites, False)
            if collisions:
                for coll in collisions:
                    if type(coll) == main_entity.Main_entity:
                        self.selected_item = coll
                        self.selected_item.set_is_selected()
