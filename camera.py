from constants import *
import pygame


class Camera:
    def __init__(self):

        self.width = CAMERA_VIEW_WIDTH
        self.height = CAMERA_VIEW_HEIGHT
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.world_offset = [0, 0]



    def move_into_camera(self, entity):
        return entity.rect.move(-self.rect.x, -self.rect.y)


    def update(self, target):
        x = target.rect.centerx - self.width // 2
        y = target.rect.centery - self.height // 2

        x = max(0, x)
        y = max(0, y)
        x = min(GAME_WIDTH - self.width, x)
        y = min(GAME_HEIGHT - self.height, y)

        self.rect = pygame.Rect(x, y, self.width, self.height)


    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (0, 0, CAMERA_VIEW_WIDTH, CAMERA_VIEW_HEIGHT), 3)
