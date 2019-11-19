import math
from room import room
import pygame
from Gameobject import Personnage
from pygame.locals import *
import math
import Global
import UI
# variable de l'ecran
width = 1500
height = 700


# verifie si la case visé est ans le tableau
def isinrange(x, y, max_x, max_y):
    """
    :param x: position x visée
    :param y: position y visée
    :param max_x: taille du tableau x
    :param max_y: taille du tableau y
    :return: si on est dans le tableau ou pas
    """
    if x >= max_x or x < 0 or y >= max_y or y < 0:
        return False
    else:
        return True


# gere l'animation du curseur
def anim_cursor(tab_map, map_pos, cursor, red_cursor, dir_x, dir_y):
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
    window=Global.window
    if isinrange(cursor.x + dir_x, cursor.y + dir_y, 10, 10):  # si on est dans le tableau
        window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))  # on affiche l'ancienne position du curseur
        if map_pos[cursor.x][cursor.y] != 0:  # si il y a un personnage on l'affice
            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
        cursor = tab_map[cursor.x + dir_x][cursor.y + dir_y]  # on actualise le curseur
        window.blit(red_cursor, (cursor.x * 64, cursor.y * 64))  # on affiche le curseur
        return cursor
    else:
        return cursor


# Faonction qui permet d'examiner les personnage
def examine( tab_map, map_pos, x, y):
    """

    :param window: la fenetre
    :param tab_map: la carte
    :param map_pos: la position des joueur sur la carte
    :param x: pos du player
    :param y: pos du player
    :return: nothing
    """
    window=Global.window
    yellow_cursor = pygame.image.load('sprite/yellow_cursor.png')  # curseur d'examination
    yellow_cursor.set_alpha(100)
    continuer = 1
    cursor = tab_map[x][y]
    window.blit(yellow_cursor, (cursor.x * 64, cursor.y * 64))
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
                if event.key == K_s or event.key == K_DOWN:
                    cursor = anim_cursor(tab_map, map_pos, cursor, yellow_cursor, 0, 1)

                if event.key == K_w or event.key == K_UP:
                    cursor = anim_cursor(tab_map, map_pos, cursor, yellow_cursor, 0, -1)

                if event.key == K_a or event.key == K_LEFT:
                    cursor = anim_cursor(tab_map, map_pos, cursor, yellow_cursor, -1, 0)

                if event.key == K_d or event.key == K_RIGHT:
                    cursor = anim_cursor(tab_map, map_pos, cursor, yellow_cursor, 1, 0)

                if event.key == K_RETURN:
                    window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                    if map_pos[cursor.x][cursor.y] != 0:
                        window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                    continuer = 0
                    if map_pos[cursor.x][cursor.y] != 0:
                        Global.ui.write(map_pos[cursor.x][cursor.y].desc)


def game(my_room, character_tab):
    """

    :param window: fenetre
    :param my_room: la salle
    :param character_tab: le tableau des personnages de la salles
    :return:
    """
    window = Global.window
    turn = 0  # gestion des tours
    bob = character_tab[0]
    Global.ui.write(bob.desc)
    Global.ui.print_coin(bob)
    Global.ui.print_life(bob)
    Global.ui.print_PA(bob)
    Global.ui.init_ui_game()
    window.blit(bob.img, (0, 0))
    window.blit(character_tab[1].img, (character_tab[1].x * 64, character_tab[1].y * 64))  # affichage des personnage
    continuer = 1
    while continuer:  # boucle du jeu
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:  # deplacement
                if event.key == K_s or event.key == K_DOWN:
                    bob.move(my_room.tab_map, my_room.map_pos, bob.x, bob.y + 1)
                if event.key == K_w or event.key == K_UP:
                    bob.move(my_room.tab_map, my_room.map_pos, bob.x, bob.y - 1)
                if event.key == K_a or event.key == K_LEFT:
                    bob.move(my_room.tab_map, my_room.map_pos, bob.x - 1, bob.y)
                if event.key == K_d or event.key == K_RIGHT:
                    bob.move(my_room.tab_map, my_room.map_pos, bob.x + 1, bob.y)
                if event.key == K_q:  # lance la fonction d'attaque
                    bob.attack(my_room.tab_map, my_room.map_pos)
                if event.key == K_x:  # lance la fonction d'examination
                    examine( my_room.tab_map, my_room.map_pos, bob.x, bob.y)
                if event.key == K_i:  # lance inventaire
                    bob.inventory.use_inventory()
                    Global.ui.init_ui_game()
                    my_room.generate()
                if event.key == K_r:  # l
                    # ance le menu de sort
                    print("r")
                if event.key == K_e:  # lance interact
                    print("e")
                if event.key == K_f:  # pich up
                    print("f")



