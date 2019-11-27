import random

from src.Game_Object.Personnages import PNJ


class Cadavre(PNJ.PNJ):
    
    def __init__(self, img, nom, desc,inventory, lvl=1,  PO=0, posX=0, posY=0):
        super().__init__(img, nom, desc,inventory, lvl, PO, posX, posY, 0, False)
        self.item = inventory.stuff
        self.attaquable = False
        self.desc=random.choice(["La première qualité d'un héros, c'est d'être mort et enterré."," Monstre, ne pleure pas ma mort - Si je vivais tu serais mort"])

    def loot(self):
        return [self.money, self.item, self.item]


    def description(self):

        txt = str(self.desc)

        return txt