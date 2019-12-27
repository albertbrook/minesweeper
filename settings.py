import pygame


class Settings(object):
    def __init__(self):
        self.block_size = 40
        self.block_space = 5
        self.block_color = (255, 255, 255)

        self.board_size = (30, 16)

        self.mine_count = 99
        self.mine_color = (255, 0, 0)

        self.line_size = 5
        self.line_color = (0, 0, 255)

        self.screen_size = ((self.block_size + self.block_space) * self.board_size[0] + self.block_space,
                            (self.block_size + self.block_space) * (self.board_size[1] + 1) + self.line_size)
        self.background = (0, 0, 0)

        self.font_size = 48
        self.font = pygame.font.SysFont(None, self.font_size)

        self.button_color = (0, 255, 0)
