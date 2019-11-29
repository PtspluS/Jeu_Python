from copy import deepcopy

import pygame

from src import Pathfinder, Global
from src.Game_Object.Personnages import Boss
from src.Game_Object.spell import Kick


class Garde_de_la_porte(Boss.Boss):

    def __init__(self,img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl):
        self.ranges=2
        self.img=Global.guarde_de_la_porte
        self.kick=Kick.Kick()
        super().__init__(img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl, ranges=self.ranges)



    def play(self,room):
        pygame.time.delay(100)
        pygame.event.clear()
        self.range=1
        target = self.is_on_target(room)
        if target !=0:
            self.kick.cast(self,room,target)
        else :
            self.range = 2
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
