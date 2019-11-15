#imports


class Room:

    def __init__(self, id, brute_map, tab_map, map_pos, char_tab, doors, type):
        self.id = id
        self.brute_map = brute_map
        self.tab_map = tab_map
        self.map_pos = map_pos
        self.char_tab = char_tab
        self.doors = doors
        self.type = type