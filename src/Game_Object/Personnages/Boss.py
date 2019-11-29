from src.Game_Object.Personnages import Combattant


class Boss(Combattant.Combattant):

    def __init__(self,img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl, ranges):
        super().__init__(img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl, ranges=self.ranges)
