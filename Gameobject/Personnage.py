import pygame
import Game
from Gameobject import inventory
from pygame.locals import *

class Personnage:

    max_hp = 100
    max_speed = 1

    def __init__(self, img, nom, desc, inventory, vie=100, PO=50, posX=0, posY=0, lvl = 1):
        self.img = img
        self.name = nom
        self.desc = desc
        self.hp = vie
        self.money = PO
        self.x = posX
        self.y = posY
        self.inventory = inventory
        self.lvl = lvl

    def heal(self, val):
        self.hp = self.hp + abs(val) % self.max_hp

    def move(self, window, map, map_pos, x, y):
        if Game.isinrange(x , y , 10, 10):
            if map[x][y].is_walkable and map_pos[x][y] == 0:
                window.blit(map[self.x][self.y].image, (self.x * 32, self.y * 32))
                map_pos[self.x][self.y] = 0
                self.x = x
                self.y = y
                (map_pos[self.x][self.y]) = self
                window.blit(self.img, (self.x * 32, self.y * 32))


    def anim_cursor(self, window,map,map_pos,cursor,red_cursor,dir_x,dir_y):
        if Game.isinrange(cursor.x + dir_x, cursor.y + dir_y, 10, 10):
            window.blit(cursor.image, (cursor.x * 32, cursor.y * 32))
            if map_pos[cursor.x][cursor.y] != 0:
                window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 32, cursor.y * 32))
            cursor = map[cursor.x + dir_x][cursor.y + dir_y]
            window.blit(red_cursor, (cursor.x * 32, cursor.y * 32))
            return cursor
        else:
            return cursor


    def attack(self, window, map, map_pos):
        red_cursor = pygame.image.load('sprite/cursor.png')
        red_cursor.set_alpha(100)

        continuer=1
        cursor=map[self.x][self.y]
        window.blit(red_cursor, (cursor.x * 32, cursor.y * 32))
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
                        cursor=self.anim_cursor(window, map, map_pos, cursor, red_cursor, 0, 1)

                    if event.key == K_w or event.key == K_UP:
                        cursor=self.anim_cursor(window, map, map_pos, cursor, red_cursor, 0, -1)

                    if event.key == K_a or event.key == K_LEFT:
                        cursor = self.anim_cursor(window,map,map_pos,cursor,red_cursor,-1,0)

                    if event.key == K_d or event.key == K_RIGHT:
                        cursor = self.anim_cursor(window,map,map_pos,cursor,red_cursor,1,0)

                    if event.key == K_RETURN:
                        window.blit(cursor.image, (cursor.x * 32, cursor.y * 32))
                        if map_pos[cursor.x][cursor.y] != 0:
                            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 32, cursor.y * 32))
                        continuer=0
                        if map_pos[cursor.x][cursor.y] != 0:
                            map_pos[cursor.x][cursor.y].hp = map_pos[cursor.x][cursor.y].hp-10
                            print(map_pos[cursor.x][cursor.y].hp)
