from copy import deepcopy

import pygame

from src import Global, Pathfinder
from src.Game_Object.Personnages import Combattant, Player


class Bourgeois(Combattant.Combattant):

    def __init__(self, img, nom, desc = "",inventory=[], vie=100, PO=50, posX=0, posY=0, attaque=0, lvl=1, courage=1,
                 PA=1):
        self.ranges = 1
        super().__init__(img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl,ranges=self.ranges)
        self.PA = PA
        self.PA_max = PA



    def play(self,room):
        pygame.time.delay(100)
        pygame.event.clear()
        target=0
        if Global.isinrange(self.x+1,self.y,len(room.map_pos),len(room.map_pos[0])):
            if isinstance(room.map_pos[self.x+1][self.y],Player.Player):
                target=room.map_pos[self.x+1][self.y]
        if Global.isinrange(self.x-1,self.y,len(room.map_pos),len(room.map_pos[0])):
            if isinstance(room.map_pos[self.x-1][self.y],Player.Player):
                target=room.map_pos[self.x-1][self.y]
        if Global.isinrange(self.x,self.y+1,len(room.map_pos),len(room.map_pos[0])):
            if isinstance(room.map_pos[self.x][self.y+1],Player.Player):
                target=room.map_pos[self.x][self.y+1]
        if Global.isinrange(self.x,self.y-1,len(room.map_pos),len(room.map_pos[0])):
            if isinstance(room.map_pos[self.x][self.y-1],Player.Player):
                target=room.map_pos[self.x][self.y-1]
        if target ==0:

            my_matrix = deepcopy(room.brute_map)
            for i in range(0, len(room.map_pos)):
                for j in range(0, len(room.map_pos[i])):
                    if room.map_pos[i][j] != 0:
                        my_matrix[i][j] = 1
            my_matrix[room.char_tab[0].x][room.char_tab[0].y]=0
            my_matrix[self.x][self.y] = 0

            path=Pathfinder.astar(my_matrix,(self.x,self.y),(room.char_tab[0].x, room.char_tab[0].y))
            if path:
                dir_x=self.x-path[1][0]
                dir_y=self.y-path[1][1]
                if room.tab_map[self.x+dir_x][self.y+dir_y].is_walkable and room.map_pos[self.x+dir_x][self.y+dir_y]==0:
                    self.move(room.tab_map, room.map_pos, self.x+dir_x, self.y+dir_y)
                else :self.move(room.tab_map, room.map_pos, path[1][0], path[1][1])
            else : self.PA=0

        else:
            target.hp=target.hp-self.attaque
            self.PA-=1
