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
    if pos_portes[0] == 1:
        porte = Porte(id_door, id, id_previous, random.randint(1,size_X-2), size_Y-1)
        doors.append(porte)
    # porte vers le bas
    elif pos_portes[1] == 1:
        porte = Porte(id_door, id, id_previous, random.randint(1, size_X-2), 0)
        doors.append(porte)
    # porte vers la gauche
    elif pos_portes[2] == 1:
        porte = Porte(id_door, id, id_previous, 0,  random.randint(1,size_Y-2))
        doors.append(porte)
    # porte vers la droite
    elif pos_portes[3] == 1:
        porte = Porte(id_door, id, id_previous, size_X-1, random.randint(1, size_Y-2))
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
        p.X = x
        p.Y = y
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












