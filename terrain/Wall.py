from terrain import Decor


class Wall(Decor):
    is_destructible = False
    is_block = True
    is_walkable = False

    def __init__(self):
        super().__init__()