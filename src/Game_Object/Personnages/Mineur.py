from src.Game_Object.Personnages import Combattant

class Mineur(Combattant.Combattant):

    def __init__(self, img, nom, desc = "",inventory=[], vie=100, PO=50, posX=0, posY=0, attaque = 0,lvl=1, PA = 1):
        super().__init__(img, nom, desc, inventory, vie, PO, posX, posY, attaque, lvl)
        self.PA = PA
