from src.Game_Object.Map.terrain import Decor
from src.Global import grass1
from src.Global import grass2
import random

class Ground(Decor.Decor):
    is_destructible = False
    is_block = False
    is_walkable = True

    def __init__(self, x, y, image):
        super().__init__(x, y, image)