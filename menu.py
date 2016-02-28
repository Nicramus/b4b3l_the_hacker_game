import pygame

pygame.init()

class Menu:
    def __init__(self, screen, bg_color=(0,0,0)):
        self.screen = screen
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()




    def run(self):
        mainloop = True
        while mainloop:
            #limit frame speed to 50 fps
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
            #Redraw the background
            self.screen.fill(self.bg_color)
            blue=(0,0,255)
            pygame.draw.rect(screen,blue,(200,150,100,50))
            pygame.display.flip()
            pygame.display.update()



screen = pygame.display.set_mode((640, 480), 0, 32)
menu_items = ("Test Glitch Screen", "Hacking Test" "Quit")
pygame.display.set_caption("Game Menu")
gm = Menu(screen)
gm.run()
