import pygame

from src import Global
from src.Game_Object.Map.Room import Room
from src.Game_Object.Map.Porte import Porte
from src.Game_Object.terrain.ground import Ground
from src.Game import game
from src.Game_Object.Personnages import Personnage
from src import inventory
from src.Game_Object.Objets import Arme
from src.Game_Object.Objets import Tete
from src.Game_Object.Map.Generator.game_generator import generate_room
import copy
from pygame.locals import *


# Fonction pour tester


width = 1500
height = 704

window = Global.window

# chargement des images
grass1 = Global.grass1
grass2 = Global.grass2
ble = Global.ble
wall = Global.wall

# creation de la map
map_x = 17
map_y = 11



# creation de personnages
my_inventory = inventory.inventory()
bob_sprite = pygame.image.load('sprite/Zombie_Bowman.png')
bob = Personnage.Personnage(bob_sprite, "bob", "i m bob i have 20hp 10 armor 10 atk i m level 2 and shield are weaker in overwatch blbaalblablblablablllaalblbalabllbalablbalbalbalbalbalalbalball", my_inventory)
billy_sprite = pygame.image.load('sprite/miner.png')
billy = Personnage.Personnage(billy_sprite, "billy", "he is bob", my_inventory, 100, 0, 9, 9)
imgcasque = pygame.image.load('sprite/wall.png')
helmet=Tete.Tete("casque",imgcasque, 1, 10)
imgepee = pygame.image.load('sprite/ble.png')
sword=Arme.Arme("epee",imgepee, 1, 10)
bob.inventory.stuff[0][1] = helmet
bob.inventory.stuff[0][0] = sword
# character_tab est le tableau contenant tput les personnages de la salle
character_tab = []
character_tab.append(bob)
character_tab.append(billy)
# creation de la salle
Porte=Porte(0,0,0)
first_room = generate_room(0,0,0,"champs",pos_portes=[Porte,0,0,0])


# ancement de la salle
game( first_room, character_tab)
