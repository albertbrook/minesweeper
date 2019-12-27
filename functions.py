import pygame


class Functions(object):
    def __init__(self, settings, screen, display, information, button):
        self.settings = settings
        self.screen = screen
        self.display = display
        self.information = information
        self.button = button

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (self.button.font_rect[0] < event.pos[0] < self.button.font_rect[0] + self.button.font_rect[2] and
                        self.button.font_rect[1] < event.pos[1] < self.button.font_rect[1] + self.button.font_rect[3]):
                    if not self.button.flag:
                        self.button.start_game()
                        return
                if not self.button.flag:
                    return
                i = event.pos[1] // (self.settings.block_size + self.settings.block_space)
                j = event.pos[0] // (self.settings.block_size + self.settings.block_space)
                if (event.pos[1] > i * self.settings.block_size + (i + 1) * self.settings.block_space and
                        event.pos[0] > j * self.settings.block_size + (j + 1) * self.settings.block_space):
                    self.event_button(event, i, j)
            elif event.type == pygame.USEREVENT:
                self.information.second += 1

    def draw_screen(self):
        self.screen.fill(self.settings.background)
        self.display.draw()
        self.information.draw()
        self.button.draw()
        pygame.display.flip()

    def event_button(self, event, i, j):
        if event.button == 1:
            if self.information.first_click:
                while self.display.data[i][j][0]:
                    self.display.reset_data()
                self.information.first_click = False
            if not self.display.mine_data[i][j]:
                self.open_block(i, j)
        elif event.button == 3:
            if self.display.data[i][j][1]:
                self.display.mine_data[i][j] = not self.display.mine_data[i][j]
                self.information.mine += -1 if self.display.mine_data[i][j] else 1
        elif event.button == 2:
            count = 0
            open_list = []
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if (0 <= i + m <= self.settings.board_size[1] - 1 and
                            0 <= j + n <= self.settings.board_size[0] - 1):
                        if self.display.mine_data[i + m][j + n]:
                            count += 1
                        else:
                            open_list.append([i + m, j + n])
            if self.display.data[i][j][0] == count:
                for open_block in open_list:
                    self.open_block(open_block[0], open_block[1])
        if self.information.check():
            self.button.game_over()

    def open_block(self, i, j):
        self.display.data[i][j][1] = False
        if not self.display.data[i][j][0]:
            self.display.continue_zero(i, j)
        elif self.display.data[i][j][0] == -1:
            self.button.game_over()
