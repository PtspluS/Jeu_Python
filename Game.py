import pygame
from Gameobject import Personnage
from pygame.locals import *
turn=0



def game(window, tab_map, map_pos, character_tab):
    bob=character_tab[0]
    window.blit(bob.img, (0, 0))


    continuer=1
    while continuer:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_s or event.key == K_DOWN:
                    bob.move(window, tab_map, map_pos, bob.x, bob.y+1)
                if event.key == K_w or event.key == K_UP:
                    bob.move(window,tab_map, map_pos, bob.x, bob.y - 1)
                if event.key == K_a or event.key == K_LEFT:
                    bob.move(window,tab_map, map_pos, bob.x-1, bob.y )
                if event.key == K_d or event.key == K_RIGHT:
                    bob.move(window,tab_map, map_pos, bob.x+1, bob.y)
                if event.key == K_q:
                    print("q")
                if event.key == K_e:
                    print("e")
                if event.key == K_i:
                    print("i")
                if event.key == K_r:
                    print("r")
