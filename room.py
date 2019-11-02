import pygame
from pygame.locals import *

class Room:

    def __init__(self, tab_map):
        self.tab_map = tab_map
        tab_pos = len(tab_map) * [len(tab_map)*[None]]


    def generate(self, window):
        for i in range(0, len(self.tab_map)):
            for j in range(0, len(self.tab_map[i])):
                window.blit(self.tab_map[i][j].image, (self.tab_map[i][j].x*32, self.tab_map[i][j].y*32))
        pygame.display.flip()
