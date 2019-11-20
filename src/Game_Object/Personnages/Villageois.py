from src.Game_Object.Personnages import Normal


class Villageois(Normal.Normal):

    def __init__(self, img, nom, desc ='',inventory=[], vie=100, PO=50, posX=0, posY=0, attaque=0, lvl=1,
                 PA=1):
        super(Normal.Normal, self).__init__(img, nom, desc = desc,inventory=inventory, vie=vie, PO=PO, posX=posX, posY=posY, attaque=attaque,
                       lvl=lvl)
        self.PA = PA