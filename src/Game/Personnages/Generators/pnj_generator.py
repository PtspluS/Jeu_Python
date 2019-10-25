from Game.Personnages import *
import random

'''
function which generate a random civil : Fermier or Mineur or Villageois or Bourgeois
'''
def generate_civil(attaque, vie, niveau, stuff, PA, PO, type='civ'):
    #si jamais le mec donne n'imps on crée un perso rng
    if(type != 'fermier' and type != 'mineur' and type != 'villageois' and type != 'bourgeois'):
        rng = int(random.random()*(4) % 4)
        tab_type = ['fermier', 'mineur', 'villageois', 'bourgepois']
        type = tab_type[rng]

    if type == 'fermier':
        pass

    elif type == 'mineur':
        pass

    elif type == 'villageois':
        pass

    else:
        pass




'''

'''
def generate_fermier():
    pass


'''

'''
def generate_mineur():
    pass


'''

'''
def generate_villageois():
    pass


'''

'''
def generate_bourgeois():
    pass