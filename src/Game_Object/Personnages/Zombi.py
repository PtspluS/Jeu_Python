from src import Global, Spell_book
from src.Game_Object.Personnages import Player, Villageois, Mineur, Fermier, Bourgeois
from src.Game_Object.Personnages import Cadavre
import random

from src.Game_Object.spell import Zombie_Bite


class Zombi(Player.Player):

    def __init__(self, img, nom, vie=100, PO=0, posX=0, posY=0, inventory=[], lvl=1):
        super(Zombi, self).__init__(img = img ,nom= nom,vie= vie,PO= PO,posX= posX,posY= posY, inventory=inventory, lvl = lvl)
        self.attaque = 10
        self.desc = "Je suis un zombi"
        self.spell_book=Spell_book.spell_book()
        bite=Zombie_Bite.Zombie_bite()
        self.spell_book.spell_tab[0][0]=bite



    def change_image_from_victim(self,victime):
        if isinstance(victime,Villageois.Villageois):
            self.img=Global.zombie_villager
        if isinstance(victime,Mineur.Mineur):
            self.img=Global.zombie_mineur
        if isinstance(victime,Fermier.Fermier):
            self.img=Global.zombie_farmer
        if isinstance(victime,Bourgeois.Bourgeois):
            self.img=Global.zombie_richman
