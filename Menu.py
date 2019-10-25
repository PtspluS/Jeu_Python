import pygame
from pygame.locals import *


class object_image:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


def menu(width, height, menu_window):

    sprit_dico = {}
    fond = pygame.image.load('sprite/Fond.png')
    new_game_button_picture = pygame.image.load('sprite/New_game.png')
    new_game_button = object_image(width / 2 - 327, 100,new_game_button_picture)
    sprit_dico[0] = new_game_button

    continue_button_picture = pygame.image.load('sprite/Continue.png')
    continue_button = object_image(width / 2 - 327, 300, continue_button_picture)
    sprit_dico[1] = continue_button

    exit_button_picture = pygame.image.load('sprite/Exit.png')
    exit_button = object_image(width / 2 - 327, 500,  exit_button_picture)
    sprit_dico[2] = exit_button

    fleche_picture = pygame.image.load('sprite/Fleche.png').convert_alpha()
    fleche = object_image(width/3, height/2-200, fleche_picture)
    sprit_dico["fleche"] = fleche
    fond = pygame.transform.scale(fond, (width, height))
    menu_window.blit(fond, (0, 0))
    menu_window.blit(new_game_button.image, (new_game_button.x, new_game_button.y))
    menu_window.blit(continue_button.image, (continue_button.x, continue_button.y))
    menu_window.blit(exit_button.image, (exit_button.x, exit_button.y))
    menu_window.blit(sprit_dico["fleche"].image, (sprit_dico["fleche"].x, sprit_dico["fleche"].y))

    pygame.display.flip()
    cursor = 0
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            pygame.display.flip()

            if event.type == QUIT:
                continuer = 0

            if event.type == KEYDOWN:

                if event.key == K_s or event.key == K_DOWN:
                    menu_window.blit(sprit_dico[cursor].image, (sprit_dico[cursor].x, sprit_dico[cursor].y))
                    cursor = (cursor + 1) % 3
                    print(cursor)
                if event.key == K_w or event.key == K_UP:
                    menu_window.blit(sprit_dico[cursor].image, (sprit_dico[cursor].x, sprit_dico[cursor].y))
                    cursor = (cursor - 1) % 3
                    print(cursor)
                if event.key == K_RETURN:
                    return cursor
                menu_window.blit(sprit_dico["fleche"].image, (sprit_dico["fleche"].x, sprit_dico["fleche"].y+cursor*200))

