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
class marchant_inventory:
    def __init__(self):

        self.start_stuff_x = 715
        self.start_stuff_y = 300
        self.start_sell_x = 70
        self.start_sell_y = 70

        self.inventory_fond = Global.inventory_fond
        self.inventory_tile = Global.inventory_tile
        self.inventory_press_tile = Global.inventory_press_tile


        self.stuff=[]
        for i in range(0, 5):  # tableau des items
            malist = []
            for j in range(0, 5):
                malist.append(0)
            self.stuff.append(malist)

    def blit_stuff(self, x, y, ispress):  # affiche le stuff
        window = Global.window
        if ispress:
            window.blit(self.inventory_press_tile, (self.start_stuff_x + x * 64, self.start_stuff_y + y * 64))
        else:
            window.blit(self.inventory_tile, (self.start_stuff_x + x * 64, self.start_stuff_y + y * 64))
        if self.stuff[x][y] != 0:
            window.blit(self.stuff[x][y].image, (self.start_stuff_x + x * 64, self.start_stuff_y + y * 64))
            Global.ui.write(self.stuff[x][y].describe())
        else:
            Global.ui.write("")

    def blit_player_stuff(self, x, y, ispress, player):  # affiche le stuff
        window = Global.window
        if ispress:
            window.blit(self.inventory_press_tile, (self.start_sell_x + x * 64, self.start_sell_y + y * 64))
        else:
            window.blit(self.inventory_tile, (self.start_sell_x + x * 64, self.start_sell_y + y * 64))
        if player.inventory.stuff[x][y] != 0:
            window.blit(player.inventory.stuff[x][y].image,
                        (self.start_sell_x + x * 64, self.start_sell_y + y * 64))
            Global.ui.write(player.inventory.stuff[x][y].describe())
        else:
            Global.ui.write("")


    def buy(self, player, cursor_x, cursor_y, issel):
        if issel:
            if isinstance(player.inventory.stuff[cursor_x][cursor_y], Item.Item):
                player.money+=player.inventory.stuff[cursor_x][cursor_y].value
                player.inventory.stuff[cursor_x][cursor_y]=0
                self.blit_player_stuff(cursor_x, cursor_y, True,player)

        else:
            if isinstance(self.stuff[cursor_x][cursor_y], Item.Item):
                if self.stuff[cursor_x][cursor_y].value<=player.money:
                    player.inventory.pick(self.stuff[cursor_x][cursor_y])
                    self.stuff[cursor_x][cursor_y]=0
                    player.money -=self.stuff[cursor_x][cursor_y].value
                    self.blit_stuff(cursor_x, cursor_y, True)
        Global.ui.print_coin(player)

    def anim_cursor(self, cursor_x, cursor_y, dir_x, dir_y, isequip,player):  # animation du curseur d'inventaire
        """
        :param window: la fenetre
        :param cursor_x: posx du curseur
        :param cursor_y: posy u curseur
        :param dir_x: direction du curseur
        :param dir_y: direction du curseur
        :param isequip: est on dans l'equipement ou le stuff
        :return: cursor
        """
        window = Global.window
        if isequip:  # si on est dans le stuff du joueur
            if 0 <= cursor_x + dir_x < 10 and 0 <= cursor_y + dir_y < 5:  # est on en dehors de l'inventaire
                self.blit_player_stuff(cursor_x, cursor_y, False, player)
                cursor_x = cursor_x + dir_x  # on change le curseur
                cursor_y = cursor_y + dir_y
                self.blit_player_stuff(cursor_x, cursor_y, True, player)




            return cursor_x, cursor_y

        else:  # si on est dans le stuff
            if 0 <= cursor_x + dir_x < 5 and 0 <= cursor_y + dir_y < 5:  # on verifie que on est dans le stuff
                self.blit_stuff(cursor_x, cursor_y, False)
                cursor_x = cursor_x + dir_x  # on change le curseur
                cursor_y = cursor_y + dir_y
                self.blit_stuff(cursor_x, cursor_y, True)
                return cursor_x, cursor_y
            else:
                return cursor_x, cursor_y

    def use_inventory(self, player):

        window = Global.window
        Global.ui.init_ui_marchant()
        inventory_width = 1300
        inventory_height = 500
        window.blit(self.inventory_fond, (0, 0))
        for i in range(0, 5):
            for j in range(0, 5):
                self.blit_stuff(i, j, False)
        window.blit(self.inventory_press_tile, (self.start_stuff_x, self.start_stuff_y))
        self.blit_stuff(0, 0, True)

        for i in range(0, 10):
            for j in range(0, 5):
                self.blit_player_stuff(i, j, False, player)


        cursor_x = 0
        cursor_y = 0
        issell = False
        continuer = 1
        while continuer:  # boucle de gestion de l'inventaire

            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_s or event.key == K_DOWN:  # on detecte le entré clavier
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 0, 1, issell,player)
                    if event.key == K_w or event.key == K_UP:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 0, -1, issell,player)
                    if event.key == K_a or event.key == K_LEFT:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, -1, 0, issell,player)
                    if event.key == K_d or event.key == K_RIGHT:
                        cursor_x, cursor_y = self.anim_cursor(cursor_x, cursor_y, 1, 0, issell,player)
                    if event.key == K_RETURN:
                        self.buy(player, cursor_x, cursor_y, issell)
                    if event.key == K_TAB:
                        if issell:
                            issell = False  # on passe de l'inventaire au stuff
                            self.blit_player_stuff(cursor_x, cursor_y, False,player)
                            cursor_x = 0
                            cursor_y = 0
                            self.blit_stuff(cursor_x, cursor_y, True)
                            if isinstance(self.stuff[cursor_x][cursor_y], Item.Item):
                                Global.ui.write(player.inventory.stuff[cursor_x][cursor_y].describe())

                        else:
                            issell = True  # on passe du stuff a l'inventaire
                            self.blit_stuff(cursor_x, cursor_y, False)
                            cursor_x = 0
                            cursor_y = 0
                            self.blit_player_stuff(cursor_x, cursor_y, True,player)
                            if isinstance(player.inventory.stuff[cursor_x][cursor_y], Item.Item):
                                Global.ui.write(player.inventory.stuff[cursor_x][cursor_y].describe())

                    if event.key == K_ESCAPE:
                        # on reessine la map
                        continuer = 0







