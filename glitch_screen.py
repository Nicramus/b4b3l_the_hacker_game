# -*- coding: utf-8 -*-
#mozna by się zastanowić, żeby zrobić z tego splashscreen
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255,0, 0)
colors = []
colors.append(BLACK)
colors.append(WHITE)
colors.append(GREEN)
colors.append(RED)

pygame.init()

width = 700
height = 500
size = (width, height)

screen = pygame.display.set_mode(size)
screen.convert() #szybkie?
pygame.display.set_caption("dkddkddk")

#dopóki user nie kliknie krzyżyka
done = False

#zegar- odswiezanie ekranu!
clock = pygame.time.Clock()

#glowna petla gry
while not done:
    #petla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.time.delay(1)
    for color in colors:

        screen.fill(color)
        pygame.display.flip()
        pygame.time.delay(1)
    fps = clock.get_fps()
    pygame.display.set_caption(str(fps))
    clock.tick()

