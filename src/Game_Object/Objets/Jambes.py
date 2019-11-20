from src.Game_Object.Objets import Armure


class Jambe(Armure.Armure):

    def __init__(self, name, image, armor,value):
        super().__init__(name, image, armor,value)

    def use(self):
        super().use()

    def describe(self):
        super().use()
