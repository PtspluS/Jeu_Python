import math

class Personnage:

    max_hp = 100
    max_speed = 1

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
        self.max_hp = vie

    def isoutofrange(self, X, Y, rangeX, rangeY):
        range = math.sqrt(rangeX + rangeY)

        if self.X + range <= X and self.Y + range <= Y :
            return False
        else :
            return True