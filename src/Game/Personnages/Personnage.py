

class Personnage:

    def __init__(self, img, vie=100, PO=50, posX=0, posY=0, bag=[]):
        self.img = img
        self.hp = vie
        self.money = PO
        self.X = posX
        self.Y = posY
        self.bag = bag