from src.Game_Object.Personnages import Personnage
import pygame
from src.Game_Object.Objets import Arme
from src.Game_Object.Objets import Fist
from src import Global
from pygame.locals import *
import math
from src.inventory import inventory
from src.save import save_achivement_first_kill, save_achivement_first_respawn

class Player(Personnage.Personnage):

    def __init__(self, img, nom, inventory, vie=100, PO=50, posX=0, posY=0, lvl=1, PA=6, PA_max=6):
        super().__init__(img=img, nom=nom, inventory=inventory, vie=vie, PO=PO, posX=posX, posY=posY, lvl=lvl, PA=PA,
                         PA_max=PA_max, desc="")
        # liste des victimes
        self.victims = {}
        self.dead = False
        # nombre d'exp actuel
        self.xp = 0
        # nombre d'exp qu'il faut pour aller au prochain lvl
        self.next_level = 250

    def level_up(self):
        self.lvl += 1
        self.hp += round(self.max_hp*0.1)
        self.max_hp += round(self.max_hp*0.1)

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
        damage=0
        if isinstance(self.inventory.equipement[2][1],Arme.Arme):
            weapon = self.inventory.equipement[2][1]
            damage+=weapon.atk
        if isinstance(self.inventory.equipement[0][1], Arme.Arme):
            weapon = self.inventory.equipement[0][1]
            damage += weapon.atk
        else:
            weapon = Fist.Fist("fist", "", self.attaque, 0)
            damage += weapon.atk

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


                            map_pos[cursor.x][cursor.y].hp = map_pos[cursor.x][cursor.y].hp - damage
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
        # sert pour les achevements
        if len(self.victims) == 0:
            #pass
            save_achivement_first_kill(self)
        value = self.value_of_the_victim(victime)
        self.victims[value] = victime

        xp = self.xp_increase(victime)

        while self.xp + xp >= self.next_level:
            self.level_up()
            xp = xp - (self.next_level - self.xp)
            self.xp = 0
            self.next_level = self.next_level * (1.25)

        self.xp += xp

    def xp_increase(self, victim):
        if victim.max_hp == self.max_hp :
            victim.max_hp += 1
        eq = (1+ math.tanh(victim.lvl - self.lvl))*abs(victim.max_hp - self.max_hp)*math.log(victim.attaque, 5)

        return eq

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

    def die(self):
        """
        change les stats du players par rapport a sa derniere victime pour el faire respawn
        :return: le nouveau level genere au depart
        """
        # sert pour les achevements
        if not self.dead :
            self.dead = True
            save_achivement_first_respawn(player=self)
        victims = sorted(self.victims.items())

        # on retrouve la personne qui a la plus grande victim value
        if len(victims) != 0 :
            victim = victims[-1][1]
        else:
            victim = self

        self.hp = victim.max_hp
        self.max_hp = victim.max_hp
        if self.PA_max > victim.PA_max :
            self.PA = self.PA_max
            self.PA_max = self.PA_max
        else :
            self.PA = victim.PA_max
            self.PA_max = victim.PA_max
        self.xp = 0
        self.lvl = 1
        self.inventory = victim.inventory
        self.money = victim.money
        self.x = 1
        self.y = 1
        self.attaque = victim.attaque


        # ne pas oublier de surcharger change_image_from_victim
        self.change_image_from_victim(victim)

        if  victim.dir=="left":
            self.img=pygame.transform.flip(self.img, True,False)
            self.dir="left"

        return True

    def change_image_from_victim(self, victim):
        pass






