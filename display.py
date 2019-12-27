import random
import pygame


class Display(object):
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.data = self.mine_data = None
        self.reset_data()

    def reset_data(self):
        self.data = [[[0, True] for _ in range(self.settings.board_size[0])]
                     for _ in range(self.settings.board_size[1])]
        self.mine_data = [[False] * self.settings.board_size[0] for _ in range(self.settings.board_size[1])]
        for _ in range(self.settings.mine_count):
            i = random.randint(0, self.settings.board_size[1] - 1)
            j = random.randint(0, self.settings.board_size[0] - 1)
            while self.data[i][j][0]:
                i = random.randint(0, self.settings.board_size[1] - 1)
                j = random.randint(0, self.settings.board_size[0] - 1)
            self.data[i][j][0] = -1
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if not self.data[i][j][0]:
                    for m in range(-1, 2):
                        for n in range(-1, 2):
                            if (0 <= i + m <= self.settings.board_size[1] - 1 and
                                    0 <= j + n <= self.settings.board_size[0] - 1 and
                                    self.data[i + m][j + n][0] == -1):
                                self.data[i][j][0] += 1

    def draw(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j][1]:
                    pygame.draw.rect(self.screen, self.settings.block_color,
                                     (j * self.settings.block_size + (j + 1) * self.settings.block_space,
                                      i * self.settings.block_size + (i + 1) * self.settings.block_space,
                                      self.settings.block_size, self.settings.block_size))
                else:
                    text = ("" if not self.data[i][j][0] else
                            "*" if self.data[i][j][0] == -1 else str(self.data[i][j][0]))
                    self.display_text(text, self.settings.block_color, i, j)
                if self.mine_data[i][j]:
                    self.display_text("*", self.settings.mine_color, i, j)

    def display_text(self, text, color, i, j):
        font_image = self.settings.font.render(text, True, color)
        font_rect = font_image.get_rect()
        font_rect.x = ((j + 0.5) * self.settings.block_size +
                       (j + 1) * self.settings.block_space - font_rect.width / 2)
        font_rect.y = ((i + 0.5) * self.settings.block_size +
                       (i + 1) * self.settings.block_space - font_rect.height / 2)
        self.screen.blit(font_image, font_rect)

    def continue_zero(self, i, j):
        for m in range(-1, 2):
            for n in range(-1, 2):
                if (0 <= i + m <= self.settings.board_size[1] - 1 and
                        0 <= j + n <= self.settings.board_size[0] - 1):
                    if not self.data[i + m][j + n][0] and self.data[i + m][j + n][1]:
                        self.data[i + m][j + n][1] = False
                        self.continue_zero(i + m, j + n)
                    self.data[i + m][j + n][1] = False
