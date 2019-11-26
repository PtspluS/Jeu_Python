from src.Game_Object.Objets import Objet


class Item(Objet.Objet):

    def __init__(self, name, image, value):
        self.image = image
        self.name = name
        self.value = value

    def use(self):
        pass

    def describe(self):
        pass
