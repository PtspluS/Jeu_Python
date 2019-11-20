import pygame

from src import Global

from pygame.locals import *


class Personnage:
    max_hp = 100
    max_speed = 1

    def __init__(self, img, nom, desc, inventory, vie=100, PO=5000, posX=0, posY=0, lvl=1,PA=6):
        self.img = img
        self.name = nom
        self.desc = desc
        self.hp = vie
        self.money = PO
        self.x = posX
        self.y = posY
        self.inventory = inventory
        self.lvl = lvl
        self.PA=PA

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

    def anim_cursor(self, tab_map, map_pos, cursor, red_cursor, dir_x, dir_y):
        """

        :param window: fenetre
        :param tab_map: la carte
        :param map_pos: position des joueur sur la carte
        :param cursor: cursor
        :param red_cursor: image rouge
        :param dir_x: direction x
        :param dir_y: direction y
        :return:
        """

        window = Global.window
        if Global.isinrange(cursor.x + dir_x, cursor.y + dir_y, 17, 11):  # deplacement et affichage du curseur
            window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
            if map_pos[cursor.x][cursor.y] != 0:
                window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
            cursor = tab_map[cursor.x + dir_x][cursor.y + dir_y]
            window.blit(red_cursor, (cursor.x * 64, cursor.y * 64))
            return cursor
        else:
            return cursor

    def attack(self, tab_map, map_pos):  # fonction d'attaque
        """

        :param window: fenetre
        :param tab_map: la carte
        :param map_pos: la position des joueur sur la carte
        :return:
        """
        window = Global.window
        red_cursor = Global.red_cursor

        continuer = 1
        cursor = tab_map[self.x][self.y]
        window.blit(red_cursor, (cursor.x * 64, cursor.y * 64))
        while continuer:  # boucle qui gere le curseur
            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == QUIT:
                    continuer = 0

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                        continuer = 0
                        if map_pos[cursor.x][cursor.y] != 0:
                            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                    if event.key == K_s or event.key == K_DOWN:  # deplacement du curseur
                        cursor = self.anim_cursor(tab_map, map_pos, cursor, red_cursor, 0, 1)

                    if event.key == K_w or event.key == K_UP:
                        cursor = self.anim_cursor(tab_map, map_pos, cursor, red_cursor, 0, -1)

                    if event.key == K_a or event.key == K_LEFT:
                        cursor = self.anim_cursor(tab_map, map_pos, cursor, red_cursor, -1, 0)

                    if event.key == K_d or event.key == K_RIGHT:
                        cursor = self.anim_cursor(tab_map, map_pos, cursor, red_cursor, 1, 0)

                    if event.key == K_RETURN:
                        window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                        if map_pos[cursor.x][cursor.y] != 0:
                            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                        continuer = 0
                        if map_pos[cursor.x][cursor.y] != 0:
                            map_pos[cursor.x][cursor.y].hp = map_pos[cursor.x][cursor.y].hp - 10
                            print(map_pos[cursor.x][cursor.y].hp)


