import pygame


class Scene():
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self, events):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError








