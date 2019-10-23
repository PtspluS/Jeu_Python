import pygame
from pygame.locals import *


def menu():
    cursor=1
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:

                continuer = 0

            if event.type == KEYDOWN:
                if event.key == K_s or event.key == K_DOWN:
                    cursor = (cursor + 1) % 3
                    print(cursor)
                if event.key == K_w or event.key == K_UP:
                    cursor = (cursor - 1) % 3
                    print(cursor)
                if event.key == K_RETURN:
                    return cursor


pygame.display.quit()