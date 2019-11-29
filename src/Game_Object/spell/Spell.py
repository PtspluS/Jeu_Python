import pygame

from src import Global
from pygame.locals import *

class Spell:

    def __init__(self,image,range=1,PA=0,):
        self.image=image
        self.PA_cost=PA
        self.range = range

    def anim_cursor(self, tab_map, map_pos, cursor, cursor_image, dir_x, dir_y, player):
        """
         :param window: fenetre
         :param tab_map: la carte
         :param map_pos: position des joueur sur la carte
         :param cursor: cursor
         :param cursor_image: image rouge
         :param dir_x: direction x
         :param dir_y: direction y
         :return:
              """
        if Global.isinrange(cursor.x + dir_x, cursor.y + dir_y, len(map_pos),
                            len(map_pos[0])):  # deplacement et affichage du curseur
            Global.window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
            if map_pos[cursor.x][cursor.y] != 0:
                Global.window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
            if self.range > 1:
                if (player.x == cursor.x + dir_x or player.y == cursor.y + dir_y) and (
                        abs(player.x - (cursor.x + dir_x)) <= self.range and abs(
                        player.y - (cursor.y + dir_y)) <= self.range):
                    cursor = tab_map[cursor.x + dir_x][cursor.y + dir_y]

            else:
                cursor = tab_map[player.x + dir_x][player.y + dir_y]
            Global.window.blit(cursor_image, (cursor.x * 64, cursor.y * 64))
            return cursor
        else:
            return cursor

    def cast(self,casteur, room,cursor=0):
        window = Global.window
        red_cursor = Global.red_cursor
        player = room.char_tab[0]
        room.print()
        continuer = 1
        cursor = room.tab_map[player.x][player.y]
        window.blit(red_cursor, (cursor.x * 64, cursor.y * 64))
        while continuer:  # boucle qui gere le curseur
            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                        if room.map_pos[cursor.x][cursor.y] != 0:
                            window.blit(room.map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                        return False

                    if event.key == K_s or event.key == K_DOWN:  # deplacement du curseur
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, 0, 1, player)

                    if event.key == K_w or event.key == K_UP:
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, 0, -1, player)

                    if event.key == K_a or event.key == K_LEFT:
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, -1, 0, player)

                    if event.key == K_d or event.key == K_RIGHT:
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, 1, 0, player)

                    if event.key == K_RETURN:
                       return cursor


                    pygame.display.flip()

    def describe(self):
        return Global.ui.write("it's a spell")