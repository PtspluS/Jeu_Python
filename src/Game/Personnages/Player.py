from Game.Personnages import Personnage


class Player(Personnage.Personnage):

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], attack=10, stuff=[], lvl=1):
        super().__init__(img, nom, desc, vie, PO, posX, posY, bag, lvl)
        self.attack = attack
        self.stuff = stuff