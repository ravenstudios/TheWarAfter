from constants import *
import pygame

import main_entity
import grid
import camera
import map_manager
import cursor

clock = pygame.time.Clock()
surface = pygame.display.set_mode((CAMERA_VIEW_WIDTH, CAMERA_VIEW_HEIGHT))

pygame.init()

camera = camera.Camera()

grid = grid.Grid()

cursor = cursor.Cursor()

player = main_entity.Main_entity(64 * 5, 64 * 5, (0, 0))
player2 = main_entity.Main_entity(64 * 4, 64 * 4, (32, 0))


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()

mobs.add(player, player2)

map = map_manager.Map_manager()
all_sprites.add(map.make_map())
all_sprites.add(mobs)

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

            if event.type == pygame.KEYUP:
                if event.scancode == 40:
                    cursor.select(all_sprites)

        update()
        draw()


    pygame.quit()


def display_hud(surface):
    font_size = 24
    font = pygame.font.Font(None, font_size)
    pygame.draw.rect(surface, (192, 192, 192), (0, 0, CAMERA_VIEW_WIDTH, font_size))
    text = font.render(f"R:{cursor.rect.y // BLOCK_SIZE}, C:{cursor.rect.x // BLOCK_SIZE}, Biome Type:{cursor.object_highlighted}", True, RED)  # Render text onto a surface
    text_rect = text.get_rect(center=(GAME_WIDTH // 3, font_size // 2))  # Get the rect of the text surface
    surface.blit(text, text_rect)


def draw():


    surface.fill((0, 0, 0))#background

    for entity in all_sprites:
        surface.blit(entity.image, camera.move_into_camera(entity))
    surface.blit(cursor.image, camera.move_into_camera(cursor))

    display_hud(surface)
    camera.draw(surface)

    pygame.display.flip()



def update():
    # world_offset = camera.get_world_offset(player)
    # grid.update(world_offset)
    cursor.update(all_sprites)
    all_sprites.update()
    camera.update(cursor)


if __name__ == "__main__":
    main()
