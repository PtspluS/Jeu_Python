class Personnage:

    max_hp = 100
    max_speed = 1

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], lvl = 1):
        self.img = img
        self.name = nom
        self.desc = desc
        self.hp = vie
        self.money = PO
        self.X = posX
        self.Y = posY
        self.bag = bag
        self.lvl = lvl

    def heal(self, val):
        self.hp = self.hp + abs(val) % self.max_hp

    def move(self, window, map, posmap, x, y):
        if map[x][y].iswakable and posmap[x][y] == 0:
            window.blit(map[self.x][self.y].image,self.x,self.y)
            window.blit(self.img,x, y)
