from src.Game_Object.Objets import Item


class Armure(Item.Item):

    def __init__(self, name, image, armor,value):
        super().__init__(name, image,value)
        self.armor = armor

    def use(self):
        super().use()

    def describe(self):
        print("it'a ", self.name, " with ", self.armor, " armor\nhe has a value of ", self.value, " PO")