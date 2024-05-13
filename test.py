import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Top-Down Grid with Keyboard Navigation")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (192, 192, 192)
YELLOW = (255, 255, 0)

# Constants
TILE_SIZE = 32
MAP_WIDTH, MAP_HEIGHT = 1000, 1000  # Define map dimensions
CAMERA_WIDTH, CAMERA_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT  # Define camera dimensions

# Create the map
map_data = [[0] * MAP_WIDTH for _ in range(MAP_HEIGHT)]  # Initialize map data (for demonstration purposes)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.highlighted = False

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# Camera class
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(-self.camera.x, -self.camera.y)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Clamp camera position to stay within map bounds
        x = min(0, x)
        y = min(0, y)
        x = max(-(MAP_WIDTH - self.width), x)
        y = max(-(MAP_HEIGHT - self.height), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)

# Create player
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create camera
camera = Camera(CAMERA_WIDTH, CAMERA_HEIGHT)

# Main loop
running = True
dx, dy = 0, 0  # Player movement deltas
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -TILE_SIZE
            elif event.key == pygame.K_RIGHT:
                dx = TILE_SIZE
            elif event.key == pygame.K_UP:
                dy = -TILE_SIZE
            elif event.key == pygame.K_DOWN:
                dy = TILE_SIZE
            elif event.key == pygame.K_SPACE:
                player.highlighted = not player.highlighted  # Toggle highlight

    # Update player and camera
    player.update(dx, dy)
    camera.update(player)

    # Draw map tiles
    for y in range(camera.camera.top // TILE_SIZE, camera.camera.bottom // TILE_SIZE + 1):
        for x in range(camera.camera.left // TILE_SIZE, camera.camera.right // TILE_SIZE + 1):
            tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if player.highlighted and tile_rect.collidepoint(player.rect.center):
                pygame.draw.rect(screen, YELLOW, (tile_rect.x - camera.camera.x, tile_rect.y - camera.camera.y, TILE_SIZE, TILE_SIZE))
            else:
                pygame.draw.rect(screen, GRAY, (tile_rect.x - camera.camera.x, tile_rect.y - camera.camera.y, TILE_SIZE, TILE_SIZE))

    # Draw player
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))

    pygame.display.flip()

pygame.quit()
sys.exit()
