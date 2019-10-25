from terrain import Decor


class Water(Decor):
    is_destructible = False
    is_block = False
    is_walkable = False

    def __init__(self):
        super().__init__()