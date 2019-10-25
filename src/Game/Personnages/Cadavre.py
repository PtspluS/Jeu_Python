from Game.Personnages import PNJ


class Cadavre(PNJ.PNJ):
    
    def __init__(selfimg, img, nom, desc, lvl=1,  PO=50, posX=0, posY=0, bag=[], item=[]):
        super().__init__(img, nom, desc, lvl, PO, posX, posY, bag, item, 0, False)

    def loot(self):
        return [self.money, self.item, self.bag]