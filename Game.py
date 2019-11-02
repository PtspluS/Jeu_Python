import math

import pygame
from Gameobject import Personnage
from pygame.locals import *
import math


def isinrange(x, y, max_x, max_y):
    if(x >= max_x or x<0 or y>=max_y or y<0):
        return False
    else :
        return True


def anim_cursor(window, map, map_pos, cursor, red_cursor, dir_x, dir_y):
    if isinrange(cursor.x + dir_x,cursor.y + dir_y,10,10):
        window.blit(cursor.image, (cursor.x * 32, cursor.y * 32))
        if map_pos[cursor.x][cursor.y] != 0:
            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 32, cursor.y * 32))
        cursor = map[cursor.x + dir_x][cursor.y + dir_y]
        window.blit(red_cursor, (cursor.x * 32, cursor.y * 32))
        return cursor
    else:
        return cursor




def examine(window, map, map_pos,x,y):
    yellow_cursor = pygame.image.load('sprite/yellow_cursor.png')
    yellow_cursor.set_alpha(100)
    continuer = 1
    cursor = map[x][y]
    window.blit(yellow_cursor, (cursor.x * 32, cursor.y * 32))
    while continuer:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    window.blit(cursor.image, (cursor.x * 32, cursor.y * 32))
                    continuer = 0
                    if map_pos[cursor.x][cursor.y] != 0:
                        window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 32, cursor.y * 32))
                if event.key == K_s or event.key == K_DOWN:
                    cursor = anim_cursor(window, map, map_pos, cursor, yellow_cursor, 0, 1)

                if event.key == K_w or event.key == K_UP:
                    cursor = anim_cursor(window, map, map_pos, cursor, yellow_cursor, 0, -1)

                if event.key == K_a or event.key == K_LEFT:
                    cursor = anim_cursor(window, map, map_pos, cursor, yellow_cursor, -1, 0)

                if event.key == K_d or event.key == K_RIGHT:
                    cursor = anim_cursor(window, map, map_pos, cursor, yellow_cursor, 1, 0)

                if event.key == K_RETURN:
                    window.blit(cursor.image, (cursor.x * 32, cursor.y * 32))
                    if map_pos[cursor.x][cursor.y] != 0:
                        window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 32, cursor.y * 32))
                    continuer = 0
                    if map_pos[cursor.x][cursor.y] != 0:
                        print(map_pos[cursor.x][cursor.y].desc)



def game(window, tab_map, map_pos, character_tab):
    turn = 0
    bob = character_tab[0]
    window.blit(bob.img, (0, 0))
    window.blit(character_tab[1].img, (character_tab[1].x*32, character_tab[1].y*32))
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
                    bob.attack(window,tab_map, map_pos)
                if event.key == K_e:
                    examine(window, tab_map, map_pos,bob.x,bob.y)
                if event.key == K_i:
                    print("i")
                if event.key == K_r:
                    print("r")
