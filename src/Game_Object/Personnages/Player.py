from Game_Object.Personnages import Personnage


class Player(Personnage.Personnage):

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], force=10, stuff=[], lvl=1):
        super().__init__(img, nom, desc, vie, PO, posX, posY, bag, lvl)
        self.force = force
        self.stuff = stuff

    def level_up(self):
        self.lvl += 1
        self.max_hp += self.max_hp*0.1

    def left_hand_attack(self, arme):
        pass

    def right_hand_attack(self, arme):
        pass

