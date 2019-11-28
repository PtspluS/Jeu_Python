from src import marchant_inventory
from src.Game_Object.Personnages import PNJ


class Marchand(PNJ.PNJ):

    def __init__(self, img, nom, desc, inventory):
        super().__init__(img=img, nom= nom, desc = desc,inventory=inventory, attaquable= False)
        self.inventory=marchant_inventory.marchant_inventory()
        self.PA = 0
        self.PA_max = 0

    def play(self, myroom):
        self.PA = 0