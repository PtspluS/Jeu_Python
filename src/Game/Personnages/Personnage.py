

class Personnage:

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], lvl = 1):
        self.img = img
        self.name = nom
        self.desc = desc
        self.hp = vie
        self.money = PO
        self.X = posX
        self.Y = posY
        self.bag = bag
        self.lvl = lvl

    def heal(self, val):
        self.hp = self.hp + abs(val)