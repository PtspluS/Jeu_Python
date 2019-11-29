import pygame
from pygame.locals import *
from src import Global
from src.Game_Object.Personnages import Cadavre
from src.Game_Object.spell.Spell import Spell


class Zombie_bite(Spell):

    def __init__(self):
        self.image = Global.bite
        self.PA_cost = 1
        self.range = 1
        super().__init__(self.image,range=self.range, PA=self.PA_cost)

    def anim_cursor(self, tab_map, map_pos, cursor, cursor_image, dir_x, dir_y, player):
        return super().anim_cursor(tab_map, map_pos, cursor, cursor_image, dir_x, dir_y, player)

    def cast(self,casteur, room,cursor=0):
        if cursor==0:
            cursor = super().cast(casteur,room)
        if casteur.PA>=self.PA_cost:
            player = room.char_tab[0]
            if cursor != False:
                if isinstance(room.map_pos[cursor.x][cursor.y], Cadavre.Cadavre):
                    h = room.map_pos[cursor.x][cursor.y].lvl * 5 + 10
                    casteur.heal(h)
                    room.map_pos[cursor.x][cursor.y] = 0
                    casteur.PA = casteur.PA - self.PA_cost
                    Global.ui.print_PA(player)
                Global.window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                if room.map_pos[cursor.x][cursor.y] != 0:
                    Global.window.blit(room.map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))



    def describe(self):
        Global.ui.write("Eat a dead enemy to heal you ")
