class Personnage:

    max_hp = 100
    max_speed = 1

    def __init__(self, img, nom, desc, vie=100, PO=50, posX=0, posY=0, bag=[], lvl = 1):
        self.img = img
        self.name = nom
        self.desc = desc
        self.hp = vie
        self.money = PO
        self.x = posX
        self.y = posY
        self.bag = bag
        self.lvl = lvl

    def heal(self, val):
        self.hp = self.hp + abs(val) % self.max_hp

    def move(self, window, map, map_pos, x, y):
        if map[x][y].is_walkable and map_pos[x][y] == 0:
            window.blit(map[self.x][self.y].image,(self.x*64,self.y*64))
            map_pos[self.x][self.y] = 0
            self.x = x
            self.y = y
            (map_pos[self.x][self.y]) = self
            window.blit(self.img,(self.x*64, self.y*64))
