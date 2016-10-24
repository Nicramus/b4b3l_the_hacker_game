# -*- coding: utf-8 -*-
import pygame
import six

from os import path

class MovieHacker:
    EXIT_CODE = 0

    # this is the way how you do the builder pattern in python
    # default params
    def __init__(self, screen, text_to_animate, font):
        self.screen = screen
        if (isinstance(text_to_animate, six.string_types)): #compatible with python 3.x
            self.text_to_animate = text_to_animate

        is_path_exists = path.exists(text_to_animate) #to jest bez sensu, na wejsciu po prostu przyjmuje tekst
        self.font = font
        # default white color
        self.font_color = pygame.Color("#FFFFFF")
        # default keysound empty
        self.key_sound = None
        # length of displayed text
        self.iteration = 0
        self.font_delay = 300
        self.user_control = False
        self.line_height = 0
        self.text_stack = text_to_animate.split("\n") #make stack/list

    def set_font_color(self, font_color):
        self.font_color = font_color

    #dodac klika roznych dzwiekow
    def set_key_sound(self, key_sound):
        self.key_sound = key_sound

    def set_font_delay(self, font_delay):
        self.font_delay = font_delay

    def set_user_control(self, user_control):
        "when true user type then "
        self.user_control = user_control

    def set_background_color(self, color=pygame.Color('#FBFF00')):
        "background setting"
        self.screen.fill(color)
        pygame.display.update()

    # Font rendering is not thread safe:
    # only a single thread can render text at any time.
    def __render_text(self, rendered_string):
        # label is surface type
        # True is antialiasing parameter
        # print dir(self.font) #show all atttrs
        anti_aliasing = False
        label = self.font.render(rendered_string, anti_aliasing, self.font_color)
        #label to typ surface- więc mozna go pocisnąc jakos
        #label.scroll(5,0)


        self.screen.blit(label, (0, self.line_height))

    def __convert_string_to_stack(self):
        pass

    def animete_by_keystrokes(self):
        # animate text after keyboard hits (and mouse) HACK BY MOUSE!!!
        pass

    def set_font_color(self, font_color):
        self.font_color = font_color

    def __play_key_sound(self):
        "play sound key, if is passed"
        if (self.key_sound is not None):
            self.key_sound.play(0)

    def __event_loop(self):
        pass

    def __update_screen(self):
        pygame.display.update()
        self.__play_key_sound()

    def animate_text(self):
        for line_index, line_str in enumerate(self.text_stack):
            font_height = self.font.size(line_str)[1]
            self.line_height += font_height
            for index, char in enumerate(line_str):
                  string_part = line_str[0:index]

                  self.__render_text(string_part)

                  for event in pygame.event.get():
                    if self.user_control:
                        if pygame.key.get_pressed():
                            self.__update_screen()

                  if not self.user_control:
                    self.__update_screen()

                  pygame.time.wait(self.font_delay)

