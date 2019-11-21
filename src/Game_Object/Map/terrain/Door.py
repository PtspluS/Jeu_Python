from src.Game_Object.Map.terrain import Decor
from src import Global


class Door(Decor.Decor):
    is_destructible = False
    is_block = True
    is_walkable = False
    is_close=True

    def __init__(self, x, y):
        image = Global.door
        super().__init__(x, y, image)
