from src.Game_Object.Personnages import Personnage


class Player(Personnage.Personnage):

    def __init__(self, img, nom, desc,inventory, vie=100, PO=50, posX=0, posY=0, force=10, lvl=1):
        super().__init__(img, nom, desc,inventory, vie, PO, posX, posY, lvl)
        self.force = force
        self.stuff = inventory.stuff

    def level_up(self):
        self.lvl += 1
        self.max_hp += self.max_hp*0.1

    def left_hand_attack(self, arme):
        pass

    def right_hand_attack(self, arme):
        pass

