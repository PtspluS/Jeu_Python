from src.Game_Object.Personnages import Fermier, Mineur, Villageois, Bourgeois
import random
from src import inventory
from src import Global

# partie poor pour les fermiers et mineurs
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
descriptions_poor = [
    "Aime le vin, les femmes et l'eau plate (c'est un type d'alcool dans ce pays).",
    "Son père est partie chercher du pain depuis ses 18 ans, il garde espoir de le retrouver.",
    "A trouvé une pépite dans un champs de blé, dommage qu'elle était en chocolat.",
    "Avant il travaillait à la poste mais avec sa petite taille on le prenait pour un nain posteur.",
    "Il n'est pas gros, il est joviale et épanoui.",
    "Chez lui c'est lui qui commande, après sa femme bien entendu.",
    "Ne boit jamais d'eau.",
    "Ne boit jamais de vin.",
    "Ne boit pas tout court, mais comment il fait d'ailleurs ?",
    "Il a travaillé dans des mines de trucs brillants, il se souvient plus de quoi.",
    "Sa plus grande peur ? Que le ciel lui tombe sur la tête."

]


# partie rich, pour les villageois et les bourgeois
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
descriptions_rich = [
    "De tous ces voyages il n'a ramené que une chose, la syphilis.",
    "Il voulait être médecin, mais ici c'est pas comme ça que ça marche.",
    "Ne lui parlait pas de son frère, vraiment.",
    "Il sait qui a volé l'orange du marchand.",
    "Son pote Karl ne lui parle que d'un monde égalitaire.",
    "NULL pointer exception ... Non je rigole, il y a juste rien à dire sur lui.",
    "On en parle de ses 3 femmes ?",
    "L'infinie ne lui suffit plus, il vise au delà.",
    "C'est le mari de Curry"

]

img_farmer = Global.bowman
img_miner = Global.miner
img_villager = Global.villager
img_bourgeois = Global.richman

'''
function which generate a random civil : Fermier or Mineur or Villageois or Bourgeois
'''
def generate_civil(attaque = 0, vie = 0, niveau = 0, stuff = inventory.inventory(), PA = 0, PO = 0, type='civ'):
    #si jamais le mec donne n'imps on crée un perso rng
    if(type != 'fermier' and type != 'mineur' and type != 'villageois' and type != 'bourgeois'):
        tab_type = ['fermier', 'mineur', 'villageois', 'bourgeois']
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
    att_max = 20
    vie_max = 150
    vie_min = 75
    lvl_max = 3
    lvl_min = 1

    PA_list = [2,3,4]

    PO_max = 40
    PO_min = 15

    courage_max = 3
    courage_min = 1

    name = random.choice(list_name_poor)
    courage = random.randint(courage_min, courage_max)
    desc = random.choice(descriptions_poor)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)

    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on return un objet fermier avec les attributs aleatoires
    return Fermier.Fermier(img_farmer, name, vie = vie, PO = PO, inventory = stuff, attaque = attaque, lvl = niveau, PA = PA, courage = courage, desc= desc)

'''
function which generate a miner
'''
def generate_mineur(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    # def des attributs et de leurs bornes
    att_max = 25
    vie_max = 150
    vie_min = 50
    lvl_max = 4
    lvl_min = 2

    PA_list = [2, 3, 4]

    PO_max = 75
    PO_min = 25

    courage_max = 5
    courage_min = 2

    name = random.choice(list_name_poor)
    courage = random.randint(courage_min, courage_max)
    desc = random.choice(descriptions_poor)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)

    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on renvoit un obj mineur
    return Mineur.Mineur(img_miner, name, vie = vie, PO = PO, inventory = stuff, attaque = attaque, lvl = niveau, PA = PA, desc= desc)


'''
function which generate a villager
'''
def generate_villageois(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    # def des attributs et de leurs bornes
    att_max = 20
    vie_max = 200
    vie_min = 100
    lvl_max = 5
    lvl_min = 3

    PA_list = [2, 3, 4]

    PO_max = 100
    PO_min = 50

    courage_max = 3
    courage_min = 2

    name = random.choice(list_name_rich)
    courage = random.randint(courage_min, courage_max)
    desc = random.choice(descriptions_rich)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)

    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on renvoit un obj villageois
    return Villageois.Villageois(img_villager, name,inventory=stuff, vie = vie, PO = PO, attaque = attaque, lvl = niveau, PA = PA, desc= desc)


'''
function which generate a bourgeois
'''
def generate_bourgeois(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    # def des attributs et de leurs bornes
    att_max = 15
    vie_max = 200
    vie_min = 125
    lvl_max = 7
    lvl_min = 4

    PA_list = [1, 2, 3]

    PO_max = 3000
    PO_min = 100

    courage_max = 2
    courage_min = 1

    name = random.choice(list_name_rich)
    courage = random.randint(courage_min, courage_max)
    desc = random.choice(descriptions_rich)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if (attaque <= 0):
        attaque = random.randint(1, att_max)
    if vie <= 0:
        vie = random.randint(vie_min, vie_max)
    if niveau <= 0:
        niveau = random.randint(lvl_min, lvl_max)

    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0:
        PO = random.randint(PO_min, PO_max)

    # on renvoit un objet bourgeois
    return Bourgeois.Bourgeois(img_bourgeois, name, vie = vie, PO = PO, inventory = stuff, attaque = attaque, lvl = niveau, PA = PA, desc = desc)