from Game.Personnages import Personnage


class Player(Personnage.Personnage):

    def __init__(self, img, vie=100, PO=50, posX=0, posY=0, bag=[], attack=10, stuff=[]):
        super.__init__(img, vie, PO, posX, posY, bag)
        self.attack = attack
        self.stuff = stuff