from src.Game_Object.Objets.Generators.arme_generator import generate_bow, generate_sword
from src.inventory import inventory
from src import Global
import random


def generate_stuff(lvl):
    tab_proba = {
        1: {1: 0.8, 2: 0.15, 3: 0.05, 4: 0, "nb_item_max": 2, "nb_item_min": 0},
        2: {1: 0.8, 2: 0.15, 3: 0.05, 4: 0, "nb_item_max": 2, "nb_item_min": 1},
        3: {1: 0.8, 2: 0.15, 3: 0.05, 4: 0, "nb_item_max": 3, "nb_item_min": 1},
        4: {1: 0.8, 2: 0.15, 3: 0.05, 4: 0, "nb_item_max": 3, "nb_item_min": 2},
        5: {1: 0.6, 2: 0.25, 3: 0.15, 4: 0, "nb_item_max": 4, "nb_item_min": 2},
        6: {1: 0.5, 2: 0.25, 3: 0.15, 4: 0.1, "nb_item_max": 5, "nb_item_min": 2},
        7: {1: 0.45, 2: 0.25, 3: 0.15, 4: 0.15, "nb_item_max": 5, "nb_item_min": 3},
    }

    # on sort la ligne du tableau correpondant au niveau du pnj
    proba_items = tab_proba[lvl]

    items_lvl = [4,3,2,1]

    type_arme = ["epee", "arc"]

    nb_item = random.randint(proba_items["nb_item_min"], proba_items["nb_item_max"])

    rng = random.random()

    i = 0

    stuff = []

    # on remplis le tableau stuff avec des armes
    for _ in range(nb_item):
        while proba_items[items_lvl[i]] < rng:
            i += 1
            if i >= len(items_lvl):
                i = 0
                rng = random.random()

        t = random.choice(type_arme)
        if t == "epee" :
            item = generate_sword(items_lvl[i])
        elif t == 'arc':
            item = generate_bow(items_lvl[i])

        stuff.append(item)

    inv = inventory()
    for s in stuff:
        inv.pick(s)

    return inv



