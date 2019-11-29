import pygame
from pygame.locals import *
from src import Global
from src.Game_Object.Personnages import Cadavre
from src.Game_Object.spell.Spell import Spell


class Kick(Spell):

    def __init__(self):
        self.image = Global.spell
        self.PA_cost = 1
        self.range = 1
        super().__init__(self.image,range=self.range, PA=self.PA_cost)

    def anim_cursor(self, tab_map, map_pos, cursor, cursor_image, dir_x, dir_y, player):
        return super().anim_cursor(tab_map, map_pos, cursor, cursor_image, dir_x, dir_y, player)

    def cast(self,casteur, room,cursor=0,):
        if cursor==0:
            cursor = super().cast(casteur,room)
        player = room.char_tab[0]
        if cursor != False:
            if room.map_pos[cursor.x][cursor.y]!=0:
                target=room.map_pos[cursor.x][cursor.y]
                ismove=target.PA
                target.move(room.tab_map,room.map_pos,cursor.x+(cursor.x-casteur.x),cursor.y+(cursor.y-casteur.y))
                casteur.PA =casteur.PA - self.PA_cost
                if target.PA!=ismove:
                    target.PA-=1
                    target.hp-=10
                else :
                    target.PA+=1
                Global.ui.print_PA(player)
            Global.window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
            if room.map_pos[cursor.x][cursor.y] != 0:
                Global.window.blit(room.map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))

    def describe(self):
        Global.ui.write("repousse ton enemie ")
