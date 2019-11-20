from src.Game_Object.Personnages import Player
from src.Game_Object.Personnages import Cadavre
import random


class Zombi(Player.Player):

    def __init__(self, img, nom, vie=100, PO=50, posX=0, posY=0, stuff=[], lvl=1):
        super(Zombi, self).__init__(img = img, nom = nom, vie = vie, PO = PO, posX = posX, posY = posY, inventory = stuff, lvl = lvl)
        self.desc = "Je suis un zombi."

    # sort de charognard
    def bite_death(self, Cadavre):
        rng = random.randint(25, 55)
        h = Cadavre.Cadavre.lvl*rng % 50
        self.heal(h)
