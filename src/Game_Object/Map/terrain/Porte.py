from src.Game_Object.terrain import Decor
from src import Global


class Porte(Decor.Decor):
    is_destructible = False
    is_block = True
    is_walkable = False
    is_close = True

    def __init__(self, id, id_in, id_out, x = 0, y = 0):
        self.id = id
        self.id_in = id_in
        self.id_out = id_out
        image = Global.door
        super().__init__(x, y, image)
