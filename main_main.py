# -*- coding: utf-8 -*-
import pygame
from glitch_screen import GlitchScreen
from scene import Scene

pygame.init()

#test!
class CircleScene(Scene):

    def __init__(self):
        #in python 3, you can call just super().__init__()
        #super(TestScene, self).__init__()
        self.circle_color = pygame.Color(255, 0, 0, 0)

    def render(self, screen):
        pygame.draw.circle(screen, self.circle_color, (300, 50), 20, 0)

    def update(self, events):
        pass

    def handle_events(self, event):
        #for e in events:
        if event.type == pygame.K_ESCAPE:
            print ("ESCAPE PRESSED")

class SceneManager():
    def __init__(self):
        "set initial scene- menu, splash screen etc"
        self.go_to(GlitchScreen())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class Main():
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        pygame.display.set_caption("B4B3L")
        self.scene_manager = SceneManager()

    def exit_game(self, event):
        if event.type == pygame.QUIT:
            print "Exiting program!"
            pygame.quit()

    def run(self):
        mainloop = True
        # pętla główna gry
        while mainloop:
            #print ("main loop")
            for event in pygame.event.get():
                self.exit_game(event)
                self.scene_manager.scene.handle_events(event)
                #             manager.scene.update(event)
                self.scene_manager.scene.render(self.screen)
                pygame.display.flip()




# def main():
#     pygame.init()
#     screen_dimension = (640, 480) #width, height
#     screen = pygame.display.set_mode(screen_dimension, 0, 32)
#     pygame.display.set_caption("Test Scene")
#
#     timer = pygame.time.Clock()
#     running = True
#
#     manager = SceneManager()
#
#     while running:
#         timer.tick(60)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print ("Exit!")
#                 running = False
#                 return
#             manager.scene.handle_events(pygame.event.get())
#             manager.scene.update(event)
#             manager.scene.render(screen)
#             pygame.display.flip()
#
# main()

main = Main()
main.run()
