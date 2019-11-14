import pygame
from room import room
from terrain.ground import Ground
from Game import game
from Gameobject import Personnage
from Gameobject import inventory
from Gameobject import Arme
from Gameobject import Tete
import copy
from pygame.locals import *

# Fonction pour tester

pygame.init()
width = 1500
height = 704

window = pygame.display.set_mode((width, height))

# chargement des images
grass1 = pygame.image.load('sprite/Grass1.png')
grass2 = pygame.image.load('sprite/Grass2.png')
ble = pygame.image.load('sprite/ble.png')
wall = pygame.image.load('sprite/Wall.png')

# creation de la map
map_x = 17
map_y = 11

tab_map = []
for i in range(0, map_x):
    malist = []
    for j in range(0, map_y):
        malist.append(Ground(i, j, grass1))
    tab_map.append(malist)

# creation de personnages
my_inventory = inventory.inventory()
bob_sprite = pygame.image.load('sprite/Zombie_Bowman.png')
bob = Personnage.Personnage(bob_sprite, "bob", "he is bob", my_inventory)
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
first_room = room(tab_map, character_tab)
first_room.generate(window)

# ancement de la salle
game(window, first_room, character_tab)
