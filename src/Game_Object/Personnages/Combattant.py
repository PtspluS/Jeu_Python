from Game_Object.Personnages import PNJ, Cadavre


class Combattant(PNJ.PNJ):

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], item =[], attaque = 0,lvl=1):
        super(Combattant, self).__init__(img, nom = nom, desc = desc, vie= vie, PO= PO, posX= posX, posY = posY, bag = bag, lvl=lvl, attaquable=True)
        self.attaque = attaque
        self.item = item

    def heal(self, val):
        self.hp = (self.hp + abs(val)) % self.max_hp

    def die(self):
        img_cadavre = ""
        return Cadavre.Cadavre(img_cadavre, nom = self.name, desc = self.desc, lvl = self.lvl, PO= self.money, posX= self.X, posY=self.Y, bag= self.bag,item= self.item)