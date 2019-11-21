# imports
import random
import numpy as np
from src.Game_Object.Personnages.Generators.pnj_generator import generate_civil
from src.Game_Object.Map.Porte import Porte
from src.Game_Object.Map.Room import Room


# pos_portes = [droite, gauche, haut, bas]

def generate_room(id, id_next, id_previous, type, nb_char = -1, pos_portes = [1,0,0,0], marchand = False):

    last_room = False

    size_X_max = 17
    size_X_min = 10
    size_Y_max = 11
    size_Y_min = 8

    min_char = 1
    max_char = 5

    nb_decors = 10

    # on regarde si la piece c'est une premiere ou derniere piece
    if id_next == -1:
        last_room = True

    # on genere le nombre de personnages dans la map
    if nb_char == -1 and not marchand:
        nb_char = random.randint(min_char,max_char)
    elif marchand:
        nb_char = 0
    elif last_room:
        nb_char = random.randint(0,2)
        boss = 1

    # on genere la taille de la map
    size_X = random.randint(size_X_min, size_X_max)
    size_Y = random.randint(size_Y_min, size_Y_max)

    # on genere les portes
    id_door = 1
    doors = []
    # porte vers le haut
    if pos_portes[0] != 0:
        #porte = Porte(id_door, id, id_previous, random.randint(1,size_X-2), size_Y-1)
        porte = pos_portes[0]
        porte.X = random.randint(1,size_X-2)
        porte.Y = size_Y-1
        doors.append(porte)
    # porte vers le bas
    elif pos_portes[1] != 0:
        #porte = Porte(id_door, id, id_previous, random.randint(1, size_X-2), 0)
        porte = pos_portes[1]
        porte.X = random.randint(1, size_X-2)
        porte.Y = 0
        doors.append(porte)
    # porte vers la gauche
    elif pos_portes[2] != 0:
        #porte = Porte(id_door, id, id_previous, 0,  random.randint(1,size_Y-2))
        porte = pos_portes[2]
        porte.X = 0
        porte.Y = random.randint(1,size_Y-2)
        doors.append(porte)
    # porte vers la droite
    elif pos_portes[3] != 0:
        #porte = Porte(id_door, id, id_previous, size_X-1, random.randint(1, size_Y-2))
        porte = pos_portes[3]
        porte.X = size_X-1
        porte.Y = random.randint(1, size_Y-2)
        doors.append(porte)

    # on genere les pnj dans la piece
    pnj = []
    pnj_type = ['fermier', 'mineur', 'villageois', 'bourgeois']
    type_present = []
    map_pos = [size_Y * [0] for i in range(size_X)]
    # on definit quel type de pnj sera present dans la piece
    if type == 'champs':
        type_present.append(pnj_type[0])
        type_present.append(pnj_type[0])
    elif type == 'mines':
        type_present.append(pnj_type[1])
        type_present.append(pnj_type[1])
    elif type == 'faubourg':
        type_present.append(pnj_type[2])
        type_present.append(pnj_type[3])
    elif type == 'porte':
        type_present.append(pnj_type[2])
        type_present.append(pnj_type[3])

    # on regarde ou on peut mettre les persos
    x_possible = list(range(2, size_X-2))
    y_possible = list(range(2, size_Y-2))
    for i in range(nb_char):
        # on donne des pos rng aux persos et on retire du tab les endroit ou ils sont
        x = random.choice(x_possible)
        y = random.choice(y_possible)
        x_possible.remove(x)
        y_possible.remove(y)
        # on genere un civil pour le moment mais a la fin ca sera un mec selon son type
        p = generate_civil(type= random.choice(type_present))
        p.x = x
        p.y = y
        pnj.append(p)
        map_pos[x][y] = p

    # on genere la map brute
    brute_map = np.zeros((size_X, size_Y), dtype='int64')
    proba_decor = 0.2
    nb_decor_gen = 0
    for i in range(len(brute_map)):
        for j in range(len(brute_map[i])):
            # on entoure la map de 1 pour les murs
            if i == 0 or i == size_X-1 or j == 0 or j == size_Y-1:
                brute_map[i][j] = 1
            if i in x_possible and j in y_possible :
                if proba_decor >  random.random() and nb_decor_gen < nb_decors:
                    brute_map[i][j] = 3
                    x_possible.remove(i)
                    y_possible.remove(j)
                    nb_decor_gen += 1
                    proba_decor -= random.choice([0.01, 0.005])
                else :
                    proba_decor += random.choice([0.01,0.05,0.075,0.1])

            for d in doors :
                 if d.X == i and d.Y == j :
                     brute_map[i][j] = 2

    room = Room(id, brute_map = brute_map, map_pos= map_pos, char_tab= pnj, doors = doors, type=type)


    return room


def generate_level(type = 1, nb_room = 5):
    # chance de faire pop un marchand dans une salle
    ratio_pop_marchand = 0.5

    brute_map = np.zeros((10,10), dtype='int64')

    pt = np.array([5,5])

    directions = [[1,0], [0,1], [-1,0], [0,-1]]

    current_id = 1
    rooms = []

    while current_id <= nb_room and (pt < brute_map.shape).all():
        brute_map[pt[0]][pt[1]] = current_id
        current_id += 1
        pt += random.choice(directions)

    # pos_portes = [droite, gauche, haut, bas]
    # si on est dans la premiere partie
    if type == 1:
        type_room = ['champs', 'mines', 'faubourg', 'porte']
        # on renvoit une map trié dans l'odre inverse des salles de max -> salle de depart
        srt_map = sort_map(brute_map)
        id_porte = 0
        for i in range(len(srt_map)):
            room = srt_map[i]
            id = brute_map[room[0]][room[1]]
            id_previous = -1
            id_next = -1
            tab = [0,0,0,0]
            if i != len(srt_map):
                id_next = brute_map[srt_map[i+1][0]][srt_map[i+1][1]]
                next_room = srt_map[i + 1]

                # on vient voir on est situe next_room par rapport a room
                # pos_portes = [droite, gauche, haut, bas]
                if room[0] < next_room[0]:
                    tab[0] = Porte(id_porte, id, id_next)
                    id_porte += 1
                elif room[0] > next_room[0]:
                    tab[1] = Porte(id_porte, id, id_next)
                    id_porte += 1
                elif room[1] > next_room[1]:
                    tab[3] = Porte(id_porte, id, id_next)
                    id_porte += 1
                elif room[1] < next_room[1]:
                    tab[2] = Porte(id_porte, id, id_next)
                    id_porte += 1
            if i != 0 :
                id_previous = brute_map[srt_map[i-1][0]][srt_map[i-1][1]]
                previous_room = srt_map[i-1]

                # on vient voir ou se situe previous_room par rapport a room
                # pos_portes = [droite, gauche, haut, bas]
                if room[0] < previous_room[0]:
                    tab[0] = Porte(id_porte, id, id_previous)
                    id_porte += 1
                elif room[0] > previous_room[0]:
                    tab[1] = Porte(id_porte, id, id_previous)
                    id_porte += 1
                elif room[1] > previous_room[1]:
                    tab[3] = Porte(id_porte, id, id_previous)
                    id_porte += 1
                elif room[1] < previous_room[1]:
                    tab[2] = Porte(id_porte, id, id_previous)
                    id_porte += 1



    # si on est dans la seconde partie
    elif type == 2:
        pass
    # si on est dans la derniere partie
    elif type == 3:
        pass

def sort_map(map):
    a = np.array(map)
    i = (-a).argsort(axis=None, kind='mergesort')
    j = np.unravel_index(i, a.shape)
    # sort = np.vstack(j).T
    sort = [[x, y] for x, y in zip(j[0], j[1])]
    return sort








