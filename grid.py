from constants import *
import pygame

class Grid(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        # self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

        font_size = 20
        font = pygame.font.Font(None, font_size)

        for r in range(GAME_WIDTH // BLOCK_SIZE):
            for c in range(GAME_HEIGHT // BLOCK_SIZE):
                pygame.draw.line(self.image, WHITE, (0, r * BLOCK_SIZE), (GAME_WIDTH, r * BLOCK_SIZE), 1)
                pygame.draw.line(self.image, WHITE, (c * BLOCK_SIZE, 0), (c * BLOCK_SIZE, GAME_HEIGHT), 1)
                text = font.render(f"R:{r}, C:{c}", True, WHITE)  # Render text onto a surface
                text_rect = text.get_rect()  # Get the rect of the text surface
                self.image.blit(text, (r * BLOCK_SIZE + (BLOCK_SIZE // 2) - font_size, c * BLOCK_SIZE + (BLOCK_SIZE // 2) - font_size))


    def update(self):
        # self.rect = self.rect.move(world_offset)
        pass
