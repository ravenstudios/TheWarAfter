import pygame
from constants import *

# Ensure that constants like BLOCK_SIZE and BLACK are defined
# try:
#     assert BLOCK_SIZE is not None
#     assert BLACK is not None
# except NameError:
#     print("Ensure BLOCK_SIZE and BLACK are defined in your constants module.")
#     raise

class Popup_menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.row_width = 3
        self.row_height = 6
        self.width = BLOCK_SIZE * self.row_width
        self.height = BLOCK_SIZE * self.row_height

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # self.image.fill((200, 200, 200))

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

        self.is_visible = False
        self.gap = BLOCK_SIZE // 4
        self.menu_items = []

        pygame.font.init()  # Initialize font module
        self.font_size = 36
        self.font = pygame.font.Font(None, self.font_size)  # Default font, size 36

    #
    #
    # def add_menu_item(self, title, callback, rect):
    #     self.menu_items.append(Menu_item(title, callback, rect))



    def add_menu_items(self, items, loc):
        self.menu_items = [] #clear every time we make a new menu
        for item in items:
            rect = pygame.Rect(loc[0], loc[1] + (len(self.menu_items) * BLOCK_SIZE) + (self.gap * len(self.menu_items)), BLOCK_SIZE * self.row_width, BLOCK_SIZE)


            item_to_add = Menu_item(item[0], item[1], rect)
            # print(f"ita:{item_to_add.rect}")
            self.menu_items.append(item_to_add)



    def update(self):
        if self.is_visible:
            self.image.fill((200, 200, 200))  # Clear the menu background
            for index, item in enumerate(self.menu_items):
                rect = pygame.Rect((0, (index * BLOCK_SIZE) + (self.gap * index), BLOCK_SIZE * self.row_width, BLOCK_SIZE))
                pygame.draw.rect(self.image, BLACK, rect, 5)

                # Render the text
                text_surface = self.font.render(item.title, True, (0, 0, 255))
                text_rect = text_surface.get_rect()
                text_rect.center = rect.center
                self.image.blit(text_surface, text_rect)




    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                for item in self.menu_items:
                    if item.rect.collidepoint(event.pos):
                        if item.callback:
                            item.callback()
                            self.is_visible = False
                            self.menu_items = []
                        else:
                            print(f"Clicked {item.title}")





    def toggle_visibility(self):
        self.is_visible = not self.is_visible




    def resize(self, loc):
        self.row_height = len(self.menu_items)
        self.width = BLOCK_SIZE * self.row_width
        self.height = (BLOCK_SIZE * self.row_height) + (self.gap * self.row_height)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = loc
        for index, item in enumerate(self.menu_items):
            item.rect.topleft = (loc[0], loc[1] + (BLOCK_SIZE * index) + (self.gap * index))

class Menu_item:
    def __init__(self, title, callback, rect):
        self.title = title
        self.callback = callback
        self.rect = rect
