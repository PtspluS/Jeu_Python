from Game.Personnages import Personnage


class PNJ(Personnage.Personnage):

    def __init__(self, img, vie=100, PO=50, posX=0, posY=0, bag=[], item=[]):
        super.__init__(img, vie, PO, posX, posY, bag)
        self.item = item
