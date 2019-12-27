import pygame


class Information(object):
    def __init__(self, settings, screen, display):
        self.settings = settings
        self.screen = screen
        self.display = display

        self.first_click = self.second = self.mine = None
        self.reset_data()

    def reset_data(self):
        self.first_click = True
        self.second = 0
        self.mine = self.settings.mine_count

    def draw(self):
        size = self.settings.block_size + self.settings.block_space
        pygame.draw.line(self.screen, self.settings.line_color,
                         (0, size * self.settings.board_size[1] +
                          self.settings.block_space + self.settings.block_space // 2),
                         (size * self.settings.board_size[0] + self.settings.block_space,
                          size * self.settings.board_size[1] +
                          self.settings.block_space + self.settings.block_space // 2),
                         self.settings.line_size)
        self.draw_text(str(self.second))
        self.draw_text(str(self.mine), True)

    def draw_text(self, text, right=False):
        font_image = self.settings.font.render(text, True, self.settings.mine_color)
        font_rect = font_image.get_rect()
        font_rect.bottom = self.screen.get_rect().bottom
        if right:
            font_rect.right = self.screen.get_rect().right
        self.screen.blit(font_image, font_rect)

    def check(self):
        count = 0
        for i in range(len(self.display.data)):
            for j in range(len(self.display.data[i])):
                if not self.display.data[i][j][1]:
                    count += 1
        if count == self.settings.board_size[0] * self.settings.board_size[1] - self.settings.mine_count:
            return True
