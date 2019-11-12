from Gameobject import Objet


class Item(Objet.Objet):

    def __init__(self, image):
        super().__init__()
        self.image=image
