from constants import *
import pygame

import main_entity
import grid


clock = pygame.time.Clock()
surface = pygame.display.set_mode((CAMERA_VIEW_WIDTH, CAMERA_VIEW_HEIGHT))

pygame.init()


grid = grid.Grid()
player_group = pygame.sprite.GroupSingle()

player = main_entity.Main_entity(50, 50)
test = main_entity.Main_entity(600, 64)

player_group.add(player)
player_group.add(test)

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    grid.draw(surface)
    player_group.draw(surface)
    pygame.display.flip()



def update():
    pass



if __name__ == "__main__":
    main()
