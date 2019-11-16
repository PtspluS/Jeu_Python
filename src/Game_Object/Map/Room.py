#imports


class Room:

    def __init__(self, id, brute_map, map_pos, char_tab, doors, type):
        """

        :param id: (int) id de la map
        :param brute_map: (np.array) map sous la forme de tableau de chiffre
        :param tab_map: (list[list]) map sous la forme de tableau d'objets
        :param map_pos: (list[list]) map sous la forme de tableau de personnages
        :param char_tab: (list) list des pnj sur la salle
        :param doors: (list) list des portes de la salle
        :param type: (str) type de la salle
        """
        self.id = id
        self.brute_map = brute_map
        self.tab_map = self.convert_to_tab_map()
        self.map_pos = map_pos
        self.char_tab = char_tab
        self.doors = doors
        self.type = type

    def convert_to_tab_map(self):
        return []