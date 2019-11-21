from src.Game_Object.Personnages import PNJ, Cadavre
from src import Global

class Combattant(PNJ.PNJ):

    def __init__(self, img, nom, desc,inventory, vie=100, PO=50, posX=0, posY=0, attaque = 0,lvl=1):
        super(Combattant, self).__init__(img, nom = nom, desc = desc,inventory=inventory, vie= vie, PO= PO, posX= posX, posY = posY, lvl=lvl, attaquable=True)
        self.attaque = attaque
        self.item = inventory.stuff

    def heal(self, val):
        self.hp = (self.hp + abs(val)) % self.max_hp

    def play(self,room):
        self.PA=0

    def die(self):
        img_cadavre = Global.inventory_ring
        return Cadavre.Cadavre(img_cadavre, nom = self.name, desc = self.desc,inventory=self.inventory, lvl = self.lvl, PO= self.money, posX= self.x, posY=self.y)