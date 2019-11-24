from src.Game_Object.Personnages import Personnage
import pygame
from src.Game_Object.Objets import Arme
from src.Game_Object.Objets import Fist
from src import Global
from pygame.locals import *
import math
from src.Game_Object.Map.Generator.game_generator import generate_level
import random
from src.inventory import inventory

class Player(Personnage.Personnage):

    def __init__(self, img, nom,inventory, vie=100, PO=50, posX=0, posY=0, lvl=1,PA=6,PA_max=6):
        super().__init__(img, nom, inventory, vie, PO, posX, posY, lvl,PA,PA_max, desc= "")
        # liste des victimes
        self.victims = {}

    def level_up(self):
        self.lvl += 1
        self.max_hp += self.max_hp*0.1

    def move(self, tab_map, map_pos, x, y):
        super().move(tab_map,map_pos,x,y)

    def attack(self, tab_map, map_pos):  # fonction d'attaque
        """

        :param window: fenetre
        :param tab_map: la carte
        :param map_pos: la position des joueur sur la carte
        :return:
        """
        window = Global.window
        red_cursor = Global.red_cursor
        if isinstance(self.inventory.equipement[0][1],Arme.Arme):
            weapon=self.inventory.equipement[0][1]
        elif isinstance(self.inventory.equipement[2][1],Arme.Arme):
            weapon = self.inventory.equipement[2][1]
        else:
            weapon = Fist.Fist("fist", "", 10, 0)

        continuer = 1
        cursor = tab_map[self.x][self.y]
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
                        if map_pos[cursor.x][cursor.y] != 0:
                            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                    if event.key == K_s or event.key == K_DOWN:  # deplacement du curseur
                        cursor = weapon.anim_cursor(tab_map, map_pos, cursor, red_cursor, 0, 1,self)

                    if event.key == K_w or event.key == K_UP:
                        cursor = weapon.anim_cursor(tab_map, map_pos, cursor, red_cursor, 0, -1,self)

                    if event.key == K_a or event.key == K_LEFT:
                        cursor = weapon.anim_cursor(tab_map, map_pos, cursor, red_cursor, -1, 0,self)

                    if event.key == K_d or event.key == K_RIGHT:
                        cursor = weapon.anim_cursor(tab_map, map_pos, cursor, red_cursor, 1, 0,self)

                    if event.key == K_RETURN:
                        window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
                        if map_pos[cursor.x][cursor.y] != 0:
                            window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
                            map_pos[cursor.x][cursor.y].hp = map_pos[cursor.x][cursor.y].hp - weapon.atk
                            print(map_pos[cursor.x][cursor.y].hp)

                        continuer = 0
                        self.PA=self.PA-weapon.PA
                        Global.ui.print_PA(self)
                    pygame.display.flip()

    def kill(self, victime):
        """
        add the victim to the list of the monster's victims
        :param victime: object Combattant
        :return:
        """
        value = self.value_of_the_victim(victime)
        self.victims[value] = victime

    @staticmethod
    def value_of_the_victim(victime):
        """
        equation to determine the value of a victim.
        :param victime: object Combatant
        :return: the result of the equation
        """
        if victime.lvl == 1:
            victime.lvl += 1
        res = victime.max_hp*victime.attaque/math.log(victime.lvl, 2)

        return res

    def respawn(self):
        """
        change les stats du players par rapport a sa derniere victime pour el faire respawn
        :return: le nouveau level genere au depart
        """
        victims = sorted(self.victims.items())
        # on retrouve la personne qui a la plus grande victim value
        victim = victims[-1][1]

        self.hp = victim.hp
        self.max_hp = victim.hp_max
        self.PA_max = self.PA_max // 2 + victim.PA_max
        self.inventory = inventory()

        # ne pas oublier de surcharger change_image_from_victim
        self.change_image_from_victim(victim)

        return generate_level(1, random.randint(7, 15))

    def change_image_from_victim(self, victim):
        pass






