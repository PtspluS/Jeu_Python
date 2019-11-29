from src.Game_Object.Personnages import Personnage


class PNJ(Personnage.Personnage):

    def __init__(self, img, nom, desc,inventory, vie=100, PO=50, posX=0, posY=0, lvl=1, attaquable=True):
        super().__init__(img,nom= nom,desc =  desc,inventory=inventory,vie= vie, PO=PO, posX=posX, posY=posY,  lvl=lvl)
        self.attaquable = attaquable

    def ciblable(self):
        return self.attaquable