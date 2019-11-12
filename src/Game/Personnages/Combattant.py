from Game.Personnages import PNJ, Cadavre


class Combattant(PNJ.PNJ):

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], item =[], attaque = 0,lvl=1):
        super(Combattant, self).__init__(img, nom, desc, vie, PO, posX, posY, bag, lvl, attaquable=True)
        self.attaque = attaque
        self.item = item

    def heal(self, val):
        self.hp = (self.hp + abs(val)) % self.max_hp

    def die(self):
        img_cadavre = ""
        return Cadavre(img_cadavre, self.name, self.desc, self.lvl, self.money, self.X, self.Y, self.bag, self.item)