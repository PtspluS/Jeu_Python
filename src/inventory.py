import pygame
from src.Game_Object.Objets import Tete
from src.Game_Object.Objets import Arme
from src.Game_Object.Objets import Bijou
from src.Game_Object.Objets import Corps
from src.Game_Object.Objets import Jambes
from src.Game_Object.Objets import Pied
from src.Game_Object.Objets import Item
from src import Global
from pygame.locals import *

from src.Game_Object.Personnages import Marchand

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
        self.start_stuff_x = 300
        self.start_stuff_y = 300
        self.start_equipement_x = 70
        self.start_equipement_y = 70
        self.space_equipement = 70
        self.ring = 2 * [0]  # tableau des bijoux
        self.stuff = []
        for i in range(0, 10):  # tableau des items
            malist = []
            for j in range(0, 5):
                malist.append(0)
            self.stuff.append(malist)
        self.inventory_fond = Global.inventory_fond
        self.inventory_tile = Global.inventory_tile
        self.inventory_press_tile = Global.inventory_press_tile
        self.inventory_helmet = Global.inventory_helmet
        self.inventory_sword = Global.inventory_sword
        self.inventory_chest = Global.inventory_chest
        self.inventory_pants = Global.inventory_pants
        self.inventory_shoes = Global.inventory_shoes
        self.inventory_ring = Global.inventory_ring
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

    def blit_stuff(self, x, y, ispress):  # affiche le stuff
        window = Global.window
        if ispress:
            window.blit(self.inventory_press_tile, (self.start_stuff_x + x * 64, self.start_stuff_y + y * 64))
        else:
            window.blit(self.inventory_tile, (self.start_stuff_x + x * 64, self.start_stuff_y + y * 64))
        if self.stuff[x][y] != 0:
            window.blit(self.stuff[x][y].image, (self.start_stuff_x + x * 64 + 24, self.start_stuff_y + y * 64 + 24))
            Global.ui.write(self.stuff[x][y].describe())
        else:
            Global.ui.write("")

    def blit_equipement(self, x, y, ispress):  # affiche l'equipement
        window = Global.window
        if ispress:
            window.blit(self.inventory_press_tile, (
                self.start_equipement_x + x * self.space_equipement,
                self.start_equipement_y + y * self.space_equipement))
        else:
            window.blit(self.inventory_tile, (
                self.start_equipement_x + x * self.space_equipement,
                self.start_equipement_y + y * self.space_equipement))
        if isinstance(self.equipement[x][y], Item.Item):
            window.blit(self.equipement[x][y].image,
                        (self.start_equipement_x + x * self.space_equipement + 16,
                         self.start_equipement_y + 16 + y * self.space_equipement))
            Global.ui.write(self.equipement[x][y].describe())

        else:
            window.blit(self.equipement[x][y],
                        (self.start_equipement_x + x * self.space_equipement + 16,
                         self.start_equipement_y + 16 + y * self.space_equipement))
            Global.ui.write("")

    def throw(self, cursor_x, cursor_y, isequip):  # on jette  un item

        if isequip:
            self.equipement[cursor_x][cursor_y] = self.empty_equipement[cursor_x][
                cursor_y]
            self.blit_equipement(cursor_x, cursor_y, True)
        else:
            self.stuff[cursor_x][cursor_x] = 0
            self.blit_stuff(cursor_x, cursor_y, True)

    def pick_up(self, player, cursor_x, cursor_y, isequip):  # on prend iun item
        if isequip:
            if isinstance(self.equipement[cursor_x][cursor_y], Item.Item):
                player.inventory.pick(self.equipement[cursor_x][cursor_y])
                self.equipement[cursor_x][cursor_y] = 0
                self.blit_equipement(cursor_x, cursor_y, False)
        else:
            if isinstance(self.stuff[cursor_x][cursor_y], Item.Item):
                player.inventory.pick(self.stuff[cursor_x][cursor_y])
                self.stuff[cursor_x][cursor_y] = 0
                self.blit_stuff(cursor_x, cursor_y, False)

    def pick(self, item):  # Si il reste de la place on ajoute un item
        """

        :param item: l'itemramassé
        :return:
        """
        for i in range(0, len(self.stuff)):
            for j in range(0, len(self.stuff[i])):  # si il reste de la place
                if self.stuff[i][j] == 0:
                    self.stuff[i][j] = item
                    return i, j
        return -1, -1

    # fonction qui permet d'equipé ou desequipé un object
    def equipe(self, cursor_x, cursor_y, isequip):
        """
        :param window
        :param cursor_x: pos x u curseur
        :param cursor_y: pos y du curseur
        :param isequip: si on est dans l'equipement
        :return:
        """

        if isequip:  # si on est dans l'equipement
            if isinstance(self.equipement[cursor_x][cursor_y], Item.Item):
                i, j = self.pick(self.equipement[cursor_x][cursor_y])
                if i != -1:  # si il reste de la place dans le stuff
                    self.equipement[cursor_x][cursor_y] = self.empty_equipement[cursor_x][
                        cursor_y]  # on deplace l'object
                    self.blit_equipement(cursor_x, cursor_y, True)
                    self.blit_stuff(i, j, False)

        else:  # si on est pas dans l'equipement

            if isinstance(self.stuff[cursor_x][cursor_y], Tete.Tete):  # on verfifie quel type,d'item est selectionné
                if self.equipement[1][0] == self.inventory_helmet:  # si il n'y a rien on equipe
                    self.equipement[1][0] = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = 0

                else:  # si il y a quelque choses on echange
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][0]
                    self.equipement[1][0] = tmp
                self.blit_equipement(1, 0, False)

            if isinstance(self.stuff[cursor_x][cursor_y], Corps.Corps):
                if self.equipement[1][1] == self.inventory_chest:
                    self.equipement[1][1] = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = 0
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][1]
                    self.equipement[1][1] = tmp
                self.blit_equipement(1, 1, False)

            if isinstance(self.stuff[cursor_x][cursor_y], Jambes.Jambe):
                if self.equipement[1][2] == self.inventory_pants:
                    self.equipement[1][2] = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = 0
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][2]
                    self.equipement[1][2] = tmp
                self.blit_equipement(1, 2, False)

            if isinstance(self.stuff[cursor_x][cursor_y], Pied.Pied):
                if self.equipement[1][3] == self.inventory_shoes:
                    self.equipement[1][3] = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = 0
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[1][3]
                    self.equipement[1][3] = tmp
                self.blit_equipement(1, 0, False)

            if isinstance(self.stuff[cursor_x][cursor_y], Bijou.Bijou):
                if self.equipement[3][1] == self.inventory_ring:
                    self.equipement[3][1] = self.stuff[cursor_x][cursor_y]
                    self.blit_equipement(3, 1, False)
                    self.stuff[cursor_x][cursor_y] = 0
                elif self.equipement[3][2] == self.inventory_ring:
                    self.equipement[3][2] = self.stuff[cursor_x][cursor_y]
                    self.blit_equipement(3, 2, False)
                    self.stuff[cursor_x][cursor_y] = 0
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[3][1]
                    self.equipement[3][1] = tmp
                    self.blit_equipement(3, 1, False)

            if isinstance(self.stuff[cursor_x][cursor_y], Arme.Arme):
                if self.equipement[0][1] == self.inventory_sword:
                    self.equipement[0][1] = self.stuff[cursor_x][cursor_y]
                    self.blit_equipement(0, 1, False)
                    self.stuff[cursor_x][cursor_y] = 0
                elif self.equipement[2][1] == self.inventory_sword:
                    self.equipement[2][1] = self.stuff[cursor_x][cursor_y]
                    self.blit_equipement(2, 1, False)
                    self.stuff[cursor_x][cursor_y] = 0
                else:
                    tmp = self.stuff[cursor_x][cursor_y]
                    self.stuff[cursor_x][cursor_y] = self.equipement[0][1]
                    self.equipement[0][1] = tmp
                    self.blit_equipement(0, 1, False)
            self.blit_stuff(cursor_x, cursor_y, True)

    def anim_cursor(self, cursor_x, cursor_y, dir_x, dir_y, isequip):  # animation du curseur d'inventaire
        """

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
                    self.blit_equipement(cursor_x, cursor_y, False)
                    cursor_x = cursor_x + dir_x  # on change le curseur
                    cursor_y = cursor_y + dir_y
                    self.blit_equipement(cursor_x, cursor_y, True)

                    return cursor_x, cursor_y
            return cursor_x, cursor_y

        else:  # si on est dans le stuff
            if 0 <= cursor_x + dir_x < 10 and 0 <= cursor_y + dir_y < 5:  # on verifie que on est dans le stuff
                self.blit_stuff(cursor_x, cursor_y, False)
                cursor_x = cursor_x + dir_x  # on change le curseur
                cursor_y = cursor_y + dir_y
                self.blit_stuff(cursor_x, cursor_y, True)
                return cursor_x, cursor_y
            else:
                return cursor_x, cursor_y

    def use_inventory(self, player):  # utilisation de l'inventaire

        window = Global.window
        Global.ui.init_ui_inventory()
        inventory_width = 1300
        inventory_height = 500

        window.blit(self.inventory_fond, (0, 0))  # on affiche l'inventaire
        for i in range(0, 10):
            for j in range(0, 5):
                self.blit_stuff(i, j, False)
        window.blit(self.inventory_press_tile, (self.start_stuff_x, self.start_stuff_y))
        self.blit_stuff(0, 0, True)
        window.blit(self.inventory_tile, (self.start_equipement_x + self.space_equipement, self.start_equipement_y))
        if isinstance(self.equipement[1][0], Item.Item):
            window.blit(self.equipement[1][0].image,
                        (self.start_equipement_x + self.space_equipement + 16, self.start_equipement_y + 16))
        else:
            window.blit(self.equipement[1][0],
                        (self.start_equipement_x + self.space_equipement + 16, self.start_equipement_y + 16))

        window.blit(self.inventory_tile,
                    (self.start_equipement_x + self.space_equipement, self.start_equipement_y + self.space_equipement))
        if isinstance(self.equipement[1][1], Item.Item):
            window.blit(self.equipement[1][1].img, (
                self.start_equipement_x + self.space_equipement + 16,
                self.start_equipement_y + self.space_equipement + 16))
        else:
            window.blit(self.equipement[1][1], (
                self.start_equipement_x + self.space_equipement + 16,
                self.start_equipement_y + self.space_equipement + 16))

        window.blit(self.inventory_tile, (
            self.start_equipement_x + self.space_equipement, self.start_equipement_y + 2 * self.space_equipement))
        if isinstance(self.equipement[1][2], Item.Item):
            window.blit(self.equipement[1][2].image, (
                self.start_equipement_x + self.space_equipement + 16,
                self.start_equipement_y + 2 * self.space_equipement + 16))
        else:
            window.blit(self.equipement[1][2], (
                self.start_equipement_x + self.space_equipement + 16,
                self.start_equipement_y + 2 * self.space_equipement + 16))
            window.blit(self.inventory_tile, (
                self.start_equipement_x + self.space_equipement, self.start_equipement_y + 3 * self.space_equipement))
        if isinstance(self.equipement[1][3], Item.Item):
            window.blit(self.equipement[1][3].image, (
                self.start_equipement_x + self.space_equipement + 16,
                self.start_equipement_y + 3 * self.space_equipement + 16))
        else:
            window.blit(self.equipement[1][3], (
                self.start_equipement_x + self.space_equipement + 16,
                self.start_equipement_y + 3 * self.space_equipement + 16))

        window.blit(self.inventory_tile, (self.start_equipement_x, self.start_equipement_y + self.space_equipement))
        if isinstance(self.equipement[0][1], Item.Item):
            window.blit(self.equipement[0][1].image,
                        (self.start_equipement_x + 16, self.start_equipement_y + self.space_equipement + 16))
        else:
            window.blit(self.equipement[0][1],
                        (self.start_equipement_x + 16, self.start_equipement_y + self.space_equipement + 16))

        window.blit(self.inventory_tile, (
            self.start_equipement_x + 2 * self.space_equipement, self.start_equipement_y + self.space_equipement))
        if isinstance(self.equipement[2][1], Item.Item):
            window.blit(self.equipement[2][1].image, (
                self.start_equipement_x + 2 * self.space_equipement + 16,
                self.start_equipement_y + self.space_equipement + 16))
        else:
            window.blit(self.equipement[2][1], (
                self.start_equipement_x + 2 * self.space_equipement + 16,
                self.start_equipement_y + self.space_equipement + 16))

        window.blit(self.inventory_tile, (
            self.start_equipement_x + 3 * self.space_equipement, self.start_equipement_y + self.space_equipement))
        if isinstance(self.equipement[3][1], Item.Item):
            window.blit(self.equipement[3][1].image, (
                self.start_equipement_x + 3 * self.space_equipement + 16,
                self.start_equipement_y + self.space_equipement + 16))
        else:
            window.blit(self.equipement[3][1], (
                self.start_equipement_x + 3 * self.space_equipement + 16,
                self.start_equipement_y + self.space_equipement + 16))

        window.blit(self.inventory_tile, (
            self.start_equipement_x + 3 * self.space_equipement, self.start_equipement_y + 2 * self.space_equipement))
        if isinstance(self.equipement[3][2], Item.Item):
            window.blit(self.equipement[3][2].image, (self.start_equipement_x + 3 * self.space_equipement + 16,
                                                      self.start_equipement_y + 2 * self.space_equipement + 16))
        else:
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
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 0, 1, isequip)
                    if event.key == K_w or event.key == K_UP:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 0, -1, isequip)
                    if event.key == K_a or event.key == K_LEFT:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, -1, 0, isequip)
                    if event.key == K_d or event.key == K_RIGHT:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 1, 0, isequip)
                    if event.key == K_e:  # on equipe
                        self.equipe(cursor_x, cursor_y, isequip)
                    if event.key == K_RETURN:  # on prend
                        if player.inventory != self:
                            self.pick_up(player, cursor_x, cursor_y, isequip)
                    if event.key == K_t:  # on jette
                        self.throw(cursor_x, cursor_y, isequip)
                    if event.key == K_TAB:  # on switche de l'equipement au stuff
                        if isequip:
                            isequip = False  # on passe de l'inventaire au stuff
                            self.blit_equipement(cursor_x, cursor_y, False)
                            cursor_x = 0
                            cursor_y = 0
                            self.blit_stuff(cursor_x, cursor_y, True)
                            if isinstance(self.stuff[cursor_x][cursor_y], Item.Item):
                                Global.ui.write(self.stuff[cursor_x][cursor_y].describe())

                        else:
                            isequip = True  # on passe du stuff a l'inventaire
                            self.blit_stuff(cursor_x, cursor_y, False)
                            cursor_x = 1
                            cursor_y = 1
                            self.blit_equipement(cursor_x, cursor_y, True)
                            if isinstance(self.equipement[cursor_x][cursor_y], Item.Item):
                                Global.ui.write(self.equipement[cursor_x][cursor_y].describe())

                    if event.key == K_ESCAPE:
                        # on reessine la map
                        continuer = 0
