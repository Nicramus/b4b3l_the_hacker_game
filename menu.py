# -*- coding: utf-8 -*-

import pygame

pygame.init()

class Menu:
    def __init__(self, screen, bg_color=(0,0,0)):
        self.screen = screen
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.screen_size = screen.get_size() #tuple-> width, height

        #only for test
        liberationserif_name = pygame.font.get_fonts()[0]
        liberationserif = pygame.font.SysFont(liberationserif_name, 20, False, False)

        self.vga_437_font = liberationserif #pygame.font.Font("resources/fonts/Terminus.ttf", 20)
        self.set_center_coordinates()
        self.init_menu_properties()

    def init_menu_properties(self):
        self.menu_element_color = (0,0,255) #blue
        self.menu_text_color = (255,255,255) #white
        self.menu_element_width = 200
        self.menu_element_height = 50
        self.gap = 90
        self.menu_positions = ("Nowa gra", "Swobodne hakowanie", "Wyjście")
        #x_y_position = self.set_center_coordinates()
        #self.menu_item_y_position = y_rect_position = x_y_position[1]

    def set_center_coordinates(self):
        self.x_center_position = self.screen_width / 2
        self.y_center_position = self.screen_height / 2

    def create_menu_element(self, label_str, y_center_position):
        "create menu element, render font-label on the element"
        x_center_position = self.x_center_position - self.menu_element_height / 2
        pygame.draw.rect(screen, self.menu_element_color,
                                                  (x_center_position, y_center_position) +
                                                  (self.menu_element_width, self.menu_element_height))
        label = self.vga_437_font.render(label_str, True, self.menu_text_color)
        self.screen.blit(label, (x_center_position, y_center_position))

    def generate_menu(self):
        "generate menu elements in loop"
        y_center_position = 100
        for menu_item in self.menu_positions:
            self.create_menu_element(menu_item, y_center_position)
            y_center_position = y_center_position + 90

    def animate_menu(self):
        #simple menu animation :D
        pass

    def run(self):
        mainloop = True
        while mainloop:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            self.screen.fill(self.bg_color)

            self.generate_menu()
            pygame.display.flip()
            pygame.display.update()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("B4B3L")
gm = Menu(screen)
gm.run()
