from src.Game_Object.Objets import Arme


class Fist(Arme.Arme):

    def __init__(self, name, image, atk, value):
        self.range=1
        self.PA = 1
        super().__init__(name, image,atk,self.range, value)

    def anim_cursor(self,tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player):
        return super().anim_cursor(tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player)





