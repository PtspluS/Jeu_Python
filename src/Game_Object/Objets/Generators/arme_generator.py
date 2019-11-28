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

    if rarete <=1 :
        value_max = 1000
        value_min = 10

        img = Global.epe2

        atk_max = 30
        atk_min = 5

        name = random.choice(epe_type)+" "+random.choice(adj_1)

    elif rarete == 2:
        value_max = 2500
        value_min = 500

        img = Global.epe2

        atk_max = 50
        atk_min = 20

        name = random.choice(epe_type) + " " + random.choice(adj_2)
    elif rarete == 3:
        value_max = 8000
        value_min = 1000

        img = Global.epe3

        atk_max = 100
        atk_min = 50

        name = random.choice(epe_type) + " " + random.choice(adj_3)
    elif rarete == 4:
        legendaire = [
            ["Flamberge volcanique", Global.epe4, 169, 16753],
            ["Sabre de damocles", Global.epe4, 160, 14985],
            ["Epee en diamand", Global.epe4, 156, 10185],
            ["Claymor nordique", Global.epe4, 179, 11140],
            ["Manoda", Global.epe4, 183, 19566],
            ["Hotmourne", Global.epe4, 164,  17083],
            ["Slave Sword", Global.epe4, 151, 11230]
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

        value_min = 10
        value_max = 1000

        atk_min = 10
        atk_max = 30

        name = random.choice(arc_type)+' '+random.choice(adj_1)
        img = Global.arc1

    elif rarete == 2:
        range_min = 3
        range_max = 6

        value_min = 800
        value_max = 2500

        atk_min = 20
        atk_max = 50

        name = random.choice(arc_type) + ' ' + random.choice(adj_2)
        img = Global.arc1

    elif rarete == 3:
        range_min = 4
        range_max = 6

        value_min = 3000
        value_max = 7500

        atk_min = 55
        atk_max = 95

        name = random.choice(arc_type) + ' ' + random.choice(adj_3)
        img = Global.arc1

    elif rarete == 4:
        arc = [
            ["Gandiva", Global.arc4, 134, 10000, 8],
            ["Vijaya", Global.arc4, 126, 11485, 9],
            ["Penelope", Global.arc4, 145, 19352, 12],
            ["Arc de Paris", Global.arc4, 200, 18123, 3]
        ]

        bw = random.choice(arc)

        return Bow(bw[0], bw[1], bw[2], bw[3], bw[4])

    return Bow(name, image=img, atk= random.randint(atk_min, atk_max), value= random.randint(value_min, value_max), portee= random.randint(range_min, range_max))
