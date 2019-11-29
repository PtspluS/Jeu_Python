from src.Game_Object.Objets import Arme


class Sword(Arme.Arme):

    def __init__(self, name, image, atk, value):
        self.range=1
        self.PA = 1
        super().__init__(name, image,atk,self.range, value,nb_hand=1)


    def use(self):
        super().use()

    def anim_cursor(self,tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player):
        return super().anim_cursor(tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player)



    def describe(self):
        return str(self.name)+ " ATK:" + str(self.atk)+" Value :" +str(self.value)+ " PO"