from src.Game_Object.Personnages import Combattant


class Normal(Combattant.Combattant):


    def __init__(self, img, nom, desc,inventory, vie=100, PO=50, posX=0, posY=0, attaque = 0,lvl=1):
        super.__init__(img=img,nom= nom,desc= desc,inventory=inventory, vie=vie,PO= PO,posX= posX, posY=posY ,attaque= attaque,lv=lvl)

    def increase_courage(self, nb = 1):
        self.courage += nb

    def decrease_courage(self, nb = 1):
        if self.courage - nb <0:
            self.courage = 0
        else :
            self.courage -= nb