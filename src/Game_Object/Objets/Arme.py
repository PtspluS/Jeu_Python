from src.Game_Object.Objets import Item
from src import Global

class Arme(Item.Item):

    def __init__(self, name, image, atk,range, value):
        super().__init__(name, image, value)
        self.atk = atk
        self.range=range

    def use(self):
        super().use()

    def describe(self):
        #return str("it'a ", self.name, " with ", self.atk, " damage\nhe has a value of ", self.value, " PO")
        return "e"





    def anim_cursor(self,tab_map, map_pos, cursor, cursor_image, dir_x, dir_y,player):
        """
         :param window: fenetre
         :param tab_map: la carte
         :param map_pos: position des joueur sur la carte
         :param cursor: cursor
         :param cursor_image: image rouge
         :param dir_x: direction x
         :param dir_y: direction y
         :return:
              """
        if Global.isinrange(cursor.x + dir_x, cursor.y + dir_y, len(map_pos), len(map_pos[0])):  # deplacement et affichage du curseur
            Global.window.blit(cursor.image, (cursor.x * 64, cursor.y * 64))
            if map_pos[cursor.x][cursor.y] != 0:
                Global.window.blit(map_pos[cursor.x][cursor.y].img, (cursor.x * 64, cursor.y * 64))
            if(self.range>1):
                cursor = tab_map[cursor.x + dir_x][cursor.y + dir_y]
            else:cursor = tab_map[player.x + dir_x][player.y + dir_y]
            Global.window.blit(cursor_image, (cursor.x * 64, cursor.y * 64))
            return cursor
        else:
            return cursor

