from src.Game_Object.Map.terrain import Decor
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

    def open(self, lvl):
        """
        permet de savoir ou la porte mene
        :param lvl: level sur lequel on joue
        :return: [x,y,room] x et y du perso
        """
        for d in lvl.doors:
            if d.id_in == self.id_out and d.id_out == self.id_in:
                pos = [d.x, d.y]

                # une fois qu'on a trouve la porte qui correspond, on cherche la salle en rapport
                for r in lvl.rooms:
                    if r.id == d.id_in:
                        return [pos, r]

