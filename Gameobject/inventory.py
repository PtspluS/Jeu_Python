import pygame
from Gameobject import Item
from pygame.locals import *

width = 1500
height = 700


class inventory:

    def __init__(self, helmet=0, chest=0, pants=0, shoes=0, left_hand=0, right_hand=0):
        """

        :param helmet: un casque
        :param chest: une plaston
        :param pants: un pantalon
        :param shoes: une chaussures
        :param left_hand: une arme main droite
        :param right_hand: une arme main gauche
        """
        self.ring = 2 * [0]  # tableau des bijoux
        self.stuff = []
        for i in range(0, 10):  # tableau des items
            malist = []
            for j in range(0, 5):
                malist.append(0)
            self.stuff.append(malist)
        self.inventory_fond = pygame.image.load('sprite/inventory_fond.png')
        self.inventory_tile = pygame.image.load('sprite/inventory_tiles.png')
        self.inventory_press_tile = pygame.image.load('sprite/inventory_press_tiles.png')
        self.inventory_helmet = pygame.image.load('sprite/inventory_helmet.png')
        self.inventory_sword = pygame.image.load('sprite/inventory_sword.png')
        self.inventory_chest = pygame.image.load('sprite/inventory_chest.png')
        self.inventory_pants = pygame.image.load('sprite/inventory_pants.png')
        self.inventory_shoes = pygame.image.load('sprite/inventory_shoes.png')
        self.inventory_ring = pygame.image.load('sprite/inventory_ring.png')
        helmet = self.inventory_helmet
        left_hand = self.inventory_sword
        right_hand = self.inventory_sword
        chest = self.inventory_chest
        pants = self.inventory_pants
        shoes = self.inventory_shoes
        self.ring[0] = self.inventory_ring
        self.ring[1] = self.inventory_ring
        self.equipement = ["empty", left_hand, "empty", "empty"], [helmet, chest, pants, shoes], ["empty", right_hand,
                                                                                                  "empty", "empty"], [
                              "empty", self.ring[0], self.ring[1], "empty"]  # tableau d'equipement

    def anim_cursor(self, window, cursor_x, cursor_y, dir_x, dir_y, isequip):#animation du curseur d'inventaire
        """

        :param window: la fenetre
        :param cursor_x: posx du curseur
        :param cursor_y: posy u curseur
        :param dir_x: direction du curseur
        :param dir_y: direction du curseur
        :param isequip: est on dans l'equipement ou le stuff
        :return: cursor
        """
        if isequip:#si on est dans l'equipement

            if 0 <= cursor_x + dir_x < 4 and 0 <= cursor_y + dir_y < 4:#est on en dehors de l'inventaire
                if self.equipement[cursor_x + dir_x][cursor_y + dir_y] != "empty":# est on dans l'equipement valide
                    window.blit(self.inventory_tile, (230 + cursor_x * 70, 30 + cursor_y * 70))#affiche l'ancienne position du curseur
                    if type(self.equipement[cursor_x][cursor_y]) == Item:#si un item est equipé
                        window.blit(self.equipement[cursor_x][cursor_y].image,#on affiche l'item
                                    (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))
                    else:

                        window.blit(self.equipement[cursor_x][cursor_y],#sinon on affiche le logo
                                    (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))

                    cursor_x = cursor_x + dir_x#on change le curseur
                    cursor_y = cursor_y + dir_y
                    window.blit(self.inventory_press_tile, (230 + cursor_x * 70, 30 + cursor_y * 70))#affiche la case appuyer
                    if type(self.equipement[cursor_x][cursor_y]) == Item:#si un item est equipé
                        window.blit(self.equipement[cursor_x][cursor_y].image,#on affiche l'item
                                    (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))
                    else:
                        window.blit(self.equipement[cursor_x][cursor_y],#sinon on affiche le logo
                                    (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))
                    return cursor_x, cursor_y
            return cursor_x, cursor_y



        else:#si on est dans le stuff
            if 0 <= cursor_x + dir_x < 10 and 0 <= cursor_y + dir_y < 5:# on verifie que on est dans le stuff
                window.blit(self.inventory_tile, (650 + cursor_x * 64, 10 + cursor_y * 64))#on affiche l'ancienne case
                if self.stuff[cursor_x][cursor_y] != 0:#si il y a un item
                    window.bilt(self.stuff[cursor_x][cursor_y].image, (650 + cursor_x * 64, 10 + cursor_y * 64))#on affiche l'item
                cursor_x = cursor_x + dir_x#on change le curseur
                cursor_y = cursor_y + dir_y
                window.blit(self.inventory_press_tile, (650 + cursor_x * 64, 10 + cursor_y * 64))#on affiche la case appuyer
                if self.stuff[cursor_x][cursor_y] != 0:#si il y a un item
                    window.bilt(self.stuff[cursor_x][cursor_y].image, (650 + cursor_x * 64, 10 + cursor_y * 64))#on affiche l'item

                return cursor_x, cursor_y
            else:
                return cursor_x, cursor_y

    def use_inventory(self, window, room):
        """

        :param window: le fenetre
        :param room: la salle
        :return:
        """
        inventory_width = 1300
        inventory_height = 500

        window.blit(self.inventory_fond, (width / 2 - (inventory_width / 2), 0))
        for i in range(0, 10):
            for j in range(0, 5):
                window.blit(self.inventory_tile, (inventory_width / 2 + i * 64, 10 + j * 64))#affichage de l'inventaire
        window.blit(self.inventory_press_tile, (650, 10))
        window.blit(self.inventory_tile, (300, 30))
        window.blit(self.inventory_helmet, (300 + 16, 30 + 16))
        window.blit(self.inventory_tile, (300, 100))
        window.blit(self.inventory_chest, (300 + 16, 100 + 16))
        window.blit(self.inventory_tile, (300, 170))
        window.blit(self.inventory_pants, (300 + 16, 170 + 16))
        window.blit(self.inventory_tile, (300, 240))
        window.blit(self.inventory_shoes, (300 + 16, 240 + 16))
        window.blit(self.inventory_tile, (230, 100))
        window.blit(self.inventory_sword, (230 + 16, 100 + 16))
        window.blit(self.inventory_tile, (370, 100))
        window.blit(self.inventory_sword, (370 + 16, 100 + 16))
        window.blit(self.inventory_tile, (440, 100))
        window.blit(self.inventory_ring, (440 + 16, 100 + 16))
        window.blit(self.inventory_tile, (440, 170))
        window.blit(self.inventory_ring, (440 + 16, 170 + 16))
        cursor_x = 0
        cursor_y = 0
        isequip = False
        continuer = 1
        while continuer:#boucle de gestion de l'inventaire
            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_s or event.key == K_DOWN:#on detecte le entré clavier
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, 0, 1, isequip)
                    if event.key == K_w or event.key == K_UP:
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, 0, -1, isequip)
                    if event.key == K_a or event.key == K_LEFT:
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, -1, 0, isequip)
                    if event.key == K_d or event.key == K_RIGHT:
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, 1, 0, isequip)
                    if event.key == K_q:
                        print()
                    if event.key == K_e:
                        print()
                    if event.key == K_TAB:
                        if isequip:
                            isequip = False#on passe de l'inventaire au stuff
                            window.blit(self.inventory_tile, (230 + cursor_x * 70, 30 + cursor_y * 70))
                            if type(self.equipement[cursor_x][cursor_y]) == Item:
                                window.blit(self.equipement[cursor_x][cursor_y].image,
                                            (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))
                            else:
                                window.blit(self.equipement[cursor_x][cursor_y],
                                            (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))
                            cursor_x = 0
                            cursor_y = 0
                            window.blit(self.inventory_press_tile, (650 + cursor_x * 64, 10 + cursor_y * 64))
                        else:
                            isequip = True#on passe du stuff a l'inventaire
                            window.blit(self.inventory_tile, (650 + cursor_x * 64, 10 + cursor_y * 64))
                            cursor_x = 1
                            cursor_y = 1
                            window.blit(self.inventory_press_tile, (230 + cursor_x * 70, 30 + cursor_y * 70))
                            if type(self.equipement[cursor_x][cursor_y]) == Item:
                                window.blit(self.equipement[cursor_x][cursor_y].image,
                                            (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))
                            else:
                                window.blit(self.equipement[cursor_x][cursor_y],
                                            (230 + cursor_x * 70 + 16, 30 + 16 + cursor_y * 70))

                    if event.key == K_ESCAPE:
                        room.generate(window)# on reessine la map
                        continuer = 0
