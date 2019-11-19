from terrain.Decor import Decor


class Ground(Decor):
    is_destructible = False
    is_block = False
    is_walkable = True

    def __init__(self, x, y, image):
        super().__init__(x, y, image)