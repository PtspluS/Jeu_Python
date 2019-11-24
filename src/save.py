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
