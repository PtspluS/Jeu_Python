# imports

class Level:

    def __init__(self, map, obj_map, type, doors):
        """

        :param map: (np.array) map of the value of the room
        :param obj_map: (list [list[]]) map with the objects
        :param type: (int) if it's level 1, 2 or 3
        :param doors: (list []) list of all the door of the level
        """
        self.map = map
        self.obj_map = obj_map
        self.type = type
        self.doors = doors