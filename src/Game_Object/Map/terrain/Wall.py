from src.Game_Object.Map.terrain import Decor
from src.Global import ble

class Wall(Decor.Decor):
    is_destructible = False
    is_block = True
    is_walkable = False

    def __init__(self, x, y):
        image=ble
        super().__init__(x, y, image)