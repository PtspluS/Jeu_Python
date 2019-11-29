from copy import deepcopy

import inventory as inventory
import pygame

from src import Pathfinder, Global
from src.Game_Object.Personnages import Boss
from src.Game_Object.spell import Kick
from src.inventory import inventory





class Garde_de_la_porte(Boss.Boss):

    def __init__(self, vie = 500, PO = 1000, posX = 2, posY = 1, attaque = 25, lvl = 10):
        self.ranges=2
        self.img=Global.guarde_de_la_porte
        self.kick=Kick.Kick()

        # definition du perso
        nom = "Guarde de la porte"
        desc = "Il ne compte quand même que pour un !"
        inv = inventory()

        super().__init__(self.img, nom, desc, inv, vie, PO, posX, posY, attaque, lvl, ranges=self.ranges)



    def play(self,room):
        pygame.time.delay(100)
        pygame.event.clear()
        self.ranges=1
        target = self.is_on_target(room)
        if target !=0:
            self.kick.cast(self,room,room.tab_map[target.x][target.y])
        else :
            self.ranges = 2
            target = self.is_on_target(room)
            if target == 0:
                my_matrix = deepcopy(room.brute_map)
                for i in range(0, len(room.map_pos)):
                    for j in range(0, len(room.map_pos[i])):
                        if room.map_pos[i][j] != 0:
                            my_matrix[i][j] = 1
                my_matrix[room.char_tab[0].x][room.char_tab[0].y] = 0
                my_matrix[self.x][self.y] = 0

                path = Pathfinder.astar(my_matrix, (self.x, self.y), (room.char_tab[0].x, room.char_tab[0].y))
                if path:
                    self.move(room.tab_map, room.map_pos, path[1][0], path[1][1])
                else:
                    self.PA = 0

            else:
                target.hp = target.hp - self.attaque
                self.PA -= 1
