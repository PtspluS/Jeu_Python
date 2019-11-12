import pygame
from Gameobject import Tete
from Gameobject import Arme
from Gameobject import Bijou
from Gameobject import Corps
from Gameobject import Jambes
from Gameobject import Pied
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
        self.start_stuff_x = 650
        self.start_stuff_y = 10
        self.start_equipement_x = 230
        self.start_equipement_y = 30
        self.space_equipement = 70
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
        self.empty_equipement = ["empty", left_hand, "empty", "empty"], [helmet, chest, pants, shoes], ["empty",
                                                                                                        right_hand,
                                                                                                        "empty",
                                                                                                        "empty"], [
                                    "empty", self.ring[0], self.ring[1], "empty"]  # tableau d'equipement vide
        self.equipement = ["empty", left_hand, "empty", "empty"], [helmet, chest, pants, shoes], ["empty", right_hand,
                                                                                                  "empty", "empty"], [
                              "empty", self.ring[0], self.ring[1], "empty"]  # tableau d'equipement

    def pick(self, item):
        """

        :param item: l'itemramassé
        :return:
        """
        for slot in self.stuff:
            for i in range(0, len(slot)):  # si il reste de la place
                if slot[i] == 0:
                    slot[i] = item
                    return True
            return False

    # fonction qui permet d'equipé ou desequipé un object
    def equipe(self, window, cursor_x, cursor_y, isequip):
        """

        :param cursor_x: pos x u curseur
        :param cursor_y: pos y du curseur
        :param isequip: si on est dans l'equipement
        :return:
        """
        if isequip:  # si on est dans l'equipement
            if isinstance(self.equipement[cursor_x][cursor_y], Item.Item):
                if self.pick(self.equipement[cursor_x][cursor_y]):  # si il reste de la place dans le stuff
                    self.equipement[cursor_x][cursor_y] = self.empty_equipement[cursor_x][
                        cursor_y]  # on deplace l'object
                    print("item remove")
                else:
                    print("your stuff is full")

        else:  # si on est pas dans l'equipement
            window.blit(self.inventory_press_tile,
                        (self.start_stuff_x + cursor_x * 64,
                         self.start_stuff_y + cursor_y * 64))
            if isinstance(self.stuff[cursor_x][cursor_y], Tete.Tete):  # on verfifie quel type,d'item est selectionné
                window.blit(self.inventory_tile,
                            (self.start_equipement_x + 1 * 70,
                             self.start_equipement_y + 0 * 70))
                if self.equipement[1][0] == self.inventory_helmet:  # si il n'y a rien on equipe
                    self.equipement[1][0] = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = 0
                else:  # si il y a quelque choses on echange
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][0]
                    self.equipement[1][0] = tmp
                window.blit(self.equipement[1][0].image,  # on affiche l'item
                            (self.start_equipement_x + 1 * 70 + 16,
                             self.start_equipement_y + 16 + 0 * 70))

            if isinstance(self.stuff[cursor_x][cursor_y], Corps.Corps):
                window.blit(self.inventory_tile,
                            (self.start_equipement_x + 1 * 70,
                             self.start_equipement_y + 1 * 70))
                if self.equipement[1][1] == self.inventory_chest:
                    self.equipement[1][1] = self.stuff[cursor_x][cursor_y]
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][1]
                    self.equipement[1][1] = tmp
                window.blit(self.equipement[1][1].image,  # on affiche l'item
                            (self.start_equipement_x + 1 * 70 + 16,
                             self.start_equipement_y + 16 + 0 * 70))

            if isinstance(self.stuff[cursor_x][cursor_y], Jambes.Jambe):
                window.blit(self.inventory_tile,
                            (self.start_equipement_x + 1 * 70,
                             self.start_equipement_y + 2 * 70))
                if self.equipement[1][2] == self.inventory_pants:
                    self.equipement[1][2] = self.stuff[cursor_x][cursor_y]
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][2]
                    self.equipement[1][2] = tmp
                window.blit(self.equipement[1][2].image,  # on affiche l'item
                            (self.start_equipement_x + 1 * 70 + 16,
                             self.start_equipement_y + 16 + 2 * 70))

            if isinstance(self.stuff[cursor_x][cursor_y], Pied.Pied):
                window.blit(self.inventory_tile,
                            (self.start_equipement_x + 1 * 70,
                             self.start_equipement_y + 3 * 70))
                if self.equipement[1][3] == self.inventory_shoes:
                    self.equipement[1][3] = self.stuff[cursor_x][cursor_y]
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][3]
                    self.equipement[1][3] = tmp
                window.blit(self.equipement[1][3].image,  # on affiche l'item
                            (self.start_equipement_x + 1 * 70 + 16,
                             self.start_equipement_y + 16 + 2 * 70))

            if isinstance(self.stuff[cursor_x][cursor_y], Bijou.Bijou):

                if self.equipement[3][1] == self.inventory_ring:
                    self.equipement[3][1] = self.stuff[cursor_x][cursor_y]
                    window.blit(self.inventory_tile,
                                (self.start_equipement_x + 3 * 70,
                                 self.start_equipement_y + 1 * 70))
                    window.blit(self.equipement[3][1].image,  # on affiche l'item
                                (self.start_equipement_x + 3 * 70 + 16,
                                 self.start_equipement_y + 16 + 1 * 70))
                elif self.equipement[3][2] == self.inventory_ring:
                    self.equipement[3][2] = self.stuff[cursor_x][cursor_y]
                    window.blit(self.inventory_tile,
                                (self.start_equipement_x + 3 * 70,
                                 self.start_equipement_y + 2 * 70))
                    window.blit(self.equipement[3][2].image,  # on affiche l'item
                                (self.start_equipement_x + 3 * 70 + 16,
                                 self.start_equipement_y + 16 + 2 * 70))
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[3][1]
                    window.blit(self.inventory_tile,
                                (self.start_equipement_x + 3 * 70,
                                 self.start_equipement_y + 1 * 70))
                    self.equipement[3][1] = tmp
                    window.blit(self.equipement[3][1].image,  # on affiche l'item
                                (self.start_equipement_x + 3 * 70 + 16,
                                 self.start_equipement_y + 16 + 1 * 70))

            if isinstance(self.stuff[cursor_x][cursor_y], Arme.Arme):

                if self.equipement[0][1] == self.inventory_sword:
                    self.equipement[0][1] = self.stuff[cursor_x][cursor_y]
                    window.blit(self.inventory_tile,
                                (self.start_equipement_x + 0 * 70,
                                 self.start_equipement_y + 1 * 70))
                    window.blit(self.equipement[0][1].image,  # on affiche l'item
                                (self.start_equipement_x + 0 * 70 + 16,
                                 self.start_equipement_y + 16 + 1 * 70))
                elif self.equipement[2][1] == self.inventory_sword:
                    self.equipement[2][1] = self.stuff[cursor_x][cursor_y]
                    window.blit(self.inventory_tile,
                                (self.start_equipement_x + 2 * 70,
                                 self.start_equipement_y + 1 * 70))
                    window.blit(self.equipement[2][1].image,  # on affiche l'item
                                (self.start_equipement_x + 2 * 70 + 16,
                                 self.start_equipement_y + 16 + 1 * 70))
                else:
                    window.blit(self.inventory_tile,
                                (self.start_equipement_x + 0 * 70,
                                 self.start_equipement_y + 1 * 70))
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[0][1]
                    self.equipement[0][1] = tmp
                    window.blit(self.equipement[0][1].image,  # on affiche l'item
                                (self.start_equipement_x + 0 * 70 + 16,
                                 self.start_equipement_y + 16 + 1 * 70))
            if self.stuff[cursor_x][cursor_y] != 0:  # si il y a un item
                window.bilt(self.stuff[cursor_x][cursor_y].image,
                            (self.start_stuff_x + cursor_x * 64,
                             self.start_stuff_y + cursor_y * 64))

    def anim_cursor(self, window, cursor_x, cursor_y, dir_x, dir_y, isequip):  # animation du curseur d'inventaire
        """
        :param window: la fenetre
        :param cursor_x: posx du curseur
        :param cursor_y: posy u curseur
        :param dir_x: direction du curseur
        :param dir_y: direction du curseur
        :param isequip: est on dans l'equipement ou le stuff
        :return: cursor
        """
        if isequip:  # si on est dans l'equipement

            if 0 <= cursor_x + dir_x < 4 and 0 <= cursor_y + dir_y < 4:  # est on en dehors de l'inventaire
                if self.equipement[cursor_x + dir_x][cursor_y + dir_y] != "empty":  # est on dans l'equipement valide
                    window.blit(self.inventory_tile,
                                (self.start_equipement_x + cursor_x * 70,
                                 self.start_equipement_y + cursor_y * 70))  # affiche l'ancienne position du curseur
                    if type(self.equipement[cursor_x][cursor_y]) == Item:  # si un item est equipé
                        window.blit(self.equipement[cursor_x][cursor_y].image,  # on affiche l'item
                                    (self.start_equipement_x + cursor_x * 70 + 16,
                                     self.start_equipement_y + 16 + cursor_y * 70))
                    else:

                        window.blit(self.equipement[cursor_x][cursor_y],  # sinon on affiche le logo
                                    (self.start_equipement_x + cursor_x * 70 + 16,
                                     self.start_equipement_y + 16 + cursor_y * 70))

                    cursor_x = cursor_x + dir_x  # on change le curseur
                    cursor_y = cursor_y + dir_y
                    window.blit(self.inventory_press_tile,
                                (self.start_equipement_x + cursor_x * 70,
                                 self.start_equipement_y + cursor_y * 70))  # affiche la case appuyer
                    if type(self.equipement[cursor_x][cursor_y]) == Item:  # si un item est equipé
                        window.blit(self.equipement[cursor_x][cursor_y].image,  # on affiche l'item
                                    (self.start_equipement_x + cursor_x * 70 + 16,
                                     self.start_equipement_y + 16 + cursor_y * 70))
                    else:
                        window.blit(self.equipement[cursor_x][cursor_y],  # sinon on affiche le logo
                                    (self.start_equipement_x + cursor_x * 70 + 16,
                                     self.start_equipement_y + 16 + cursor_y * 70))
                    return cursor_x, cursor_y
            return cursor_x, cursor_y

        else:  # si on est dans le stuff
            if 0 <= cursor_x + dir_x < 10 and 0 <= cursor_y + dir_y < 5:  # on verifie que on est dans le stuff
                window.blit(self.inventory_tile,
                            (self.start_stuff_x + cursor_x * 64,
                             self.start_stuff_y + cursor_y * 64))  # on affiche l'ancienne case
                if self.stuff[cursor_x][cursor_y] != 0:  # si il y a un item
                    window.bilt(self.stuff[cursor_x][cursor_y].image,
                                (self.start_stuff_x + cursor_x * 64,
                                 self.start_stuff_y + cursor_y * 64))  # on affiche l'item
                cursor_x = cursor_x + dir_x  # on change le curseur
                cursor_y = cursor_y + dir_y
                window.blit(self.inventory_press_tile,
                            (self.start_stuff_x + cursor_x * 64,
                             self.start_stuff_y + cursor_y * 64))  # on affiche la case appuyer
                if self.stuff[cursor_x][cursor_y] != 0:  # si il y a un item
                    window.bilt(self.stuff[cursor_x][cursor_y].image,
                                (self.start_stuff_x + cursor_x * 64,
                                 self.start_stuff_y + cursor_y * 64))  # on affiche l'item

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
                window.blit(self.inventory_tile,
                            (inventory_width / 2 + i * 64, self.start_stuff_y + j * 64))  # affichage de l'inventaire
        window.blit(self.inventory_press_tile, (self.start_stuff_x, self.start_stuff_y))
        window.blit(self.inventory_tile, (self.start_equipement_x + self.space_equipement, self.start_equipement_y))
        window.blit(self.equipement[1][0],
                    (self.start_equipement_x + self.space_equipement + 16, self.start_equipement_y + 16))
        window.blit(self.inventory_tile,
                    (self.start_equipement_x + self.space_equipement, self.start_equipement_y + self.space_equipement))
        window.blit(self.equipement[1][1], (
            self.start_equipement_x + self.space_equipement + 16, self.start_equipement_y + self.space_equipement + 16))
        window.blit(self.inventory_tile, (
            self.start_equipement_x + self.space_equipement, self.start_equipement_y + 2 * self.space_equipement))
        window.blit(self.equipement[1][2], (
            self.start_equipement_x + self.space_equipement + 16,
            self.start_equipement_y + 2 * self.space_equipement + 16))
        window.blit(self.inventory_tile, (
            self.start_equipement_x + self.space_equipement, self.start_equipement_y + 3 * self.space_equipement))
        window.blit(self.equipement[1][3], (
            self.start_equipement_x + self.space_equipement + 16,
            self.start_equipement_y + 3 * self.space_equipement + 16))
        window.blit(self.inventory_tile, (self.start_equipement_x, self.start_equipement_y + self.space_equipement))
        window.blit(self.equipement[0][1],
                    (self.start_equipement_x + 16, self.start_equipement_y + self.space_equipement + 16))
        window.blit(self.inventory_tile, (
            self.start_equipement_x + 2 * self.space_equipement, self.start_equipement_y + self.space_equipement))
        window.blit(self.equipement[2][1], (
            self.start_equipement_x + 2 * self.space_equipement + 16,
            self.start_equipement_y + self.space_equipement + 16))
        window.blit(self.inventory_tile, (
            self.start_equipement_x + 3 * self.space_equipement, self.start_equipement_y + self.space_equipement))
        window.blit(self.equipement[3][1], (
            self.start_equipement_x + 3 * self.space_equipement + 16,
            self.start_equipement_y + self.space_equipement + 16))
        window.blit(self.inventory_tile, (
            self.start_equipement_x + 3 * self.space_equipement, self.start_equipement_y + 2 * self.space_equipement))
        window.blit(self.equipement[3][2], (self.start_equipement_x + 3 * self.space_equipement + 16,
                                            self.start_equipement_y + 2 * self.space_equipement + 16))
        cursor_x = 0
        cursor_y = 0
        isequip = False
        continuer = 1
        while continuer:  # boucle de gestion de l'inventaire
            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_s or event.key == K_DOWN:  # on detecte le entré clavier
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, 0, 1, isequip)
                    if event.key == K_w or event.key == K_UP:
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, 0, -1, isequip)
                    if event.key == K_a or event.key == K_LEFT:
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, -1, 0, isequip)
                    if event.key == K_d or event.key == K_RIGHT:
                        cursor_x, cursor_y = self.anim_cursor(window, cursor_x, cursor_y, 1, 0, isequip)
                    if event.key == K_e:
                        self.equipe(window, cursor_x, cursor_y, isequip)
                    if event.key == K_r:
                        print("use")
                    if event.key == K_t:
                        print("lancer")
                    if event.key == K_TAB:
                        if isequip:
                            isequip = False  # on passe de l'inventaire au stuff
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
                            isequip = True  # on passe du stuff a l'inventaire
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
                        room.generate(window)  # on reessine la map
                        continuer = 0
