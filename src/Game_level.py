import pygame

from src import Global
from src import Game_room
from src.Game_Object.Map.terrain.Porte import Porte
from src.Game import game
from src import inventory
from src.Game_Object.Personnages import Player, Zombi
from src.Game_Object.Objets import Arme
from src.Game_Object.Objets import Sword
from src.Game_Object.Objets import Bow
from src.Game_Object.Objets import Tete
from src.Game_Object.Map.Generator.game_generator import generate_room, generate_level
import random


def game_level():
    #test
    my_inventory = inventory.inventory()
    imgcasque = pygame.image.load('sprite/wall.png')
    helmet = Tete.Tete("casque", imgcasque, 1, 10)
    imgepee = pygame.image.load('sprite/ble.png')
    sword = Sword.Sword("epee", imgepee, 100, 10)
    bow = Bow.Bow("bow", imgepee, 100, 10)
    #my_inventory.pick(sword)
    #my_inventory.pick(bow)
    player = Zombi.Zombi(img=Global.zombie, nom="You", inventory=my_inventory, posX=1, posY=1)

    continuer=1
    while continuer:
        pygame.mixer.music.load('sprite/music.mp3')
        pygame.mixer.music.play(-1)
        nb_room = random.randint(7,12)
        lvl=generate_level(nb_room=nb_room)
        player=Game_room.game_room(lvl,player)
        if not player:
            pygame.mixer.music.stop()

            continuer=0

