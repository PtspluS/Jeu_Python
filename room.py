import pygame
from pygame.locals import *


class room:

    def __init__(self, tab_map, character_tab):
        self.tab_map = tab_map
        self.character_tab = character_tab
        self.map_pos = 10 * [0]
        for i in range(0, 10):
            self.map_pos[i] = (10 * [0])
        for j in character_tab:
            self.map_pos[j.x][j.y] = j
            print(j)

    def generate(self, window):  # fonction qui dessinala map
        """

        :param window: la feneter
        :return:
        """
        for i in range(0, len(self.tab_map)):
            for j in range(0, len(self.tab_map[i])):
                window.blit(self.tab_map[i][j].image, (self.tab_map[i][j].x * 64, self.tab_map[i][j].y * 64))

                if self.map_pos[i][j] != 0:
                    window.blit(self.map_pos[i][j].img, (self.map_pos[i][j].x * 64, self.map_pos[i][j].y * 64))
        pygame.display.flip()
