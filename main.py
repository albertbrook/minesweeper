import pygame
from settings import Settings
from functions import Functions
from display import Display
from information import Information
from button import Button


class Game(object):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.display = Display(self.settings, self.screen)
        self.information = Information(self.settings, self.screen, self.display)
        self.button = Button(self.settings, self.screen, self.display, self.information)
        self.function = Functions(self.settings, self.screen, self.display, self.information, self.button)

    def start(self):
        while True:
            self.function.check_event()
            self.function.draw_screen()


if __name__ == '__main__':
    game = Game()
    game.start()
