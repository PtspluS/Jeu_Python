from src.Game_Object.Objets import Arme


class Bow(Arme.Arme):

    def __init__(self, name, image, atk, value):
        self.range=5
        self.PA = 2
        super().__init__(name, image,atk, self.range, value)

    def anim_cursor(self,tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player):
        if (player.x == cursor.x+dir_x or player.y== cursor.y+dir_y) and (abs(player.x-(cursor.x+dir_x))<=self.range and abs(player.y- (cursor.y+dir_y))<=self.range ):
            return super().anim_cursor(tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player)
        else :
            return cursor