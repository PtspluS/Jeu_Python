from terrain import Decor


class Door(Decor):
    is_destructible = False
    is_block = True
    is_walkable = False
    is_close=True

    def __init__(self):
        super().__init__()