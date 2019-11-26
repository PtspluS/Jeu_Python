from src.Game_Object.Personnages import Player
from src.Game_Object.Personnages import Cadavre
import random


class Zombi(Player.Player):

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], attack=10, stuff=[], lvl=1):
        super(Zombi, self).__init__(img, nom, desc, vie, PO, posX, posY, bag, attack, stuff, lvl)
        self.attaque = 35

    def bite_death(self, Cadavre):
        rng = random.random()*(50-2)+2
        h = Cadavre.Cadavre.lvl*rng % 50
        self.heal(h)
