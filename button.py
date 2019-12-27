import pygame


class Button(object):
    def __init__(self, settings, screen, display, information):
        self.settings = settings
        self.screen = screen
        self.display = display
        self.information = information

        self.flag = False

        self.font_rect = None

    def draw(self):
        if not self.flag:
            font_image = self.settings.font.render("Start", True, self.settings.block_color)
            self.font_rect = font_image.get_rect()
            self.font_rect.center = self.screen.get_rect().center
            pygame.draw.rect(self.screen, self.settings.button_color, self.font_rect)
            self.screen.blit(font_image, self.font_rect)

    def start_game(self):
        self.flag = True
        self.display.reset_data()
        self.information.reset_data()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

    def game_over(self):
        self.flag = False
        pygame.time.set_timer(pygame.USEREVENT, 0)
