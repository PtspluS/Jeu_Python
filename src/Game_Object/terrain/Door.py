from src.Game_Object.terrain import Decor


class Door(Decor.Decor):
    is_destructible = False
    is_block = True
    is_walkable = False
    is_close=True

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
