from Game.Personnages import Fermier
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
    "Tymoteusz"
]
list_name_rich = [
    "Emil Daniel",
    "Cyprian Nowak",
    "Quincy Todd",
    "Jed Schmidt"
]

img_farmer = ""
img_miner = ""
img_villager = ""
img_bourgeois = ""

'''
function which generate a random civil : Fermier or Mineur or Villageois or Bourgeois
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

    name = random.choice(list_name_poor)
    # on genere ds valeurs aleatoire pour les attributs du pnj
    if(attaque<=0):
        attaque = random.randint()*(att_max)
    if vie <= 0:
        vie = random.randint()*vie_max + vie_min
    if niveau <= 0:
        niveau = random.randint()*lvl_max+lvl_min
    if len(stuff) == 0:
        pass
    if PA == 0:
        PA = random.choice(PA_list)
    if PO == 0 :
        PO = random.randint()*PO_max+PO_min

    # on return un objet fermier avec les attributs aleatoires
    return Fermier(img_farmer, name, vie = vie, PO = PO, bag = stuff, attaque = attaque, lvl = niveau, PA = PA, courage = 1)

'''
function which generate a miner
'''
def generate_mineur(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    pass


'''
function which generate a villager
'''
def generate_villageois(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    pass


'''
function which generate a bourgeois
'''
def generate_bourgeois(attaque = 0, vie = 0, niveau = 0, stuff = [], PA = 0, PO = 0):
    pass