import pygame
from pygame.locals import *

from src import Global
from src.Game_Object.spell import Spell


class spell_book:
    def __init__(self):
        self.spell_tab = []
        for i in range(0, 5):  # tableau des items
            malist = []
            for j in range(0, 2):
                malist.append(0)
            self.spell_tab.append(malist)
        self.inventory_fond = Global.inventory_fond
        self.inventory_tile = Global.inventory_tile
        self.inventory_press_tile = Global.inventory_press_tile
        self.start_spell_x = 100
        self.start_spell_y = 100

    def blit_spell(self, x, y, ispress):  # affiche le stuff
        window = Global.window
        if ispress:
            window.blit(self.inventory_press_tile, (self.start_spell_x + x * 64, self.start_spell_y + y * 64))
        else:
            window.blit(self.inventory_tile, (self.start_spell_x + x * 64, self.start_spell_y + y * 64))
        if isinstance(self.spell_tab[x][y],Spell.Spell):
            window.blit(self.spell_tab[x][y].image, (self.start_spell_x + x * 64, self.start_spell_y + y * 64 ))
            self.spell_tab[x][y].describe()
        else:
            Global.ui.write("")

    def anim_cursor(self, cursor_x, cursor_y, dir_x, dir_y):  # animation du curseur d'inventaire
        """

        :param cursor_x: posx du curseur
        :param cursor_y: posy u curseur
        :param dir_x: direction du curseur
        :param dir_y: direction du curseur

        :return: cursor
        """
        if 0 <= cursor_x + dir_x < 5 and 0 <= cursor_y + dir_y < 2:  # est on en dehors du spell book

            self.blit_spell(cursor_x, cursor_y, False)
            cursor_x = cursor_x + dir_x  # on change le curseur
            cursor_y = cursor_y + dir_y
            self.blit_spell(cursor_x, cursor_y, True)


        return cursor_x, cursor_y

    def open(self,room):
        cursor_x=0
        cursor_y=0
        continuer=1
        window = Global.window
        Global.ui.init_ui_inventory()
        window.blit(self.inventory_fond, (0, 0))
        for i in range(0, 5):
            for j in range(0, 2):
                self.blit_spell(i, j, False)
        window.blit(self.inventory_press_tile, (self.start_spell_x, self.start_spell_y))
        self.blit_spell(0, 0, True)
        while continuer:  # boucle de gestion de l'inventaire

            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_s or event.key == K_DOWN:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 0, 1)
                    # on detecte le entré clavier

                    if event.key == K_w or event.key == K_UP:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 0, -1)

                    if event.key == K_a or event.key == K_LEFT:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, -1, 0)

                    if event.key == K_d or event.key == K_RIGHT:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 1, 0)

                    if event.key == K_RETURN:
                        if  self.spell_tab[cursor_x][cursor_y]!=0:
                            self.spell_tab[cursor_x][cursor_y].cast(room)
                        continuer=0
                    if event.key == K_ESCAPE:
                        # on reessine la map
                        continuer = 0


