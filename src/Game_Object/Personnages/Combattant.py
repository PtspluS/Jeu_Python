import time
from copy import deepcopy

import pygame

from src.Game_Object.Personnages import PNJ, Cadavre
from src import Global
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np
from src.Game_Object.Personnages import Player
from src import Pathfinder


class Combattant(PNJ.PNJ):

    def __init__(self, img, nom, desc,inventory, vie=100, PO=50, posX=0, posY=0,attaque=0,lvl=1):
        super(Combattant, self).__init__(img, nom = nom, desc = desc,inventory=inventory, vie= vie, PO= PO, posX= posX, posY = posY, lvl=lvl, attaquable=True)
        self.attaque = attaque
        self.item = inventory.stuff

    def heal(self, val):
        self.hp = (self.hp + abs(val)) % self.max_hp

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
                self.move(room.tab_map, room.map_pos, path[1][0], path[1][1])
            else : self.PA=0

        else:
            target.hp=target.hp-self.attaque
            self.PA-=1






    def die(self):
        img_cadavre = Global.grave
        return Cadavre.Cadavre(img_cadavre, nom = self.name,desc='' ,inventory=self.inventory, lvl = self.lvl, PO= self.money, posX= self.x, posY=self.y)