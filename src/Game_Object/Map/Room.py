from src import Global
import pygame
from src.Game_Object.Map.terrain import Wall, Porte, ground, Water
import src.Global as Global

class Room:

    # tableau qui donne les bons objets selon le type de la piece
    translate_table = {
        'champs': {0: Global.dirt, 1: Global.ble, 2: Global.door, 3: Global.ble},
        'mines': {0: Global.grass1, 1: Global.wall, 2: Global.door, 3: Global.wall},
        'faubourg': {0: Global.grass1, 1: Global.wall, 2: Global.door, 3: Global.wall},
        'porte': {0: Global.grass1, 1: Global.wall, 2: Global.door, 3: Global.wall}
    }

    def __init__(self, id, brute_map, map_pos, char_tab, doors, type):
        """

        :param id: (int) id de la map
        :param brute_map: (np.array) map sous la forme de tableau de chiffre
        :param map_pos: (list[list]) map sous la forme de tableau de personnages
        :param char_tab: (list) list des pnj sur la salle
        :param doors: (list) list des portes de la salle
        :param type: (str) type de la salle
        """
        self.id = id
        self.brute_map = brute_map
        self.tab_map = []
        self.map_pos = map_pos
        self.char_tab = char_tab
        self.doors = doors
        self.type = type
        self.convert_to_tab_map()

    def convert_to_tab_map(self):
        for i in range(0, len(self.brute_map)):
            maliste=[]
            for j in range(0, len(self.brute_map[i])):
                if self.brute_map[i][j] == 0:
                    myground = ground.Ground(i, j, image=self.translate_table[self.type][0])
                    maliste.append(myground)
                if self.brute_map[i][j] == 1:
                    my_wall = Wall.Wall(i, j, image=self.translate_table[self.type][1])
                    maliste.append(my_wall)
                if self.brute_map[i][j] == 2:
                    for k in self.doors:
                        if k.x==i and k.y==j:
                            my_door = k
                            maliste.append(my_door)

                if self.brute_map[i][j] == 3:
                    my_wall = Wall.Wall(i, j, image=self.translate_table[self.type][3])
                    maliste.append(my_wall)
            self.tab_map.append(maliste)

        return []

    def print(self):  # fonction qui dessine la map
        """

        :param window: la feneter
        :return:
        """
        window=Global.window
        window.blit(Global.black, (0, 0))
        for i in range(0, len(self.tab_map)):
            for j in range(0, len(self.tab_map[i])):
                window.blit(self.tab_map[i][j].image, (self.tab_map[i][j].x * 64, self.tab_map[i][j].y * 64))
                if self.map_pos[i][j] != 0:
                    window.blit(self.map_pos[i][j].img, (self.map_pos[i][j].x * 64, self.map_pos[i][j].y * 64))
