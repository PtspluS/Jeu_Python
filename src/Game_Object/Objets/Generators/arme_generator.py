from src.Game_Object.Objets.Sword import Sword
from src.Game_Object.Objets.Bow import Bow
import random
from src import Global

def generate_sword(rarete = 1):
    epe_type = [
        "Dard",
        "Rapiere",
        "Glaive",
        "Claymor",
        "Espadon",
        "Epee batarde",
        "Flamberge",
        "Dao",
        "Sabre",
        "Scimtaire",
        "Epee crochee"
    ]

    adj_1 = [
        "emouse",
        "en bois",
        "fendu",
        "casse",
        "de seconde main",
        "peu aiguise",
        "a bout rond",
        "a la garde cassee",
        "sans garde",
        "a la poignet sans protection",
        ""
    ]

    adj_2 = [
        "hors de prix",
        "achete au rabait",
        "avec une garde en bois",
        "mal equilibre",
        "neuf",
        "ensanglante",
        ""
    ]

    adj_3 = [
        "parfaitement aiguise",
        "de maitre",
        "unique au monde",
        "au pommeau d'or",
        "pour expert",
        "pour noble",
        "grave en lettre d'or",
        "sans aucune marque"
    ]

    if rarete <= 1:
        value_max = 100
        value_min = 1

        img = Global.epe2

        atk_max = 12
        atk_min = 5

        name = random.choice(epe_type)+" "+random.choice(adj_1)

    elif rarete == 2:
        value_max = 250
        value_min = 50

        img = Global.epe2

        atk_max = 39
        atk_min = 20

        name = random.choice(epe_type) + " " + random.choice(adj_2)
    elif rarete == 3:
        value_max = 800
        value_min = 100

        img = Global.epe3

        atk_max = 53
        atk_min = 45

        name = random.choice(epe_type) + " " + random.choice(adj_3)
    elif rarete == 4:
        legendaire = [
            ["Flamberge volcanique", Global.epe4, 69, 8502],
            ["Sabre de damocles", Global.epe4, 60, 7952],
            ["Epee en diamand", Global.epe4, 56, 5050],
            ["Claymor nordique", Global.epe4, 79, 6100],
            ["Manoda", Global.epe4, 83, 9547],
            ["Hotmourne", Global.epe4, 64,  8472],
            ["Slave Sword", Global.epe4, 51, 5555]
        ]

        sw = random.choice(legendaire)
        return Sword(sw[0], sw[1], sw[2], sw[3])

    return Sword(name= name, image=img, atk=random.randint(atk_min, atk_max), value= random.randint(value_min, value_max))

def generate_bow(rarete = 1):
    arc_type = [
        "Arc classique",
        "Recurve",
        "Arc monobloc",
        "Arc demontable",
        "Arc a poulies",
        "Arc composite",
        "Longbow",
        "Arc nu",
        "Arc de chasse",
        "Arc de competition",
        "Yumi"
    ]

    adj_1 = [
        "en bois de chauffage",
        "long",
        "en fil de peche",
        "sans protege bras",
        "tordu",
        "sans viseur",
        "en bois de chaise",
        "beaucoup trop petit",
        "de bebe",
        ""
    ]

    adj_2 = [
        "de paysan",
        "de chasseur",
        "de garde",
        "gorge de vin",
        "avec un mire en fer",
        "avec une mire en bois",
        "equilibre",
        ""
    ]

    adj_3 = [
        "de specialiste",
        "de seigneur",
        "en bois noble",
        "en noisetier",
        'sans defaut',
        "au fleches d'or",
        ""
    ]

    if rarete <= 1:
        range_min = 3
        range_max = 5

        value_min = 1
        value_max = 100

        atk_min = 7
        atk_max = 30

        name = random.choice(arc_type)+' '+random.choice(adj_1)
        img = Global.arc1

    elif rarete == 2:
        range_min = 3
        range_max = 6

        value_min = 80
        value_max = 250

        atk_min = 20
        atk_max = 50

        name = random.choice(arc_type) + ' ' + random.choice(adj_2)
        img = Global.arc1

    elif rarete == 3:
        range_min = 4
        range_max = 6

        value_min = 300
        value_max = 750

        atk_min = 55
        atk_max = 95

        name = random.choice(arc_type) + ' ' + random.choice(adj_3)
        img = Global.arc1

    elif rarete == 4:
        arc = [
            ["Gandiva", Global.arc4, 134, 5789, 8],
            ["Vijaya", Global.arc4, 126, 5005, 9],
            ["Penelope", Global.arc4, 145, 9578, 12],
            ["Arc de Paris", Global.arc4, 200, 9782, 3]
        ]

        bw = random.choice(arc)

        return Bow(bw[0], bw[1], bw[2], bw[3], bw[4])

    return Bow(name, image=img, atk= random.randint(atk_min, atk_max), value= random.randint(value_min, value_max), portee= random.randint(range_min, range_max))
