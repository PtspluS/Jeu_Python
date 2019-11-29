from src.Game_Object.Map.terrain import Decor


class Water(Decor.Decor):
    is_destructible = False
    is_block = False
    is_walkable = False

    def __init__(self, x, y, image):
        super().__init__(x, y, image)