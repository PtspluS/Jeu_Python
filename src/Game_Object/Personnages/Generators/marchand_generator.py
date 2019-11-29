from src.Game_Object.Objets.Generators.arme_generator import generate_bow, generate_sword
from src.Game_Object.Personnages.Rousse import Rousse
from src.Game_Object.Personnages.Lepreux import Lepreux
from src.Game_Object.Personnages.Croque_mort import Croque_mort
from src.marchant_inventory import marchant_inventory
from src import Global

import random

def generate_marchand(t = 0):
    t_marchand = ['Rousse', 'Lepreux', 'Croque_mort']
    if t != 'Rousse' and t != 'Lepreux' and t != 'Croque_mort':
        t = random.choice(t_marchand)

    if t == t_marchand[0]:
        return generate_rousse()
    elif t == t_marchand[1]:
        return generate_lepreux()
    elif t == t_marchand[2]:
        return generate_croque()


def generate_rousse():
    pass


def generate_lepreux():
    inv = marchant_inventory()

    nb_item = random.randint(3, 7)

    offre = []

    # permet de s'assurer qu'au moins un item de chaque niveau est cree
    item_lvl1 = False
    item_lvl2 = False
    item_lvl3 = False
    item_lvl4 = False

    # sert pour gen les item
    t_item_min = 0 # 0 pour les arcs
    t_item_max = 1 # 1 pour les epes
    for _ in range(nb_item):

        # sert a definir le t de l'item
        t = random.randint(t_item_min,t_item_max)

        # on vient voir quel item on genere
        if not item_lvl1:
            if t == 0:
                item = generate_bow(1)
            elif t == 1:
                item = generate_sword(1)

            item_lvl1 = True

        elif not item_lvl2:
            if t == 0:
                item = generate_bow(2)
            elif t == 1:
                item = generate_sword(2)

            item_lvl2 = True

        elif not item_lvl3:
            if t == 0:
                item = generate_bow(3)
            elif t == 1:
                item = generate_sword(3)

            item_lvl3 = True

        elif not item_lvl4:
            if t == 0:
                item = generate_bow(4)
            elif t == 1:
                item = generate_sword(4)

            item_lvl4 = True

        # si on a au moins genere un item de chaque niveau
        else :
            lvl = random.randint(1,4)

            if t == 0:
                item = generate_bow(lvl)
            elif t == 1:
                item = generate_sword(lvl)

        offre.append(item)

    for i in offre:
        inv.pick(i)

    nom = "Lépreux"
    desc = "Si il perd un bras, il peut bien en vendre un..."
    img = Global.zombie_bowman
    return Lepreux(img=img, nom=nom, desc=desc, inventory=inv)


def generate_croque():
    pass
