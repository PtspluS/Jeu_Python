from src.Game_Object.Personnages import Marchand


class Croque_mort(Marchand.Marchand):

    def __init__(self, img, nom, desc, inventory):
        super().__init__(img=img, nom=nom, desc=desc, inventory=inventory)