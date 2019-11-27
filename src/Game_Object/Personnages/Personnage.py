import pygame

from src import Global

from pygame.locals import *


class Personnage:
    max_hp = 100
    max_speed = 1

    def __init__(self, img, nom, desc, inventory, vie=100, PO=5000, posX=0, posY=0, lvl=1,PA=6,PA_max=6):
        self.img = img
        self.name = nom
        self.desc = desc
        self.hp = vie
        self.money = PO
        self.x = posX
        self.y = posY
        self.inventory = inventory
        self.lvl = lvl
        self.PA_max = PA_max
        self.PA=PA
        self.attaque = 0

    def heal(self, val):
        self.hp = self.hp + abs(val) % self.max_hp

    def move(self, tab_map, map_pos, x, y):
        """

        :param window: la fenetre
        :param tab_map: la carte
        :param map_pos: la postion des joueurs sur la cartes
        :param x: case x ou on veut se deplacer
        :param y: case y ou on veut se deplacer
        :return:
        """
        window = Global.window
        if Global.isinrange(x, y, 17, 11):  # si la case est dans le tableau
            if tab_map[x][y].is_walkable and map_pos[x][y] == 0:  # la case est walkable il n y a peronnes sur la carte
                window.blit(tab_map[self.x][self.y].image, (self.x * 64, self.y * 64))  # dessine la
                map_pos[self.x][self.y] = 0
                self.x = x
                self.y = y
                (map_pos[self.x][self.y]) = self
                window.blit(self.img, (self.x * 64, self.y * 64))
                self.PA = self.PA -1
                Global.ui.print_PA(self)
                pygame.display.flip()


    def description(self):
        txt = str(self.name)+''+str(self.desc)+' ATK:'+str(self.attaque)+' HP:'+str(self.hp)+'/'+str(self.max_hp)\
            +' PO: '+str(self.money)+'PA: '+str(self.PA_max)

        return txt


