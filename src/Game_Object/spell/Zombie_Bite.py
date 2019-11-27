import pygame
from pygame.locals import *
from src import Global
from src.Game_Object.Personnages import Cadavre
from src.Game_Object.spell.Spell import Spell


class Zombie_bite(Spell):

    def __init__(self):
        self.image=Global.bite
        self.PA_cost=1
        self.range=1

    def anim_cursor(self, tab_map, map_pos, cursor, cursor_image, dir_x, dir_y, player):
        return super().anim_cursor(tab_map, map_pos, cursor, cursor_image, dir_x, dir_y, player)


    def cast(self,room):
        window = Global.window
        red_cursor = Global.red_cursor
        player=room.char_tab[0]
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
                        continuer = 0
                        if room.map_pos[cursor.x][cursor.y] != 0:
                            window.blit(room.map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                    if event.key == K_s or event.key == K_DOWN:  # deplacement du curseur
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, 0, 1, player)

                    if event.key == K_w or event.key == K_UP:
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, 0, -1, player)

                    if event.key == K_a or event.key == K_LEFT:
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, -1, 0, player)

                    if event.key == K_d or event.key == K_RIGHT:
                        cursor = self.anim_cursor(room.tab_map, room.map_pos, cursor, red_cursor, 1, 0, player)

                    if event.key == K_RETURN:
                        if isinstance(room.map_pos[cursor.x][cursor.y],Cadavre.Cadavre):
                            h = room.map_pos[cursor.x][cursor.y].lvl * 5 + 10
                            player.heal(h)
                            room.map_pos[cursor.x][cursor.y]=0
                            player.PA =   player.PA- self.PA_cost
                            Global.ui.print_PA(player)
                        window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                        if room.map_pos[cursor.x][cursor.y] != 0:
                            window.blit(room.map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                        continuer = 0

                    pygame.display.flip()

    def describe(self):
        Global.ui.write("Eat a dead enemy to heal you ")
