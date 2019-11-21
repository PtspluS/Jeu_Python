# imports
import numpy as np

class Level:

    def __init__(self, map, type, doors, rooms):
        """

        :param map: (np.array) map of the value of the room
        :param obj_map: (list [list[]]) map with the objects
        :param type: (int) if it's level 1, 2 or 3
        :param doors: (list []) list of all the door of the level
        """
        self.map = map
        self.type = type
        self.doors = doors
        self.rooms = rooms
        self.obj_map = self.convert_to_obj_map()

    def convert_to_obj_map(self):
        convert = [[0]*self.map.shape[0] for i in range(self.map.shape[1])]
        srt = sort_map(self.map)
        srt.reverse()
        for r in self.rooms:
            convert[srt[0][0]][srt[0][1]] = r
            srt.remove(srt[0])

        return convert


def sort_map(map):
    """
    yolo c'est magique en fait non mais c'est pas propre
    :param map: (np.array 2D) map avec des int
    :return: return list de pos
    """
    mp = np.copy(map)
    a = np.array(map)
    i = (-a).argsort(axis=None, kind='mergesort')
    j = np.unravel_index(i, a.shape)
    # sort = np.vstack(j).T
    #sort = [[x, y] for x, y in zip(j[0], j[1])]
    sort = []
    for x,y in zip(j[0], j[1]):
        if mp[x][y] != 0:
            sort.append([x,y])
    return sort

