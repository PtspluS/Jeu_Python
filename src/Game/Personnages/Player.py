from Game.Personnages import Personnage


class Player(Personnage):

    def __init__(self, attack=10, stuff=[]):
        self.attack = attack
        self.stuff = stuff