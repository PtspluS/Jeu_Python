from Game.Personnages import Normal


class Mineur(Normal.Normal):

    def __init__(self, img, nom, desc = "", vie=100, PO=50, posX=0, posY=0, bag=[], item =[], attaque = 0,lvl=1, PA = 1):
        super(Normal.Normal, self).__init__(img, nom, desc = desc, vie=vie, PO=PO, posX=posX, posY=posY, bag=bag, item=item, attaque=attaque,
                       lvl=lvl)
        self.PA = PA
