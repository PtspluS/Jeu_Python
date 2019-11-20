from src.Game_Object.Objets import Item


class Arme(Item.Item):

    def __init__(self, name, image, atk, value):
        super().__init__(name, image, value)
        self.atk = atk

    def use(self):
        super().use()

    def describe(self):
        print("it'a ", self.name, " with ", self.atk, " damage\nhe has a value of ", self.value, " PO")