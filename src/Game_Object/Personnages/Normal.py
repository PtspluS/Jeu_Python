from Game_Object.Personnages import Combattant


class Normal(Combattant.Combattant):


    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], item =[], attaque = 0,lvl=1):
        super.__init__(img, nom, desc, vie, PO, posX, posY, bag, item , attaque,lvl)

    def increase_courage(self, nb = 1):
        self.courage += nb

    def decrease_courage(self, nb = 1):
        if self.courage - nb <0:
            self.courage = 0
        else :
            self.courage -= nb