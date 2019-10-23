import Game
from pygame.locals import *


def menu_select(cursor):
    if cursor == 0:
        Game.game()
        return 1
    if cursor == 1:
        print("charge une partie")
        return 1
    if cursor == 2:
        return 0


def menu(pygame):
    continuer =1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                continuer = 0

            if event.type == KEYDOWN:
                if event.key == K_s or event.key == K_DOWN:
                    cursor = (cursor + 1) % 3
                    print(cursor)
                if event.key == K_w or event.key == K_UP:
                    cursor = (cursor - 1) % 3
                    print(cursor)
                if event.key == K_RETURN:
                    continuer=menu_select(cursor)
