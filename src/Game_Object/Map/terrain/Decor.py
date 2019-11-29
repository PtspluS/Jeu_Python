

class Decor:
    isdestructible = False
    isblock = False
    iswalkable = False

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
