from src.Game_Object.Objets import Arme


class Sword(Arme.Arme):

    def __init__(self, name, image, atk, value):
        self.range=1
        self.PA = 1
        super().__init__(name, image,atk,self.range, value)


    def use(self):
        super().use()

    def anim_cursor(self,tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player):
        return super().anim_cursor(tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player)



    def describe(self):
        print("it'a ", self.name, " with ", self.atk, " damage\nhe has a value of ", self.value, " PO")