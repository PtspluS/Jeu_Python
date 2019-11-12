from Game.Personnages import PNJ


class Cadavre(PNJ.PNJ):
    
    def __init__(self, img, nom, desc, lvl=1,  PO=0, posX=0, posY=0, bag=[], item=[]):
        super().__init__(img, nom, desc, lvl, PO, posX, posY, bag, 0, False)
        self.item = item
        self.attaquable = False

    def loot(self):
        return [self.money, self.item, self.bag]