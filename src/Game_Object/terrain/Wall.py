from src.Game_Object.terrain import Decor
from src.Global import wall

class Wall(Decor.Decor):
    is_destructible = False
    is_block = True
    is_walkable = False

    def __init__(self, x, y):
        image=wall
        super().__init__(x, y, image)