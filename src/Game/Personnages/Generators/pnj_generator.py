from Game.Personnages import Fermier, Mineur, Villageois, Bourgeois
import random


list_name_poor = [
    "Billy le borgne",
    "Michel sans bretelles",
    "Piolet",
    "Maurycy",
    "Roch",
    "Urban",
    "Bronislaw",
    "Ari",
    "Hansel",
    "Herbert",
    "Tymoteusz",
    "Johann",
    "Albin",
    "Marek",
    "Remigiusz",
    "Albert",
    "Dan"
]
list_name_rich = [
    "Emil Daniel",
    "Cyprian Nowak",
    "Quincy Todd",
    "Jed Schmidt",
    "Antonin Vallet",
    "Walter Paul",
    "Marian Jordan",
    "Ali Todd",
    "Arda Lewandowski",
    "Tomek Krawczyk",
    "Cezary Humphreys",
    "Adam Wojciechowski",
    "Aleksandr Daniel",
    "Mo Rose",
    "Martin Abraham"
]

img_farmer = ""
img_miner = ""
img_villager = ""
img_bourgeois = ""

'''
function which generate a random civil : Fermier or Mineur.py or Villageois or Bourgeois
'''
def generate_civil(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0, type='civ'):
    #si jamais le mec donne n'imps on crée un perso rng
    if(type != 'fermier' and type != 'mineur' and type != 'villageois' and type != 'bourgeois'):
        tab_type = ['fermier', 'mineur', 'villageois', 'bourgepois']
        type = random.choice(tab_type)

    if type == 'fermier':
        return generate_fermier(attaque, vie, niveau, stuff, PA, PO)

    elif type == 'mineur':
        return generate_mineur(attaque, vie, niveau, stuff, PA, PO)

    elif type == 'villageois':
        return generate_villageois(attaque, vie, niveau, stuff, PA, PO)

    else:
        return generate_bourgeois(attaque, vie, niveau, stuff, PA, PO)




'''
function which generate a farmer
'''
def generate_fermier(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    # def des attributs et de leurs bornes
    att_max = 10
    vie_max = 150
    vie_min = 50
    lvl_max = 3
    lvl_min = 1

    PA_list = [2,3,4]

    PO_max = 30
    PO_min = 10

    courage_max = 3
    courage_min = 1

    name = random.choice(list_name_poor)
    courage = random.randint(courage_min, courage_max)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)
    if len(stuff) == 0:
        pass
    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on return un objet fermier avec les attributs aleatoires
    return Fermier.Fermier(img_farmer, name, vie = vie, PO = PO, bag = stuff, attaque = attaque, lvl = niveau, PA = PA, courage = courage)

'''
function which generate a miner
'''
def generate_mineur(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    # def des attributs et de leurs bornes
    att_max = 15
    vie_max = 150
    vie_min = 75
    lvl_max = 4
    lvl_min = 2

    PA_list = [2, 3, 4]

    PO_max = 75
    PO_min = 25

    courage_max = 5
    courage_min = 2

    name = random.choice(list_name_poor)
    courage = random.randint(courage_min, courage_max)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)
    if len(stuff) == 0:
        pass
    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on renvoit un obj mineur
    return Mineur.Mineur(img_miner, name, vie = vie, PO = PO, bag = stuff, attaque = attaque, lvl = niveau, PA = PA)


'''
function which generate a villager
'''
def generate_villageois(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    # def des attributs et de leurs bornes
    att_max = 10
    vie_max = 150
    vie_min = 50
    lvl_max = 5
    lvl_min = 3

    PA_list = [2, 3, 4]

    PO_max = 100
    PO_min = 50

    courage_max = 3
    courage_min = 2

    name = random.choice(list_name_rich)
    courage = random.randint(courage_min, courage_max)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)
    if len(stuff) == 0:
        pass
    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on renvoit un obj villageois
    return Villageois.Villageois(img_villager, name, vie = vie, PO = PO, bag = stuff, attaque = attaque, lvl = niveau, PA = PA)


'''
function which generate a bourgeois
'''
def generate_bourgeois(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    # def des attributs et de leurs bornes
    att_max = 10
    vie_max = 150
    vie_min = 50
    lvl_max = 7
    lvl_min = 4

    PA_list = [1, 2, 3]

    PO_max = 3000
    PO_min = 100

    courage_max = 2
    courage_min = 1

    name = random.choice(list_name_rich)
    courage = random.randint(courage_min, courage_max)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)
    if len(stuff) == 0:
        pass
    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on renvoit un objet bourgeois
    return Bourgeois.Bourgeois(img_bourgeois, name, vie = vie, PO = PO, bag = stuff, attaque = attaque, lvl = niveau, PA = PA)