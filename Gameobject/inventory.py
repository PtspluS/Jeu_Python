from math import floor

import pygame

from pygame.locals import *
width = 1500
height = 700
class inventory:


    def __init__(self,helmet=0, chest=0, pants=0, shoes=0, left_hand=0, right_hand=0):
        self.ring = 3*[0]
        self.stuff=[]
        for i in range(0, 10):
            malist = []
            for j in range(0, 5):
                malist.append(0)
            self.stuff.append(malist)

        self.equipement = [[0],[0],[helmet],[0],[0]], [[0],[left_hand],[chest],[right_hand],[self.ring[0]]],[[0],[0],[pants],[0],[self.ring[1]]],[[0],[0],[shoes],[0],[0]]


    def anim_cursor(self,window, cursor_x,cursor_y, dir_x, dir_y,isequip):
        if isequip:
            if self.equipement[cursor_x+dir_x][cursor_y+dir_y] != 0:
                window.blit(self.inventory_tile, (300 + cursor_x * 32, 30 + cursor_y * 32))
                if self.equipement[cursor_x+dir_x][cursor_y+dir_y] != 0:
                    window.bilt(self.equipement[cursor_x][cursor_y].image, (300 + cursor_x * 32, 10 + cursor_y * 32))
                cursor_x=cursor_x+dir_x
                cursor_y=cursor_y+dir_y
                window.blit(self.inventory_press_tile, (300 + cursor_x * 32, 10 + cursor_y * 32))
                if self.stuff[cursor_x][cursor_y] != 0:
                    window.bilt(self.stuff[cursor_x][cursor_y].image, (300 + cursor_x * 32, 10 + cursor_y * 32))



        else:
            if 0 <= cursor_x + dir_x < 10 and 0 <= cursor_y + dir_y < 5:
                window.blit(self.inventory_tile, (650 + cursor_x * 32, 10 + cursor_y * 32))
                if self.stuff[cursor_x][cursor_y] != 0:
                    window.bilt(self.stuff[cursor_x][cursor_y].image, (650 + cursor_x * 32, 10 + cursor_y  * 32))
                cursor_x = cursor_x + dir_x
                cursor_y = cursor_y + dir_y
                window.blit(self.inventory_press_tile, (650 + cursor_x * 32, 10 + cursor_y * 32))
                if self.stuff[cursor_x][cursor_y] != 0:
                    window.bilt(self.stuff[cursor_x][cursor_y].image, (650 + cursor_x * 32, 10 + cursor_y * 32))

                return cursor_x,cursor_y
            else:
                return cursor_x,cursor_y






    def use_inventory(self,window, room):
        inventory_width = 1300
        inventory_height = 500

        window.blit(self.inventory_fond, (width / 2 - (inventory_width / 2), 0))
        for i in range(0, 10):
            for j in range(0, 5):
                window.blit(self.inventory_tile, (inventory_width / 2 + i * 32, 10+j*32))

        window.blit(self.inventory_tile, (300, 30))
        window.blit(self.inventory_helmet, (300 + 8, 30 + 8))
        window.blit(self.inventory_tile, (300, 70))
        window.blit(self.inventory_chest, (300 + 8, 70 + 8))
        window.blit(self.inventory_tile, (300, 110))
        window.blit(self.inventory_pants, (300 + 8, 110 + 8))
        window.blit(self.inventory_tile, (300, 150))
        window.blit(self.inventory_shoes, (300 + 8, 150 + 8))
        window.blit(self.inventory_tile, (260, 70))
        window.blit(self.inventory_sword, (260, 70))
        window.blit(self.inventory_tile, (340, 70))
        window.blit(self.inventory_sword, (340, 70))
        window.blit(self.inventory_tile, (380, 70))
        window.blit(self.inventory_ring, (380 + 8, 70 + 8))
        window.blit(self.inventory_tile, (380, 110))
        window.blit(self.inventory_ring, (380 + 8, 110 + 8))
        cursor_x=0
        cursor_y=0
        isequip=False
        continuer = 1
        while continuer:
            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_s or event.key == K_DOWN:
                        cursor_x,cursor_y=self.anim_cursor(window, cursor_x,cursor_y, 0,1,isequip)
                    if event.key == K_w or event.key == K_UP:
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x,cursor_y, 0, -1,isequip)
                    if event.key == K_a or event.key == K_LEFT:
                        cursor_x,cursor_y = self.anim_cursor(window, cursor_x,cursor_y, -1, 0,isequip)
                    if event.key == K_d or event.key == K_RIGHT:
                        cursor_x,cursor_y=self.anim_cursor(window, cursor_x,cursor_y, 1,0,isequip)
                    if event.key == K_q:
                        print()
                    if event.key == K_e:
                        print()
                    if event.key == K_TAB:
                        if isequip:
                            isequip=False
                            cursor_x = 0
                            cursor_y = 0
                        else :
                            isequip=True
                            cursor_x = 3
                            cursor_y = 0

                    if event.key == K_ESCAPE:
                        room.generate(window)
                        continuer = 0



