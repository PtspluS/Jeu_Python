import math
from src.Game_Object.Map.Generator.game_generator import generate_room
from src.Game_Object.Map.terrain import Porte
import pygame
from src.Game_Object.Personnages import Cadavre
from src.Game_Object.Personnages import Player
from pygame.locals import *
import math
from src import Global

# variable de l'ecran
width = 1500
height = 700


# verifie si la case visé est ans le tableau


# gere l'animation du curseur
def anim_cursor(tab_map, map_pos, cursor, red_cursor, dir_x, dir_y, player, image_cursor):
    """
    :param window: l'objet fenetre de pygame
    :param tab_map: la carte
    :param map_pos: la position des joueur sur la carte
    :param cursor: objet curseur qui pointe sur une case
    :param red_cursor: image du cursor rouge
    :param dir_x: direction du curseur en x
    :param dir_y:irection du curseur en y
    :return:la position du curseur
    """
    window = Global.window
    if Global.isinrange(cursor.x + dir_x, cursor.y + dir_y, len(map_pos), len(map_pos[0])):  # si on est dans le tableau
        window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))  # on affiche l'ancienne position du curseur
        if map_pos[cursor.x][cursor.y] != 0:  # si il y a un personnage on l'affice
            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
        if image_cursor == Global.yellow_cursor:
            cursor = tab_map[cursor.x + dir_x][cursor.y + dir_y]
        else:
            cursor = tab_map[player.x + dir_x][player.y + dir_y]
        # on actualise le curseur
        window.blit(red_cursor, (cursor.x * 64, cursor.y * 64))  # on affiche le curseur
        return cursor
    else:
        return cursor


# Faonction qui permet d'examiner les personnage
def examine(tab_map, map_pos, x, y, image_cursor, player):
    """

    :param window: la fenetre
    :param tab_map: la carte
    :param map_pos: la position des joueur sur la carte
    :param x: pos du player
    :param y: pos du player
    :return: nothing
    """
    window = Global.window
    continuer = 1
    cursor = tab_map[x][y]
    window.blit(image_cursor, (cursor.x * 64, cursor.y * 64))
    while continuer:  # boucle qui permet de deplacer le curseur
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # retour
                    window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                    continuer = 0
                    if map_pos[cursor.x][cursor.y] != 0:
                        window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                    return False
                if event.key == K_s or event.key == K_DOWN:
                    cursor = anim_cursor(tab_map, map_pos, cursor, image_cursor, 0, 1, player, image_cursor)

                if event.key == K_w or event.key == K_UP:
                    cursor = anim_cursor(tab_map, map_pos, cursor, image_cursor, 0, -1, player, image_cursor)

                if event.key == K_a or event.key == K_LEFT:
                    cursor = anim_cursor(tab_map, map_pos, cursor, image_cursor, -1, 0, player, image_cursor)

                if event.key == K_d or event.key == K_RIGHT:
                    cursor = anim_cursor(tab_map, map_pos, cursor, image_cursor, 1, 0, player, image_cursor)

                if event.key == K_RETURN:
                    window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                    if map_pos[cursor.x][cursor.y] != 0:
                        window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                    continuer = 0
                    if image_cursor == Global.yellow_cursor:
                        Global.ui.write(map_pos[cursor.x][cursor.y].description())
                        return False
                    else:
                        if isinstance(map_pos[cursor.x][cursor.y], Cadavre.Cadavre):
                            map_pos[cursor.x][cursor.y].inventory.use_inventory(player)
                            map_pos[cursor.x][cursor.y]=0
                            Global.ui.init_ui_game()
                            return False
                        elif isinstance(tab_map[cursor.x][cursor.y], Porte.Porte):
                            door = tab_map[cursor.x][cursor.y].open()

                            return door
                        else:
                            return False


def game(my_room, player):
    """
    :param window: fenetre
    :param my_room: la salle
    :param character_tab: le tableau des personnages de la salles
    :return:
    """

    my_room.map_pos[player.x][player.y] = player
    player.PA = player.PA_max
    if len(my_room.char_tab)==0:
        my_room.char_tab.append(player)
        my_room.char_tab.reverse()
    elif not isinstance( my_room.char_tab[0],Player.Player):
        my_room.char_tab.append(player)
        my_room.char_tab.reverse()


    window = Global.window
    Global.ui.write(player.desc)
    Global.ui.print_coin(player)
    Global.ui.print_life(player)
    Global.ui.print_PA(player)
    Global.ui.init_ui_game()
    my_room.print()
    pygame.display.flip()
    turn=0
    continuer = 1
    while continuer:  # boucle du jeu

        if isinstance(my_room.char_tab[turn], Player.Player):
            for event in pygame.event.get():

                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:  # deplacement
                    if event.key == K_s or event.key == K_DOWN:
                        player.move(my_room.tab_map, my_room.map_pos, player.x, player.y + 1)
                    if event.key == K_w or event.key == K_UP:
                        player.move(my_room.tab_map, my_room.map_pos, player.x, player.y - 1)
                    if event.key == K_a or event.key == K_LEFT:
                        player.move(my_room.tab_map, my_room.map_pos, player.x - 1, player.y)
                    if event.key == K_d or event.key == K_RIGHT:
                        player.move(my_room.tab_map, my_room.map_pos, player.x + 1, player.y)
                    if event.key == K_q:  # lance la fonction d'attaque
                        player.attack(my_room.tab_map, my_room.map_pos)
                    if event.key == K_x:  # lance la fonction d'examination
                        examine(my_room.tab_map, my_room.map_pos, player.x, player.y, Global.yellow_cursor, player)
                    if event.key == K_i:  # lance inventaire
                        player.inventory.use_inventory(player)
                        Global.ui.init_ui_game()
                        my_room.print()
                    if event.key == K_r:  # l
                        # ance le menu de sort
                        print("r")
                    if event.key == K_SPACE:  # l
                        # ance le menu de sort
                        player.PA=0
                    if event.key == K_e:  # lance interact
                       door=examine(my_room.tab_map, my_room.map_pos, player.x, player.y, Global.cyan_cursor, player)
                       if door:
                           my_room.map_pos[player.x][player.y] = 0
                           return door
                       else :
                           my_room.print()


        else:
            my_room.char_tab[turn].play(my_room)

        for i in my_room.char_tab:
            if i.hp <= 0:
                cadavre=i.die()
                if cadavre==True:
                   return player
                else:
                    player.kill(i)
                my_room.char_tab.remove(i)
                my_room.map_pos[i.x][i.y]=cadavre
                my_room.print()
        if my_room.char_tab[turn].PA <= 0:
            my_room.char_tab[turn].PA = my_room.char_tab[turn].PA_max
            Global.ui.print_PA(my_room.char_tab[turn])
            turn = (turn + 1) % len(my_room.char_tab)
        Global.ui.print_life(player)
        pygame.display.flip()
