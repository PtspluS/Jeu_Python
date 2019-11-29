from src.Game_Object.Personnages import Boss


class Garde_de_la_porte(Boss.Boss):

    def __init__(self,img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl):
        self.ranges=2
        super().__init__(img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl, ranges=self.ranges)