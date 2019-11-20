from src.Game_Object.Personnages import PNJ


class Cadavre(PNJ.PNJ):
    
    def __init__(self, img, nom, desc,inventory, lvl=1,  PO=0, posX=0, posY=0):
        super().__init__(img, nom, desc,inventory, lvl, PO, posX, posY, 0, False)
        self.item = inventory.stuff
        self.attaquable = False

    def loot(self):
        return [self.money, self.item, self.item]