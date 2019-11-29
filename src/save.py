from pymongo import MongoClient
import pickle
from datetime import datetime


def save_game(level, player, path = 'local'):
    """
    save the game into the db
    :param level: current level generated
    :param player: current player
    :param path: path to save
    """
    # on serealize pour save
    save = {
        "date" : str(datetime.now()),
        "player" : pickle.dumps(player),
        #"level" : pickle.dumps(level)
    }

    if path == 'local':
        client = MongoClient('mongodb://localhost:27017/')
    else :
        client = MongoClient(path)

    try :
        mydb = client['game_python']

        mycol = mydb['save']

        mycol.insert_one(save)

    except Exception:
        print(Exception)


def load_save(path="local"):

    if path == 'local':
        client = MongoClient('mongodb://localhost:27017/')
    else:
        client = MongoClient(path)

    try:
        mydb = client['game_python']

        mycol = mydb['save']

        save = mycol.find().sort("date", -1)[0]

        return pickle.loads(save['player'])
    except Exception:
        print(Exception)


def save_achivement_first_kill(player, path = 'local'):
    save = {
        'date' : str(datetime.now()),
        'name' : player.name,
        'achievement': "Le meurtre est l'ultime échec de la parole.",
        "description": "Tuer sa première victime en tant que monstre."
    }

    if path == 'local':
        client = MongoClient('mongodb://localhost:27017/')
    else :
        client = MongoClient(path)

    try :
        mydb = client['game_python']

        mycol = mydb["Le meurtre est l'ultime échec de la parole."]

        # si l'achievements et pas fait on le met dans la collection
        if mycol.count() == 0:
            mycol.insert_one(save)

    except Exception:
        print(Exception)


def save_achivement_first_respawn(player, path = 'local'):
    save = {
        'date': str(datetime.now()),
        'name': player.name,
        "achievement": "La mort est une journée qui mérite d'être vécu.",
        "description": "Ressuciter dans une de vos victime pour la première fois."
    }

    if path == 'local':
        client = MongoClient('mongodb://localhost:27017/')
    else:
        client = MongoClient(path)

    try:
        mydb = client['game_python']

        mycol = mydb["La mort est une journée qui mérite d'être vécu."]

        # si l'achievements et pas fait on le met dans la collection
        if mycol.count() == 0:
            mycol.insert_one(save)

    except Exception:
        print(Exception)