# -*- coding: utf-8 -*-
import pygame
#import li
#from pygame.locals import *

class Main:
    def __init__(self):
        print "__init__"
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400 #wymagane
        self.last = pygame.time.get_ticks()
        self.fps = 60.0 #ilosc klatek
        self.clock = pygame.time.Clock()
        self.step = 0 #krok? chyba idziem tą drogą xD

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.screen = pygame.display.get_surface()
        self.screenrect = self.screen.get_rect()
        self.vga_437_font = pygame.font.Font("resources/fonts/Perfect_DOS_VGA_437_Win.ttf", 20)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_cleanup(self):
         pygame.quit()

    def display_fps(self):
        caption = "FPS: {:.2f}".format(self.clock.get_fps())
        pygame.display.set_caption(caption)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        #głowna pętla gry
        while( self._running ):

           #list = pygame.font.get_fonts()

           #pętla zdarzen
           for event in pygame.event.get():
               self.on_event(event)
               self.display_fps()
        self.on_cleanup()

if __name__ == "__main__":
    main = Main()
    main.on_execute()






